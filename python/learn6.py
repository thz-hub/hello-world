"""
with open('a.txt') as file:
    c = file.read()
print(c.rstrip())

with open('a.txt') as file:
    for line in file:
        print(line.rstrip())

with open('a.txt') as file:
    lines = file.readlines()

for lin in lines:
    print(lin.rstrip())
"""
with open('pi.txt') as file:
    lines = file.readlines()

pi = ''
for line in lines:
    pi += line.rstrip()

print(pi)
print(len(pi))

birthday = input('生日:')
if birthday in pi:
    print('yes')
    m = "yes"
else:
    print('no')
    m = "no"

with open('write.txt', 'w') as file_write:
    file_write.write(pi)
with open('write.txt', 'a') as file_write:
    file_write.write(m)
