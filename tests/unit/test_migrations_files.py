from os import listdir
import re

from stacktach import migrations

from tests.unit import StacktachBaseTestCase


class MigrationsTestCase(StacktachBaseTestCase):
    def test_no_duplicate_numbers(self):
        migrs = {}

        migrations_file = migrations.__file__
        migrations_dir = migrations_file[:-len('__init__.py')-1]

        migr_match = re.compile('^[0-9]{4}.*.py$')
        files = [f for f in listdir(migrations_dir)
                 if re.match(migr_match, f)]

        for f in files:
            migr_number = f[0:4]
            migr_list = migrs.get(migr_number, [])
            migr_list.append(f)
            migrs[migr_number] = migr_list
            if len(migr_list) > 1:
                msg = "Duplicate migrations found for number %s." % migr_number
                self.fail(msg)