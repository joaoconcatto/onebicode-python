from pathlib import Path


p1 = Path('auto-email', 'files', 'teste.txt')

print(p1)
print(p1.name)
print(p1.stem)
print(p1.suffix)
print(p1.exists())

if p1.exists():
    with open(p1, 'r', encoding='utf-8') as file:
        print(file.read())

p2 = Path('auto-1')

if p2.exists() == False:
    with open(p2, 'w', encoding='utf-8') as file:
        file.write("Arquivo .txt de teste")

print(list(p2.iterdir()))