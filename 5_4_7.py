class DateError(Exception):
    pass

class DateString:
    def __init__(self, date_string):
        try:
            lst = date_string.split('.')
            d, m, y = map(int, lst)
        except ValueError:
            raise DateError
        if not 1 <= d <= 31 or not 1 <= m <= 12 or not 1 <= y <= 3000:
            raise DateError
        self.d, self.m, self.y = self.data_corr(lst)

    def __str__(self):
        return f'{self.d}.{self.m}.{self.y}'

    @staticmethod
    def data_corr(value):
        to_return = [i.rjust(2, '0')if len(i) == 1 else i for i in value]
        return to_return


date_string = input()

try:
    date = DateString(date_string)
except DateError:
    print("Неверный формат даты")
else:
    print(date)
