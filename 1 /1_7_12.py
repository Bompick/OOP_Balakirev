vault: dict = {}


class Message:
    def __init__(self, text: str, fl_like: bool = False):
        self.text = text
        self.fl_like = fl_like


class Viber:
    @staticmethod
    def add_message(msg):
        vault[id(msg)] = msg

    @staticmethod
    def remove_message(msg):
        if id(msg) in vault:
            vault.pop(id(msg))

    @staticmethod
    def set_like(msg):
        if id(msg) in vault:
            if vault[id(msg)].fl_like:
                vault[id(msg)].fl_like = False
            else:
                vault[id(msg)].fl_like = True

    @staticmethod
    def show_last_message(number):
        dct_list = list(vault.items())
        for i, j in dct_list[-number:]:
            print(j.text)

    @staticmethod
    def total_messages():
        return len(vault)


dsg = Message("Всем привет!")
Viber.add_message(dsg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
print(Viber.total_messages())
Viber.show_last_message(2)
Viber.set_like(dsg)