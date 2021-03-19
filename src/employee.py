import re
from datetime import datetime
from variables import weekDays, weekendDays, timeRange1, timeRange2, timeRange3, weekValues, weekendValues

class Employee:
    """
    class Employee
    we create this class, Because we want to increase the functionalities more than just calculating the payment
    in the future.
    """
    def __init__(self, name):
        self.name = name
        self.__payment = 0
        self.timeRange1 = timeRange1
        self.timeRange2 = timeRange2
        self.timeRange3 = timeRange3

    def calculatePayment(self, data):
        """
        this function calculates the payment
        """
        total = 0
        for dateStr in data:
            hourStart, hourEnd = self.hoursFromStr(dateStr)
            timeStartRange, timeEndRange = self.hourTimeRange(hourStart, hourEnd)
            timeValues = {'hourS': hourStart, 'hourE': hourEnd, 'startRange': timeStartRange, 'endRange': timeEndRange}
            if any(map(dateStr.__contains__, weekDays)):
                total += self.calculateValue(timeValues, weekValues)
            elif any(map(dateStr.__contains__, weekendDays)):
                total += self.calculateValue(timeValues, weekendValues)
        self.__payment = total

    def calculateValue(self, timeValues, hourPrices):
        priceRange = 0
        if timeValues['startRange'] == 1 and timeValues['endRange'] == 1:
            priceRange = ((timeValues['hourE'] - timeValues['hourS']).seconds/3600)*hourPrices[0]
        if timeValues['startRange'] == 1 and timeValues['endRange'] == 2:
            pricePart1 = ((timeValues['hourE'] - self.timeRange1[1]).seconds/3600)*hourPrices[1]
            pricePart2 = ((self.timeRange1[1] - timeValues['hourS']).seconds/3600)*hourPrices[0]
            priceRange = pricePart1 + pricePart2
        if timeValues['startRange'] == 1 and timeValues['endRange'] == 3:
            pricePart1 = ((timeValues['hourE'] - self.timeRange2[1]).seconds/3600)*hourPrices[2]
            pricePart2 = 9 * hourPrices[1]
            pricePart3 = ((self.timeRange1[1] - timeValues['hourS']).seconds/3600)*hourPrices[0]
            priceRange = pricePart1 + pricePart2 + pricePart3
        if timeValues['startRange'] == 2 and timeValues['endRange'] == 2:
            priceRange = ((timeValues['hourE'] - timeValues['hourS']).seconds/3600)*hourPrices[1]
        if timeValues['startRange'] == 2 and timeValues['endRange'] == 3:
            pricePart1 = ((timeValues['hourE'] - self.timeRange2[1]).seconds/3600)*hourPrices[2]
            pricePart2 = ((self.timeRange2[1] - timeValues['hourS']).seconds/3600)*hourPrices[1]
            priceRange = pricePart1 + pricePart2
        if timeValues['startRange'] == 2 and timeValues['endRange'] == 1:
            pricePart1 = ((timeValues['hourE'] - self.timeRange1[0]).seconds/3600)*hourPrices[0]
            pricePart2 = 6 * hourPrices[2]
            pricePart3 = ((self.timeRange2[1] - timeValues['hourS']).seconds/3600)*hourPrices[1]
            priceRange = pricePart1 + pricePart2 + pricePart3
        if timeValues['startRange'] == 3 and timeValues['endRange'] == 3:
            priceRange = ((timeValues['hourE'] - timeValues['hourS']).seconds/3600)*hourPrices[2]
        if timeValues['startRange'] == 3 and timeValues['endRange'] == 1:
            pricePart1 = ((timeValues['hourE'] - self.timeRange1[0]).seconds/3600)*hourPrices[0]
            pricePart2 = ((self.timeRange3[1] - timeValues['hourS']).seconds/3600)*hourPrices[2]
            priceRange = pricePart1 + pricePart2
        if timeValues['startRange'] == 3 and timeValues['endRange'] == 2:
            pricePart1 = ((timeValues['hourE'] - self.timeRange2[1]).seconds/3600)*hourPrices[1]
            pricePart2 = 9 * hourPrices[0]
            pricePart3 = ((self.timeRange3[1] - timeValues['hourS']).seconds/3600)*hourPrices[2]
            priceRange = pricePart1 + pricePart2 + pricePart3
        return priceRange


    def hoursFromStr(self, str):
        hoursStr = str[2:]
        hoursStrSplited = re.split('-', hoursStr)
        hourStart = datetime.strptime(hoursStrSplited[0], '%H:%M') - datetime(1900, 1, 1)
        hourEnd = datetime.strptime(hoursStrSplited[1], '%H:%M') - datetime(1900, 1, 1)
        return hourStart, hourEnd

    def hourTimeRange(self, hourStart, hourEnd):
        timeStartRange = 0
        timeEndRange = 0
        if hourStart >= self.timeRange3[0]:
            timeStartRange = 3
        elif hourStart >= self.timeRange2[0]:
            timeStartRange = 2
        elif hourStart >= self.timeRange1[0]:
            timeStartRange = 1

        if hourEnd <= self.timeRange1[1]:
            timeEndRange = 1
        elif hourEnd <= self.timeRange2[1]:
            timeEndRange = 2
        elif hourEnd <= self.timeRange3[1]:
            timeEndRange = 3
        return timeStartRange, timeEndRange

    def getPayment(self):
        return self.__payment








