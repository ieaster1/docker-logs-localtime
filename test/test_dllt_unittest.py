import unittest
import pytz
from dockerlogslocaltime import dllt

class Testdllt(unittest.TestCase):

    def test_convert_ts(self):
        tz = pytz.timezone('America/New_York')
        test_line = '2020-08-13T17:15:09.076574586Z Hello from Docker!'
        valid_output = '2020-08-13 13:15:09 Hello from Docker!'

        self.assertEqual(
                dllt.convert_ts(test_line, tz),
                valid_output, 
                f'Should be {valid_output}')

if __name__ == "__main__":
  unittest.main()