import json

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

file = 'numbers.json'
with open(file, 'w') as f:
    json.dump(numbers, f)

with open(file, 'r') as r:
    num = json.load(r)
print(num)
