from random import choice
from images import vse_slova


zagadannye_clova='стопа грязь гроза арбуз сабля отпор рынок лимон жизнь фишка атлет право ссора богач смола вывод опора чехол спина тупик вождь цифра биржа смысл рубль посох комар ворон'


print('             Игра 5букв')
print('''Правила:
есть загаданное слово из пяти букв
вы должны вводить слова и отгадать его при помощи следующих подсказок:
_т___ - значит, что буква т стоит на своем месте в слове.
Если вы видите "в слове есть буква о" - это значит, что буква о стоит не на своем месте.
Если же вам пишут только кол-во оставшхся попыток, значит ни одной буквы из введенного вами слова нет в загаданном.
Вам нельзя(и у вас все равно не получится) менять форму слов и их падежи, вводить несуществующие слова, глаголы и слова, в которых не 5 букв. Удачи!''')
s = choice(zagadannye_clova.split())
a = input('''
введите слово из пяти букв: ''')

b =7
a = a.lower()
while b>1:
    while len(a) != 5:
        print('тут не пять букв!')
        a = input('введите слово из пяти букв: ')
    while a not in vse_slova:
        a = input('введите существующее слово: ')
    if a ==s:
        print(f'ты победил, правильное слово {s}')
        b=-20
    else:
        m = 0
        m2 = ''
        m3 = 0
        m1 = 0
        j = 0
        x = ''
        u = 0
        m5 = 0
        m6 = 0
        m7 = ''
        d = ''
        if a[0] in s and a[0] == s[0] and a[1] != s[1] and a[2] != s[2] and a[3] != s[3] and a[4] != s[4]:
            print(f'{a[0]}____')
        if a[0] in s and a[0] == s[0] and a[1] == s[1] and a[2] != s[2] and a[3] != s[3] and a[4] != s[4]:
            print(f'{a[0]}{a[1]}___')
        if a[0] in s and a[0] == s[0] and a[1] != s[1] and a[2] == s[2] and a[3] != s[3] and a[4] != s[4]:
            print(f'{a[0]}_{a[2]}__')
        if a[0] in s and a[0] == s[0] and a[1] != s[1] and a[2] != s[2] and a[3] == s[3] and a[4] != s[4]:
            print(f'{a[0]}__{a[3]}_')
        if a[0] in s and a[0] == s[0] and a[1] != s[1] and a[2] != s[2] and a[3] != s[3] and a[4] == s[4]:
            print(f'{a[0]}___{a[4]}')
        if a[0] in s and a[0] == s[0] and a[1] == s[1] and a[2] == s[2] and a[3] != s[3] and a[4] != s[4]:
            print(f'{a[0]}{a[1]}{a[2]}__')
        if a[0] in s and a[0] == s[0] and a[1] == s[1] and a[2] != s[2] and a[3] == s[3] and a[4] != s[4]:
            print(f'{a[0]}{a[1]}_{a[3]}_')
        if a[0] in s and a[0] == s[0] and a[1] == s[1] and a[2] != s[2] and a[3] != s[3] and a[4] == s[4]:
            print(f'{a[0]}{a[1]}__{a[4]}')
        if a[0] in s and a[0] == s[0] and a[1] != s[1] and a[2] == s[2] and a[3] != s[3] and a[4] == s[4]:
            print(f'{a[0]}_{a[2]}_{a[4]}')
        if a[0] in s and a[0] == s[0] and a[1] != s[1] and a[2] != s[2] and a[3] == s[3] and a[4] == s[4]:
            print(f'{a[0]}__{a[3]}{a[4]}')
        if a[0] in s and a[0] == s[0] and a[1] != s[1] and a[2] == s[2] and a[3] == s[3] and a[4] != s[4]:
            print(f'{a[0]}_{a[2]}{a[3]}_')
        if a[0] in s and a[0] == s[0] and a[1] == s[1] and a[2] == s[2] and a[3] == s[3] and a[4] != s[4]:
            print(f'{a[0]}{a[1]}{a[2]}{a[3]}_')
        if a[0] in s and a[0] == s[0] and a[1] != s[1] and a[2] == s[2] and a[3] == s[3] and a[4] == s[4]:
            print(f'{a[0]}_{a[2]}{a[3]}{a[4]}')
        if a[0] in s and a[0] == s[0] and a[1] == s[1] and a[2] == s[2] and a[3] != s[3] and a[4] == s[4]:
            print(f'{a[0]}{a[1]}{a[2]}_{a[4]}')
        if a[0] in s and a[0] == s[0] and a[1] == s[1] and a[2] != s[2] and a[3] == s[3] and a[4] == s[4]:
            print(f'{a[0]}{a[1]}_{a[3]}{a[4]}')
        if a[1] in s and a[0] != s[0] and a[1] == s[1] and a[2] == s[2] and a[3] == s[3] and a[4] == s[4]:
            print(f'_{a[1]}{a[2]}{a[3]}{a[4]}')
        if a[1] in s and a[0] != s[0] and a[1] == s[1] and a[2] == s[2] and a[3] == s[3] and a[4] != s[4]:
            print(f'_{a[1]}{a[2]}{a[3]}_')
        if a[1] in s and a[0] != s[0] and a[1] == s[1] and a[2] == s[2] and a[3] != s[3] and a[4] == s[4]:
            print(f'_{a[1]}{a[2]}_{a[4]}')
        if a[1] in s and a[0] != s[0] and a[1] == s[1] and a[2] != s[2] and a[3] == s[3] and a[4] == s[4]:
            print(f'_{a[1]}_{a[3]}{a[4]}')
        if a[1] in s and a[0] != s[0] and a[1] == s[1] and a[2] == s[2] and a[3] != s[3] and a[4] != s[4]:
            print(f'_{a[1]}{a[2]}__')
        if a[1] in s and a[0] != s[0] and a[1] == s[1] and a[2] != s[2] and a[3] == s[3] and a[4] != s[4]:
            print(f'_{a[1]}_{a[3]}_')
        if a[1] in s and a[0] != s[0] and a[1] == s[1] and a[2] != s[2] and a[3] != s[3] and a[4] == s[4]:
            print(f'_{a[1]}__{a[4]}')
        if a[1] in s and a[0] != s[0] and a[1] == s[1] and a[2] != s[2] and a[3] != s[3] and a[4] != s[4]:
            print(f'_{a[1]}___')
        if a[2] in s and a[0] != s[0] and a[1] != s[1] and a[2] == s[2] and a[3] == s[3] and a[4] == s[4]:
            print(f'__{a[2]}{a[3]}{a[4]}')
        if a[2] in s and a[0] != s[0] and a[1] != s[1] and a[2] == s[2] and a[3] == s[3] and a[4] != s[4]:
            print(f'__{a[2]}{a[3]}_')
        if a[2] in s and a[0] != s[0] and a[1] != s[1] and a[2] == s[2] and a[3] != s[3] and a[4] == s[4]:
            print(f'__{a[2]}_{a[4]}')
        if a[2] in s and a[0] != s[0] and a[1] != s[1] and a[2] == s[2] and a[3] != s[3] and a[4] != s[4]:
            print(f'__{a[2]}__')
        if a[3] in s and a[0] != s[0] and a[1] != s[1] and a[2] != s[2] and a[3] == s[3] and a[4] == s[4]:
            print(f'___{a[3]}{a[4]}')
        if a[3] in s and a[0] != s[0] and a[1] != s[1] and a[2] != s[2] and a[3] == s[3] and a[4] != s[4]:
            print(f'___{a[3]}_')
        if a[4] in s and a[0] != s[0] and a[1] != s[1] and a[2] != s[2] and a[3] != s[3] and a[4] == s[4]:
            print(f'____{a[4]}')
        for i in range(5):
            if a[i] == s[i]:
                m5 += 1
        if a[0] in s and a[0] == s[0]:
            x += a[0]
        if a[1] in s and a[1] == s[1]:
            x += a[1]
        if a[2] in s and a[2] == s[2]:
            x += a[2]
        if a[3] in s and a[3] == s[3]:
            x += a[3]
        if a[4] in s and a[4] == s[4]:
            x += a[4]
        for m in range(5):
            if s.count(s[m]) < 2:
                j += 1
            if a.count(a[m]) >= 2:
                m1 = 3
            if s.count(s[m]) >= 2:
                m7 += s[m]
        if m1 == 3:
            if a[0] in s and a[0] != s[0]:
                d += a[0]
            if a[1] in s and a[1] != s[1]:
                d += a[1]
            if a[2] in s and a[2] != s[2]:
                d += a[2]
            if a[3] in s and a[3] != s[3]:
                d += a[3]
            if a[4] in s and a[4] != s[4]:
                d += a[4]
            if len(d) == 1 and j != 5 and d in m7:
                m6 = 6
            if d != '' and m6 == 0:
                for m in range(5):                                                   # это просто ######, не работает. Надо сделать, чтобы бат ай ивен кам бек афтер даинг... ай эм креате ооооооф лоооооов. какая песня крутая.
                    if a.count(a[m]) >= 2 and a[m] in s and a[m] in d:
                        m3 = 3
                        m2 += a[m]
                if len(m2) > 0:
                    if m2.count(m2[0]) >= 2:
                        m2 = list(m2)
                        m2.remove(m2[0])
                        u = ''
                        for i1 in m2:
                            u += str(i1)
                        m2 = u
                if m5 != 0 or j != 5:
                    for i2 in range(2):
                        if len(m2) >= 2:
                            if m2.count(m2[0]) >= 2:
                                m2 = list(m2)
                                m2.remove(m2[0])
                                u = ''
                                for i1 in m2:
                                    u += str(i1)
                                m2 = u
                            if len(m2) >= 2:
                                if m2.count(m2[1]) >= 2:
                                    m2 = list(m2)
                                    m2.remove(m2[1])
                                    u = ''
                                    for i1 in m2:
                                        u += str(i1)
                                    m2 = u
            if m3 == 3:
                if m2 != '':
                    d = list(d)
                    for m in range(len(m2)):
                        d.remove(m2[m])
                    u = ''
                    for el in d:
                        u += str(el)
                    d = u                              # победа... 03:46 01.04.2025   после четырех бессоных ночей... я закончил... ОНО РАБОТАЕТ, И ЭТО ДАЖЕ НЕ ШУТКА НА 1 АПРЕЛЯ
        else:
            if a[0] in s and a[0] != s[0]:
                d += a[0]
            if a[1] in s and a[1] != s[1]:
                d += a[1]
            if a[2] in s and a[2] != s[2]:
                d += a[2]
            if a[3] in s and a[3] != s[3]:
                d += a[3]
            if a[4] in s and a[4] != s[4]:
                d += a[4]
        if a[0] in s and a[0] != s[0] or a[1] in s and a[1] != s[1] or a[2] in s and a[2] != s[2] or a[3] in s and a[3] !=s[3] or a[4] in s and a[4] != s[4] and len(d)!=0:
             print('в слове есть буквы(а) ', end='')
             if len(d)==5:
                 print(d[0], d[1], d[2], d[3], d[4], sep=', ')
             elif len(d)==4:
                 print(d[0], d[1], d[2], d[3], sep=', ')
             elif len(d)==3:
                 print(d[0], d[1], d[2], sep=', ')
             elif len(d)==2:
                 print(d[0], d[1], sep=', ')
             elif len(d)==1:
                 print(d[0])
        b -= 1
        print(f'осталось попыток: {b}')
        a = input('введите слоао из пяти букв: ')
if a == s and b>=1:
    print(f'ты победил, правильное слово {s}')
    b = -20
if -10<b<=1:
    print(f'попытки закончились, вы проиграли. Правильное слово {s}')

