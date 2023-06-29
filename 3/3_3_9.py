
class Clock:
    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def get_time(self):
        return self._hours*3600 + self._minutes*60+self._seconds

class DeltaClock:
    def __init__(self, clock1, clock2):
        self._clock1 = clock1
        self._clock2 = clock2

    def __str__(self):
        delta = self.__len__()
        hours = delta // 3600
        minutes = delta % 3600 // 60
        seconds = delta % 3600 % 60
        return f'{hours:02}: {minutes:02}: {seconds:02}'

    def __len__(self):
        delta = self._clock1.get_time() - self._clock2.get_time()
        return delta if delta > 0 else 0



dt = DeltaClock(Clock(12, 10, 10), Clock(2, 0, 0))
print(dt)
a = len(dt)
print(a)
