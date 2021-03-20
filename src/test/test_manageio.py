import unittest
from manage_io import *


class TestManageio(unittest.TestCase):

    def test_validateInput(self):
        lines = ['ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00',
                 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',
                 'MARIA=MO10:00-12:00,TI12:00-14:00,SU20:00-21:00']
        self.assertEqual(validateInput(lines), [['ASTRID', 'MO10:00-12:00', 'TH12:00-14:00', 'SU20:00-21:00'],
                                                ['RENE', 'MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00','SU20:00-21:00'],
                                                [3]])


if __name__ == "__main__":
    unittest.main()