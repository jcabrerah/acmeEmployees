import unittest
from src.employee import *


class TestEmployee(unittest.TestCase):

    def test_calculatePayment(self):
        employee = Employee('prueba')
        dataTest = ['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00-21:00']
        employee.calculatePayment(dataTest)
        self.assertEqual(employee.getPayment(), 215)
        employee2 = Employee('prueba2')
        dataTest = ['MO10:00-12:00', 'TH12:00-14:00', 'SU20:00-21:00']
        employee2.calculatePayment(dataTest)
        self.assertEqual(employee2.getPayment(), 85)


if __name__ == "__main__":
    unittest.main()