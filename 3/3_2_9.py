class Handler:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            if len(request)==0 or 'method' not in request or \
                    request['method']  == "GET" and request['method'] in self.methods:
                return self.get(func, request)
            elif request['method'] not in self.methods:
                return None
            elif request['method'] == "POST" and request['method'] in self.methods:
                return self.post(func, request)
        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"

    def post(self, func, request, *args, **kwargs):
        return f"POST: {func(request)}"


def contact(request):
    return "Сергей Балакирев"


tr1 = Handler() # создаем экз класса,  передаем ему разрешенные методы(аргумент фуекции декоратора)
res = tr1(contact) # вызываем объект класса,  в качестве аргумента -  оборачиваемая функция,
# возвращает фуункцию  обертку, которую  присваиваем переменной
print(res({"method": "POST", "url": "contact.html"})) # в обертке проверяем,  могут
# ли переданные аргументы использоваться

assert hasattr(Handler, 'get') and hasattr(Handler, 'post'), "класс Handler должен содержать методы get и post"

@Handler(methods=('GET', 'POST'))
def contact2(request):
    return "контакты"

assert contact2({"method": "POST"}) == "POST: контакты", "декорированная функция вернула неверные данные"
assert contact2({"method": "GET"}) == "GET: контакты", "декорированная функция вернула неверные данные"
assert contact2({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"
assert contact2({}) == "GET: контакты", "декорированная функция вернула неверные данные при указании пустого словаря"

@Handler(methods=('POST'))
def index(request):
    return "index"

assert index({"method": "POST"}) == "POST: index", "декорированная функция вернула неверные данные"
assert index({"method": "GET"}) is None, "декорированная функция вернула неверные данные"
assert index({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"