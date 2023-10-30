class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, request, *args, **kwargs):
        return self.get(self.func, request)

    def get(self, func, request, *args, **kwargs):
        if 'method' not in request or request['method'] == "GET":
            return f"GET: {self.func(request)}"
        else:
            return None


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


print(contact({"method": "POST", "url": "contact.html"}))


@HandlerGET
def index(request):
    return "главная страница сайта"


res = index({"method": "GET"})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"
res = index({"method": "POST"})
assert res is None, "декорированная функция вернула неверные данные"
res = index({"method": "POST2"})
assert res is None, "декорированная функция вернула неверные данные"

res = index({})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"

