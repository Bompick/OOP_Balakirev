class Player:
    def __init__(self, name, old, score):
        self.name = name
        if type(old) is str or type(score) is str:
            old = int(old)
            score = int(score)
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0



lst_in = ['Балакирев; 34; 2048',
'Mediel; 27; 0',
'Влад; 18; 9012',
'Nina P; 33; 0']

players = [Player(*(line.split("; "))) for line in lst_in]
players_filtered = list(filter(lambda x: bool(x), players))
for i in players_filtered:
    print(i.name)

