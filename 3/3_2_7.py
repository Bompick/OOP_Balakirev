class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list

    def __call__(self, lst, *args, **kwargs):
        mod = ",".join([f"<li>{item}</li>" for item in lst]).replace(",", "\n")
        if self.type_list == "ol":
            return f'''<{self.type_list}>\n{mod}\n</{self.type_list}>'''
        else:
            return f'''<ul>\n{mod}\n</ul>'''


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("bl")
html = render(lst)
print(html)