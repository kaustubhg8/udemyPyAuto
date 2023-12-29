from pathlib import Path


a = Path('files/trial2.txt')

if not Path.exists(a):
    with open(a,'w') as file:
        file.write("Hello")

b = Path('files')
for files in b.iterdir():
    print(files)