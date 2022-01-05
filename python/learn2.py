pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

a = {}
active = True

while active:
    name = input('\nname?')
    aa = input('number?')
    a[name] = aa
    repeat = input('yes/no?')
    if repeat == 'no':
        active = False

for name,aa in a.items():
    print(name,aa)

