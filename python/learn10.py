from random import randint

money = 1000
while money > 0:
    c = False
    while True:
        debt = int(input('输入赌资'))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print(f'摇出了{first}')
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt

    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt

    else:
        c = True

    while c:
        c = False
        current = randint(1, 6) + randint(1, 6)
        print(f'摇出了{current}')
        if current == 7:
            print('庄家胜')
            money -= debt
        elif current == first:
            print('玩家胜')
            money += debt
        else:
            c = True

print('你破产了')
