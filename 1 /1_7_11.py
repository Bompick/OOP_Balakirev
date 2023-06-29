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
app_instagram = Application("Instagram")
app_VK = Application("VK")
store.add_application(app_youtube)
store.add_application(app_instagram)
store.add_application(app_VK)
store.remove_application(app_instagram)


store.block_application(app_VK)