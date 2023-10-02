class Application:
    def __init__(self, name: str, blocked: bool = False):
        self.name = name
        self.blocked = blocked


class AppStore:
    def __init__(self, vault=[]):
        self.vault = vault

    def add_application(self, app):
        self.vault.append(app)

    def remove_application(self, app):
        self.vault.remove(app)

    def block_application(self, app):
        # print(self.vault.index(app))
        self.vault[self.vault.index(app)].blocked = True

    def total_apps(self):
        return len(self.vault)



store = AppStore()
app_youtube = Application("Youtube")
assert app_youtube.blocked == False, "начальное значение blocked должно быть равно False"

store.add_application(app_youtube)
store.block_application(app_youtube)

assert app_youtube.name == "Youtube" and app_youtube.blocked == True, "неверные значения локальных атрибутов объекта класса Application"

app_stepik = Application("Stepik")
store.add_application(app_stepik)

assert store.total_apps() == 2, "неверное число приложений в магазине"

store.remove_application(app_youtube)
assert store.total_apps() == 1, "неверное число приложений в магазине, некорректно работает метод remove_application"