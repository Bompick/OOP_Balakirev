class Aircraft:
    def __init__(self, model, mass, speed, top):
        if self.check_args(model, mass, speed, top):
            self._model = model
            self._mass = mass
            self._speed = speed
            self._top = top

    @staticmethod
    def check_args(*args):
        if type(args[0]) is str and all(map(lambda x: type(x) in (int, float) and x > 0, args[1:])):
            return True
        else:
            raise TypeError('неверный тип аргумента')


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        if type(chairs) is int and chairs > 0:
            self._chairs = chairs
        else:
            raise TypeError('неверный тип аргумента')


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons:dict):
        super().__init__(model, mass, speed, top)
        if type(weapons) is dict and all(map(lambda x: type(x) is str, weapons.keys())) and all(map(lambda x: type(x) is int, weapons.values())):
            self._weapons = weapons
        else:
            raise TypeError('неверный тип аргумента')




planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]





