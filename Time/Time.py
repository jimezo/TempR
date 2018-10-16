class Time:
    def __init__(self, second=0, minute=0, hour=0):
        self.second = second
        self.minute = minute
        self.hour = hour

    def get_second(self):
        hour = self.hour
        minute = self.minute
        second = self.second

        minute += hour * 60
        second += minute * 60
        return second

    def get_minute(self):
        minute = self.minute
        minute += self.second // 60
        return minute

    def get_hour(self):
        minute = self.second // 60
        hour = self.hour
        hour += minute // 60
        return hour

    def get_time(self):
        second = self.second
        minute = self.minute
        hour = self.hour

        minute += second // 60
        second %= 60

        hour += minute // 60
        minute %= 60

        return str(hour) + ' : ' + str(minute) + ' : ' + str(second)

if __name__ == '__main__':
    time = Time(69690, 892, 80)
    print('hour = ' + str(time.get_hour()) )
    print('minute = ' + str(time.get_minute()) )
    print('second = ' + str(time.get_second()) )
    print(time.get_time())
