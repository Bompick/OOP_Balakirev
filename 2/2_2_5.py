class Car:
    def __init__(self):
        self.__model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if type(model) is str and 2 <= len(model) <= 100:
            self.__model = model


car = Car()
car.model = "Toyota"