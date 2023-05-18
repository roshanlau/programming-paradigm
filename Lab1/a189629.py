fin = open('python_file.txt', 'rt')

name = fin.readline()
track = fin.readline()

for i in range(3):
    print(name, end='')
    print(track, end='\n\n')
    
fin.close()