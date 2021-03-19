from datetime import timedelta

weekDays = ['MO', 'TU', 'WE', 'TH', 'FR']
weekendDays = ['SA', 'SU']
timeRange1 = (timedelta(minutes=1), timedelta(hours=9))
timeRange2 = (timedelta(hours=9, minutes=1), timedelta(hours=18))
timeRange3 = (timedelta(hours=18, minutes=1), timedelta(days=1))
weekValues = [25, 15, 20]
weekendValues = [30, 20, 25]