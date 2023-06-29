class StringText:
    def __init__(self, lst_words):
        self.lst = lst_words

    def __len__(self):
        return len(self.lst)

    def __gt__(self, other):
        return self.__len__() > other.__len__()

    def __ge__(self, other):
        return self.__len__() >= other.__len__()


stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

to_delete = "–?!,.;"

lst_text = []
for line in stich:
    new = []
    for let in line:
        if let not in to_delete:
            new.append(let)
        else:
            new.append(' ')
    new_line = ''.join(new)
    fin = new_line.split()
    st = StringText(fin)
    lst_text.append(st)

lst_text_sorted = sorted(lst_text, key=lambda x: len(x), reverse=True)

lst_text_sorted = [' '.join(item.lst) for item in lst_text_sorted]




