class Course:
    def __init__(self, name: str):
        self.name = name
        self.modules: list = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)



class Module:
    def __init__(self, name: str):
        self.name = name
        self.lessons: list = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class LessonItem:
    attrs = {'title': str, 'practices': int, 'duration': int}

    def __init__(self, title: str, practices: int, duration: int):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if (key in ('practices', 'duration') and value > 0 or key == 'title') and self.attrs[key] == type(value):
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in self.attrs:
            raise AttributeError("Этот атрибут удалять нельзя")
        else:
            object.__delattr__(self, item)


# a = LessonItem("Урок 1", 7, 1000)
# print(a.pfg)
# del a.duration

course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)






