class Morph:
    def __init__(self, *args):
        self.words = [*args]

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def get_words(self):
        return tuple(self.words)

    def __eq__(self, other):
        if other.lower() in self.words:
            return True
        else:
            return False


dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
                  Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                        'формулах'),
                  Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                        'векторами', 'векторах'
                        ),
                  Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                        'эффектами', 'эффектах'
                        ), Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'
                                 )]

text = 'Мы будем устанавливать связь завтра днем.'
marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_'''
ne_l = ''.join([let.lower() for let in text if let not in marks]).split()
counter = 0
for word in ne_l:
    for sl in dict_words:
        if word == sl:
            counter += 1
print(counter)

