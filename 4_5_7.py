from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def go(self):
        """Метод для перемещения транспортного средства"""

    @classmethod
    @abstractmethod
    def abstract_class_method(cls):
        """Абстрактный метод класса"""


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        """Метод для получения ID транспортного средства"""

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    counter = 1

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.__class__.counter
        self.__class__.counter += 1

    def get_pk(self):
        return self._id


form = ModelForm("Логин", "Пароль")
print(form.get_pk())


