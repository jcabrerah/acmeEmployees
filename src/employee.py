import re
from datetime import datetime, timedelta
from src.variables import weekDays, weekendDays, timeRange1, timeRange2, timeRange3, \
    weekValues, weekendValues, calcPriceRange, subtractTimedelta

class Employee:
    """
    class Employee
    we create this class, Because we want to increase the functionalities more than just calculating the payment
    in the future.
    """
    def __init__(self, name, timeWorked=['MO08:00-8:00']):
        self.name = name
        self.__payment = 0
        self.timeRange1 = timeRange1
        self.timeRange2 = timeRange2
        self.timeRange3 = timeRange3
        self.__timeWorked = timeWorked
        self.overHoursError = 0

    def calculatePayment(self):
        """
        this function calculates the payment
        """
        total = 0
        for dateStr in self.__timeWorked:
            hourStart, hourEnd = self.hoursFromStr(dateStr)
            if hourEnd == timedelta(0):
                hourEnd = timedelta(days=1)
            timeStartRange, timeEndRange = self.hourTimeRange(hourStart, hourEnd)
            timeValues = {'hourS': hourStart, 'hourE': hourEnd, 'startRange': timeStartRange, 'endRange': timeEndRange}
            if any(map(dateStr.__contains__, weekDays)):
                overHoursError, priceRange=self.calculateValue(timeValues, weekValues)
                if overHoursError == 0:
                    total += priceRange
                else:
                    self.overHoursError = overHoursError
            elif any(map(dateStr.__contains__, weekendDays)):
                overHoursError, priceRange = self.calculateValue(timeValues, weekendValues)
                if overHoursError == 0:
                    total += priceRange
                else:
                    self.overHoursError = overHoursError
        self.__payment = total


    def calculateValue(self, timeValues, hourPrices):
        priceRange = 0
        overHoursError = 0
        index = timeValues['endRange'] - 1
        if timeValues['startRange'] == timeValues['endRange']:
            if timeValues['hourS'] > timeValues['hourE']:
                overHoursError = 1
            priceRange = calcPriceRange(timeValues['hourE'], timeValues['hourS'], hourPrices[index])

        if timeValues['startRange'] == 1 and 1 < timeValues['endRange'] < 4:
            b = self.timeRange1[1]
            pricePart3 = 0
            if timeValues['endRange'] == 3:
                b = self.timeRange2[1]
                pricePart3 = calcPriceRange(self.timeRange2[1], self.timeRange1[1], hourPrices[1])
            priceRange = calcPriceRange(timeValues['hourE'], b, hourPrices[index]) + \
                         calcPriceRange(self.timeRange1[1], timeValues['hourS'], hourPrices[0]) + pricePart3

        if timeValues['startRange'] == 2 and 0 < timeValues['endRange'] < 4 and timeValues['endRange'] != 2:
            b = self.timeRange3[1]
            pricePart3 = calcPriceRange(self.timeRange3[1], self.timeRange2[1], hourPrices[2])
            if timeValues['endRange'] == 3:
                b = self.timeRange2[1]
                pricePart3 = 0
            priceRange = calcPriceRange(timeValues['hourE'], b, hourPrices[index]) + \
                         calcPriceRange(self.timeRange2[1], timeValues['hourS'], hourPrices[1]) + pricePart3

        if timeValues['startRange'] == 3 and timeValues['endRange'] < 3:
            b = self.timeRange1[0]
            pricePart3 = 0
            if timeValues['endRange'] == 2:
                b = self.timeRange1[1]
                pricePart3 = calcPriceRange(self.timeRange1[1], self.timeRange3[1], hourPrices[0])
            priceRange = calcPriceRange(timeValues['hourE'], b, hourPrices[index]) + \
                         calcPriceRange(self.timeRange3[1], timeValues['hourS'], hourPrices[2]) + pricePart3
        return overHoursError, priceRange


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
        elif hourStart >= self.timeRange1[0] - timedelta(minutes=1):
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

    def setTimeWorked(self, timeWorked):
        self.__timeWorked = timeWorked
        self.overHoursError = 0








