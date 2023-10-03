class Server:
    sv_list: list = []

    @classmethod
    def add_to_sv_list(cls):
        cls.sv_list.append(1)
        return len(cls.sv_list)

    def __init__(self):
        self.ip = self.add_to_sv_list() # IP-адрес текущего сервера.
        self.buffer: list = [] # список принятых пакетов (объекты класса Data, изначально пустой);

    @staticmethod
    def send_data(data):
        Router().buffer.append(data)

    def get_data(self):
        lst_to_print: list = []
        if len(self.buffer) == 0:
            return lst_to_print
        else:
            for item in self.buffer:
                lst_to_print.append(item)
            self.buffer = []
            return lst_to_print

    # ready
    def get_ip(self):
        return self.ip


class Router:
    connected: dict = {}
    routers_number = None

    def __new__(cls, *args, **kwargs):
        if cls.routers_number == None:
            cls.routers_number = super().__new__(cls)
        return cls.routers_number

    def __init__(self):
        if len(self.__dict__)== 0:
            self.buffer: list = []

    @classmethod
    def link(cls, server):
        cls.connected[server.ip] = server

    @classmethod
    def unlink(cls, server):
        if server.ip in cls.connected:
            cls.connected.pop(server.ip)

    @classmethod
    def send_data(cls):
        if len(cls().buffer) > 0:
            for i in cls().buffer:
                if i.ip in cls().connected:
                    cls.connected[i.ip].buffer.append(i)
        cls().buffer = []


class Data:
    def __init__(self, data: str, ip: int):
        self.data = data  # передаваемые данные (строка);
        self.ip = ip  # IP-адрес назначения.


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

assert hasattr(Router, 'link') and hasattr(Router, 'unlink') and hasattr(Router, 'send_data'), "в классе Router присутсвутю не все методы, указанные в задании"
assert hasattr(Server, 'send_data') and hasattr(Server, 'get_data') and hasattr(Server, 'get_ip'), "в классе Server присутсвутю не все методы, указанные в задании"

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

assert len(router.buffer) == 0, "после отправки сообщений буфер в роутере должен очищаться"
assert len(sv_from.buffer) == 0, "после получения сообщений буфер сервера должен очищаться"

assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"

assert msg_lst_from[0].data == "Hi" and msg_lst_to[0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"

assert hasattr(router, 'buffer') and hasattr(sv_to, 'buffer'), "в объектах классов Router и/или Server отсутствует локальный атрибут buffer"

router.unlink(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
router.send_data()
msg_lst_to = sv_to.get_data()
assert msg_lst_to == [], "метод get_data() вернул неверные данные, возможно, неправильно работает метод unlink()"