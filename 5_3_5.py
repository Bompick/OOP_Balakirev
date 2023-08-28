class ValidatorString:
    def __init__(self, min_length, max_length, chars):
        self._min_length = min_length
        self._max_length = max_length
        self._chars = chars

    def is_valid(self, string):
        if (len(self._chars) == 0 or
                self._min_length <= len(string) <= self._max_length and len(set(self._chars) & set(string)) > 0):
            return string
        else:
            raise ValueError('недопустимая строка')


class LoginForm:
    def __init__(self, login_validator, password_validator):
        self._login_validator = login_validator
        self._password_validator = password_validator

    def form(self, request: dict):
        if 'login' not in request.keys() or 'password' not in request.keys():
            raise TypeError('в запросе отсутствует логин или пароль')

        log_valid = self._login_validator.is_valid(request['login'])
        pass_valid = self._password_validator.is_valid(request['password'])

        if log_valid and pass_valid:
            self._login = log_valid
            self._password = pass_valid



login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)