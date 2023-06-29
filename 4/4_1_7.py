class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods=('GET',)):
        super().__init__(methods)

    def render_request(self, request, method):
        if method not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        self.act_meth = method.lower()
        a = getattr(self, f'{self.act_meth}')
        return a(request)

    def get(self, request):
        if type(request) is not dict:
            raise TypeError('request не является словарем')
        if 'url' not in request.keys():
            raise TypeError('request не содержит обязательного ключа url')
        return f"url: {request['url']}"


dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')
print(html)
