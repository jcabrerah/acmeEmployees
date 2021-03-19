import argparse
import re

def readCommand(argv):
    """
    Processes the command used to run calculate_payments from the command line.
    """
    howUseStr = """
    USE:      python manage_payments.py
                    -> default values.
                    fileName: input.txt
    with custom file:
             python manage_payments.py --file customName.txt
    """
    parser = argparse.ArgumentParser(howUseStr)

    parser.add_argument("--file", dest="file", type=argparse.FileType('r', encoding='UTF-8'),
                        help="the input file name", metavar="FILE", default="input.txt")
    try:
        args, other = parser.parse_known_args(argv)
        if len(other) != 0:
            raise Exception("input arguments not understood: " + str(other))
        arguments = dict()
        arguments['inFileName'] = args.file.name
        return arguments
    except IOError as msg:
        parser.error(str(msg))


def validateInput(lines):
    goodLines = list()
    for i, line in enumerate(lines, start=1):
        matched = re.fullmatch(
            "([A-Z]{3,20})\=((MO|TU|WE|TH|FR|SA|SU)([0-1]\d|[2][0-3])\:([0-5]\d)\-([0-1]\d|[2][0-3])\:([0-5]\d)(\,|)){1,7}",
            line)
        if matched is not None:
            lineSplit = re.split('=|,', line)
            goodLines.append(lineSplit)
        else:
            goodLines.append([i])
    return goodLines


def loadDataInput(inFileName):
    """
    load data from input file
    Data= customerType, checkInDate, checkOutDate
    """
    try:
        f = open(inFileName, 'r')
        lines = f.read().splitlines()
        goodLines = validateInput(lines)
        f.close()
        return goodLines
    except IOError as msg:
        print(str(msg))


def printOutput(employee):
    print('The amount to pay ' + employee.name + ' is: ' + str(employee.getPayment()) + ' USD')


def printError(line):
    print('Error in line: ' + str(line))