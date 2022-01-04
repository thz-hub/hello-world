favorite_language = 'a python '
print(favorite_language)
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()
print(favorite_language)
print(favorite_language.title())
print(favorite_language.capitalize())

b = ['a', 'b', 'c']
print(b[-2].title())
message = f'this is a {b[0].title()}'
print(message.capitalize())

b[0] = 'd'
print(b[0].title())
print(b)
b.append('f')
print(b)
b.insert(0, 'g')
print(b)
b.sort()
print(b)
del b[0]
print(b)
pop_b = b.pop(0)
print(b)
print(pop_b)
b.sort(reverse=True)
print(b)
print(sorted(b))
for bb in b:
    print(bb)

for value in range(1, 5):
    print(value)

number = list(range(1, 6, 2))
print(number)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)
print(sum(squares))
print(f'Adding {squares}.')

c = {'a': 5, 'b': 8}
print(c['a'])

c['c'] = 9
print(c)
c['c'] = 10
print(c)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# 向右移动外星人。
# 根据当前速度确定将外星人向右移动多远。
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的移动速度肯定很快。
    x_increment = 3
    # 新位置为旧位置加上移动距离。
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

for k, v in alien_0.items():
    print(f'\nk: {k.title()}')
    print(f'v: {v}')

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

print(9 % 4)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
active = True
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        active = False
        break
    else:
        print(message)
        print(active)
