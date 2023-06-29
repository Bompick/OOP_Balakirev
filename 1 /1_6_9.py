TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        cls.DIALOG_TYPE_OS = TYPE_OS
        if cls.DIALOG_TYPE_OS == 1:
             obj = super().__new__(DialogWindows)
             setattr(obj,'name', *args)
             return obj
        else:
            obj = super().__new__(DialogLinux)
            setattr (obj,'name', *args)
            return obj


p = Dialog("Robert")
TYPE_OS =2
e = Dialog("El")
print(isinstance(p,DialogWindows))
print(p.__dict__)
