import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_calculatePayment(self):
        dataTest = [['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00-21:00'],
                    ['MO10:00-12:00', 'TH12:00-14:00', 'SU20:00-21:00'],
                    ['TU10:00-01:30'],
                    ['TU21:00-10:30'],
                    ['TU08:59-17:00'],
                    ['TU07:00-22:00'],
                    ['TU18:00-00:00'],
                    ['TU00:00-09:00'],
                    ['TU09:00-18:00'],
                    ['TU21:00-20:00'],
                    ['TU07:00-07:00'],
                    ['TU07:00-06:00', 'TH10:00-11:00'],
                    ['SU20:00-00:00']]
        totals = [215, 85, 277.5, 307.5, 120.42, 265, 120, 225, 135, 0, 0, 15, 100]
        employee = Employee('test')
        for i, datum in enumerate(dataTest):
            employee.setTimeWorked(datum)
            employee.calculatePayment()
            self.assertEqual(round(employee.getPayment()*100)/100, totals[i])


if __name__ == "__main__":
    unittest.main()