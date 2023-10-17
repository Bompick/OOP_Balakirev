import random
from string import ascii_letters, digits

POSSIBLE_SYMBOLS: str = ascii_letters+digits + "_" + '.'
POSSIBLE_SYMBOLS_: str = POSSIBLE_SYMBOLS + "@"
class EmailValidator:
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        return ''.join((random.choice(POSSIBLE_SYMBOLS) for i in range(random.randint(0, 15))))+"@gmail.com"

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            if all(map(lambda s: s in POSSIBLE_SYMBOLS_, email)) and email.count('@') == 1:
                if 1 <= len(email[:email.find('@gmail.com')]) <= 100:
                    if len(email[email.rfind('@'):]) <=50:
                        if email[email.rfind('@'):].count('.') >=1:
                            if email.count('..')<=0:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    @staticmethod
    def __is_email_str(email):
        return True if type(email) is str else False
    

print(EmailValidator.check_email('1@gmail@com'))

assert EmailValidator.check_email("sc_lib@list.ru") == True and EmailValidator.check_email("sc_lib@list_ru") == False and EmailValidator.check_email("sc@lib@list_ru") == False and EmailValidator.check_email("sc.lib@list_ru") == False and EmailValidator.check_email("sclib@list.ru") == True and EmailValidator.check_email("sc.lib@listru") == False and EmailValidator.check_email("sc..lib@list.ru") == False, "метод check_email отработал некорректно"

m = EmailValidator.get_random_email()
assert EmailValidator.check_email(m) == True, "метод check_email забраковал сгенерированный email методом get_random_email"

assert EmailValidator() is None, "при создании объекта класса EmailValidator возвратилось значение отличное от None"

assert EmailValidator._EmailValidator__is_email_str('abc'), "метод __is_email_str() вернул False для строки"
