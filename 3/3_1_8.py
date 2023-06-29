class SmartPhone:
    def __init__(self, model: str):
        self.model = model
        self.apps: list = []

    def add_app(self, app):
        q = 0
        if len(self.apps) < 1:
            self.apps.append(app)
        else:
            for item in self.apps:
                if item.name == app.name:
                    break
                else:
                    q += 1
            if q == len(self.apps):
                self.apps.append(app)

    def remove_app(self, app):
        if app in self.apps:
            self.apps.remove(app)


class AppVK:
    def __init__(self, name="ВКонтакте" ):
        self.name = name


class AppYouTube:
    def __init__(self, memory_max, name: str = "YouTube", ):
        self.memory_max = memory_max
        self.name = name


class AppPhone:
    def __init__(self, phone_list: dict, name="Phone", ):
        self.phone_list = phone_list
        self.name = name


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)