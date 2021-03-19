import sys
from employee import Employee
from manage_io import readCommand, loadDataInput, printOutput, printError


if __name__ == '__main__':
    """
    the main function is called when manage_payments.py is run from command line
    > python manage_payments.py
    """
    args = readCommand(sys.argv[1:])  # get commands
    data = loadDataInput(**args)
    employees = list()
    for datum in data:
        if datum.__len__() > 1:
            employee = Employee(datum[0], datum[1:])
            employee.calculatePayment()
            printOutput(employee)
            employees.append(employee)
        else:
            printError(datum[0])
    pass
