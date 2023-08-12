class LimitException(Exception):
    """Превышение лимита"""


class ServerLimitException(LimitException):
    """Превышение нагрузки на сервер"""


try:
    raise ServerLimitException('превышение серверной нагрузки')
except LimitException:
    print("LimitException")
except ServerLimitException:
    print("ServerLimitException")