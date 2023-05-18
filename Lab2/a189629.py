info = [('Roshan', '21', 'Ais Tea'), ('Dilshan', '17', 'Ais Lemon Tea'), ('Simran', '22', 'Green Tea')]

dict = {t[0] : (t[1], t[2]) for t in info}

val = ('21', 'Ais Tea')

for key, value in dict.items():
    if value == val:
        print(f'The key for {value} is {key} :)')