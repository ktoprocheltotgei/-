'''from tkinter import *
p = Tk()
l = Canvas(p, width = 320, height = 320, background = 'white')
l.pack()
a=b=0
c=d=40
for i in range(1,5):
    for i in range(1,4):
        l.create_rectangle(a,b,c,d, fill ='black',)
        a +=80
        c +=80
        l.create_rectangle(a, b, c, d, fill='black',)
    a -=200
    b +=40
    c -=200
    d +=40
    for i in range(1,4):
        l.create_rectangle(a, b, c, d, fill='black',)
        a +=80
        c +=80
        l.create_rectangle(a, b, c, d, fill='black',)
    a -=280
    b +=40
    c -=280
    d +=40
mainloop()'''
'''                             неудачная попытка кода 5букв(позже заменил это двумя строчками):
from images import vse_slova
o = vse_slova
j = 0
v = o.replace(' ', '')
g = len(v)
r = g//5
a = str(input())
for i in range(0,50):
    for i in range(r):
        if a != o.split()[j]:
            j +=1
            if j==r:
                a = str(input('введите существительное из пяти букв'))
                j =0
        elif a != o.split()[j]:
            a = str(input('введите существительное из пяти букв'))
            j = 0
'''
'''
a = str(input())
while a not in vse_slova:
    a = str(input('введите существующее слово: '))'''
'''                                                           задачи ОГЭ(и не только):
n = int(input('количество: '))
g = 0
men = 0
maks = 300
for i in range(0, n):
    a = int(input())
    if a >= 1 and a <= 300:
        if a <= 30:
            g += 1
        if maks >=a:
            maks =a
        if men<=a:
            men =a
d = maks - men
print(-d)
print(g)
'''
'''a = int(input())
b = 0
c =0
while a != 0 and a>=10 and a <100 and c<=1000:
    c+=1
    if a %8 == 0:
        b +=a
    else:
        b +=0
    a = int(input())
print(b)
'''
'''from math import ceil
 2^i>=M   M(кол-во символов) 
 2: i(кол-во бит на кодирование одного символа)
 3: надо i умножить на количество символов'''
'''m = 13
i = 4
c = i*18 #в битах
d = c/8 + 55 #на одного человека в байтах
c = ceil((d*64)/1024)
print(c)'''
'''
for a in range(1000, 10000):
    b1 = a%10
    b2 = (a//10)%10
    b3 = (a//100)%10
    b4 = (a//1000)%10
    c1 = b1+b2
    c2 = b3+b2
    c3 = b3 +b4
    d = [c1, c2, c3]
    d.remove(min(d))
    v = max(d)
    v1 = min(d)
    s = str(v1) + str(v)
    if s =='1215':
        print(a)'''
'''
c = 0
for i in range(105105, 1000000):
    b = str(i)
    b1 = b[0]
    b2 = b[1]
    a = b1+b2
    a1 = (i//10)%10
    a2 = i%10
    a3 = str(a1) + str(a2)
    if i%117==0 and a=='99' and a3 =='88':
        c +=1
print(c)'''
'''for i in range(990054, 9900089):
    i1 = str(i)
    if i1[:2] =='99' and i1[-2:]=='88' and i%117==0:
        print(i, i//117)'''

'''
count = 0
n = 3*3125**8+2*625**7-4*625**6+3*125**5-2*25**4-2024
b = 0
c = 0
h = ''
while n > 0:
    if n%25==0:
        count += 1
    c = n%25
    b =c
    n = n // 25
    c = n
    h +=str(b)
print(h[::-1])
print(count)'''
'''count = 0
n = 3*3125**8+2*625**7-4*625**6+3*125**5-2*25**4-2024
b = 0
c = 0
h = ''
while n > 0:
    if n%25==0:
        count += 1
    c = n%25
    b =c
    n = n // 25
    c = n
    h +=str(b)
print(h[::-1])
print(count)'''
'''a = 0
o = 0
for i in range(174457, 174506):
    c = 0
    for b in range(2, 174505):
        if i%b==0:
            c +=1
            if c==1:
                a = b
            elif c==2:
                o = b
    if c==3:
        a1 = max(o, a)
        a2 = min(o, a)
        print(i, a2, a1)'''
'''for i in range(33333, 55556):
    c1 = 0
    d = str(i)
    for b in range(len(d)):
        c = int(d[b])
        c1 +=c
    if c1>35:
        print(i)'''
'''def pp(n):
    d1 = []
    for d in range(1, n+1):
        if n%d==0:
            d1.append(d)
    return sorted(d1)
for n in range(174457, 174506):
    if len(pp(n))==4:
        print(n, pp(n)[1], pp(n)[2])'''
'''                                                     проверяет нетривиальные делители:
from math import ceil
def pp(n):
    d1 = []
    for d in range(1,n+1):
        if n%d==0:
            d1.append(d)
    return sorted(d1)
st = ceil(300000000**0.25)
en = int(500000000**0.25)
for n in range(st, en+1):
    if len(pp(n))==2 :
        print(n**4, n, n**2,n**4//n)'''
'''                                         делал я и чуть чуть учебник(ответ 8):
a = '192.168.32.160'
m = '255.255.255.240'
c1 = 0
c = ''
for i in a.split('.'):
    a1 = bin(int(i))
    c+=str(a1)+'.'
c = c.rstrip('.')
c = c.replace('0b', '')
c2 = ''
for i in m.split('.'):
    a1 = bin(int(i))
    c2+=str(a1)+'.'
c2 = c2.rstrip('.')
c2 = c2.replace('0b', '')
print('IP:  ',c, len(c))
print('Mask:',c2, len(c2))
def pg(s):
    ip = 0
    for c in s.split('.'):
        ip = ip*256 + int(c)
    return ip
print('')
a1 = int(pg(a))
m1 = int(pg(m))
for i in range(16):
    if bin(a1).count('1')%2==0:
        print( a1)
        c1+=1
    a1 += 1
print(c1)'''
'''                                     делали вместе(ответ 7)
a = '192.168.32.160'
c = ''
for i in a.split('.'):
    a1 = bin(int(i))
    c+=str(a1)+'.'
c = c.rstrip('.')
c = c.replace('0b', '')
a2 = '255.255.255.240'
c2 = ''
for i in a2.split('.'):
    a1 = bin(int(i))
    c2+=str(a1)+'.'
c2 = c2.rstrip('.')
c2 = c2.replace('0b', '')
print('IP:  ',c, len(c))
print('Mask:',c2, len(c2))
ip = (192<<24) + (168<<16) + (32<<8) + 160
print(ip)
q = 0
temp_ip = ip
for i in range(16):
    temp_ip = temp_ip + 1
    if bin(temp_ip)[2:].count('1') %2 ==0:
        print('podhodit:', temp_ip)
        q = q+1
print(q)'''
'''                                                      задание №5 на 46 странице
from math import ceil
def pp(n):
    d1 = []
    for d in range(1,n+1):
        if n%d==0:
            d1.append(d)
    return sorted(d1)
st = ceil(100000000**0.5)
en = int(900000000**0.5)
for n in range(st, en+1):
    if len(pp(n))==4 and pp(n)[1]**2==pp(n)[2]:
        print(n**2, n**2//pp(n)[1])'''
'''                                                 задание №6 тоже 46 стр
a = '193.124.85.64'
m = '255.255.255.192'
c1 = 0
c = ''
for i in a.split('.'):
    a1 = bin(int(i))
    c+=str(a1)+'.'
c = c.rstrip('.')
c = c.replace('0b', '')
c2 = ''
for i in m.split('.'):
    a1 = bin(int(i))
    c2+=str(a1)+'.'
c2 = c2.rstrip('.')
c2 = c2.replace('0b', '')
print('IP:  ',c, len(c))
print('Mask:',c2, len(c2))
def pg(s):
    ip = 0
    for c in s.split('.'):
        ip = ip*256 + int(c)
    return ip
def jj(n):
    return bin(n).lstrip('0b')
print('')
a1 = bin(int(pg(a))).lstrip('0b')
for i in range(64):
    b = str(a1)
    if b.count('1')>b.count('0'):
        c1+=1
    print(a1, a1.count('1'), a1.count('0'))
    a1 = jj(int(a1, 2)+1)
print(c1)'''
'''                                                 функция, которая переводит в любую систему счисления:
def pe(n, n1):
    c = ''
    c1 = ''
    if n1 ==8:
        c = oct(n).lstrip('o0')
    elif n1==16:
        c = hex(n).lstrip('x0')
    elif n1 ==2:
        c = bin(n).lstrip('b0')
    elif n1==1:
        print('какая единичная система?')
    else:
        if n1<=n:
            while n!=0:
                c +=str(n%n1)
                n //=n1
        else:
            while n!=0:
                if n%n1 in [10, 11, 12, 13, 14, 15, 16]:
                    if n%n1==10:
                        c +='A'
                    if n%n1==11:
                        c +='B'
                    if n%n1==12:
                        c +='C'
                    if n%n1==13:
                        c +='D'
                    if n%n1==14:
                        c +='E'
                    if n%n1==15:
                        c +='F'
                    if n%n1==16:
                        c +='G'
                    n //=n1
                else:
                    c +=str(n%n1)
                    n //=n1
    return c1.join(reversed(c))'''
'''from math import ceil
def pp(n):
    d1 = []
    n = int(n)
    for d in range(1,n+1):
        if n%d==0:
            d1.append(d)
    return sorted(d1)
st = ceil(10000/11)
en = int(99999/11)
n = round(1234)
print(pp(n), len(pp(n)), n)
for n in range(st, en+1):
    if len(pp(n))==66:
        print(n**2, n)
print(pp(66), len(pp(66)))
print(pp(6), len(pp(6)))'''
'''                                         определяет, сколько раз числа меняли свой знак(+ или -)
a = 1
c, c1 = 0,0
while a!=0:
    a = int(input())
    while a>0:
        a = int(input())
        if a==0:
            break
        if a<0:
            c +=1
    while a<0:
        a = int(input())
        if a==0:
            break
        if a>0:
            c +=1
print(c)'''
'''                                     пишет, какой последовательностью является последовательность
f = int(input('кол-во чисел '))
c, c1 = 0, -1
b = 0
a = 0
for i in range(f):
    b = a
    a = int(input())
    if a>b:
        c += 1
    elif b>a:
        c1 -= 1
if c==f:
    print('возрастающая')
elif c1==-f:
    print('убывающая')
else:
    print('это не последовательность')'''
'''                                         находит второе максимальное число в последовательности
f = int(input('кол-во чисел '))
c = list()
for i in range(f):
    a = int(input())
    c.append(str(a))
c.remove(max(c))
print(max(c))'''
'''                                         находит максимальную сумму чисел в последовательности
f = int(input('кол-во чисел '))
c = list()
for i in range(f):
    a = int(input())
    c.append(str(a))
c1 = max(c)
c.remove(max(c))
print(int(c1)+int(max(c)))'''
'''
c = 0
i =0
from math import ceil
def pp(n):
    d1 = []
    for d in range(2,n):
        if n%d==0:
            d1.append(d)
    return sorted(d1)
while c<64:
    i +=1
    c +=i
    print(c, len(pp(c)))'''
'''                                                                 заменяет А на Б и Б на А
a = 'A0ABBABA41BA'
print(''.join([i.replace('A', 'B') if i=='A' else 'A' for i in a]))


def pe(b):
    c = ''
    for i in b:
        if i=='B':
            c+='A'
        elif i=='A':
            c+='B'
        else:
            c+=i
    return c
print(pe(a))'''
'''                                             если нужно заменить символы в строке
a = ''
a = a.replace('', '')
a = a.replace('', '')
print(a)'''
'''                                                 проверяет верность номера телефона
a = input('введите номер: ')
if (a[0]=='8' and len(a)==11 and a.isdigit()==True) or (a[:2]=='+7' and len(a)==12 and a[1:].isdigit()==True):
    print('номер верен')
else:
    print('номер неверен')'''
'''                                                 заменяет максимальное число на минимальное и наоборот
a = int(input('кол-во: '))
d = list()
for i in range(a):
    b = int(input())
    d.append(b)
c = d.index(max(d))
c1 = d.index(min(d))
d[c], d[c1] = d[c1], d[c]
print(d)'''
'''                                             вводится день, месяц и год и проверяется, кто старше
a = int(input())
a1 = int(input())
a2 = int(input())
b = int(input())
b1 = int(input())
b2 = int(input())
if a2<b2:
    print('первый старше')
elif b2==a2:
    if a1<b1:
        print('первый старше')
    elif a1==b1:
        if a<b:
            print('первый старше')
        else:
            print('второй старше')
    else:
        print('второй старше')
else:
    print('второй старше')'''
'''                                                             находит в строке максимальную сумму цифр в одну строчку
a a = '123 abc 65 abc 1000 hello 91'
print(max(filter(str.isdigit, a.split()), key=lambda x: sum(int(i) for i in x)))
'''
'''                                                             изменяет функцию, которая суммирует все аргументы на функцию, которая находит среднее арифмитическое
def ya(test):
    def gay(*args):
        return test(sum(args))/test(len(args))
    return gay
@ya
def get_sum(*args):
    return sum(args)
print(get_sum(1, 2, 3, 4, 5, 6, 7))'''
'''                                                             Напишите функцию trip_list(*args), которая получает произвольное число аргументов
строк — города посещенные во время путешествия в порядке их посещения. Города
могут повторяться. Функция должна возвращать список городов отсортированный по
алфавиту без повторений.

def ger(*args):
    return list(sorted(set(args)))
print(ger('Чебоксары', 'Москва', 'Чебоксары', 'Анапа'))'''
'''                                                             Напишите программу, которая сортирует список чисел по уменьшению количества
цифр, если количество цифр совпадает, по значению по возрастанию.
Отсортированные числа следует вывести на одной строке через пробел. Используй
функцию sorted() или метод sort() и анонимную функцию в качестве ключа сортировки.

def nepridum(args):
    return ' '.join(sorted(args, key=lambda x: (-len(x), int(x))))
a = '65 56 1 3 2 242 323 252'.split()
print(nepridum(a))'''
'''                                                            Напишите функции для регистрации и авторизации пользователя: registration(user,
password) и authorization(user, password).
Функция registration() добавляет пользователя и ничего не выводит. Если при
регистрации пользователя логин уже был зарегистрирован ранее, то это значит, что
для данного пользователя необходимо обновить пароль.
Функция authorization() выводит:
Python
Unset
● «Доступ разрешен», если пара пользователь пароль верная
● «Неверный пароль», если пароль не верный
● «Пользователь не найден», если нет такого пользователя.
def log(l, p):
    global d
    d = {l: p}
    pass
def avto(n, k):
    if d == {n: k}:
        print('вход разрешен')
    else:
        if d.keys() != {n: k}.keys():
            print('пользователь не найден')
        elif d.values() != {n: k}.values():
            print('неверный пароль')
log('vanya', '12345678')
avto('vanya', '12345678')
avto('vanya', '1234')
avto('vasya', '12345678')
log('dmitri', '368')
avto('dmitri', '368')'''

'''                                                                             Напишите программу, которая по номеру билета определяет, является ли билет
счастливым. Билет называется счастливым, если сумма цифр в его левой половине
равна сумме цифр в правой. Номер билета состоит из шести цифр.
Входные данные:
Вводится одно целое шестизначное число.
Выходные данные:
Выводится одна строка «Счастливый» или «Обычный».
Пример ввода:
123006
Пример вывода:
Счастливый
a = 123456
b = 234432
c = [i for i in str(a)]
def nomer(a):
    c = list(map(int, [i for i in str(a)]))
    if sum(c[:3])==sum(c[3:]):
        return True
    else:
        return False
print(nomer(b))'''

'''                                                                                 Напишите программу, которая будет сокращать дробь.
a = 10
b = 15
def nod(a, b):
    while a!=0 and b!=0:
        if a>b:
            a = a%b
        else:
            b = b%a
    return a+b
print(a//nod(a, b), b//nod(a,b), nod(a,b))'''

'''                                                                                     Напишите программу для вывода чисел от 1, 2, 3 и так далее лесенкой. На первой
ступени должно быть одно число, на второй – два числа, на третьей три числа и так
далее.
Входные данные:
Вводится одно целое число n.
Выходные данные:
Выводится n строк - на каждой строке числа без разделителей.
a = 5
d = list()
c = 1
for i in range(a):
    i+=1
    d.clear()
    while len(d)!=i:
        d.append(c)
        c+=1
    print(int(''.join(map(str, d))))'''

'''                                                                             Напишите программу, которая будет проверять валидность адреса электронной почты
и будет продолжать запрашивать адрес до тех пор, пока не будет введён валидный
адрес. Программа должна выводить:
● «Адрес электронной почты введен верно», если в строке есть символы «@» и
«.».
● «Отсутствует @», если нет соответствующего символа.
● «Отсутствует .», если нет соответствующего символа.
● «Отсутствует @ и .», если нет соответствующих символов.
def prov(a):
    if '@' not in a and '.' not in a:
        return 2
    elif '@' not in a:
        return 0
    elif '.' not in a:
        return 1
    else:
        return 3
b = str(input())
while prov(b)!=3:
    if prov(b)==0:
        print('нету @')
        b = str(input())
    if prov(b)==1:
        print('нету .')
        b = str(input())
    if prov(b)==2:
        print('нету @ и .')
        b = str(input())
print('адрес введен верно')
'''
'''                                                                 Напишите функцию filter_numbers(*args, type), получающую произвольное
число позиционных аргументов: целые числа и один именованный аргумент type,
который может быть равен значению 'odd' или 'even'. Если значение аргумента
type равно 'odd', то функция возвращает список нечетных чисел, если 'even' —
четных.

def filters(*args, **type):
    if type.get('type')=='even':
        return list(filter(lambda a: a%2==0, args))
    elif type.get('type')=='odd':
        return list(filter(lambda a: a%2!=0, args))
print(filters(1, 2, 3, 4, type='odd'))
'''
'''                                                                 Напишите программу, которая сортирует список чисел по уменьшению количества
цифр, если количество цифр совпадает, по значению по возрастанию.
Отсортированные числа следует вывести на одной строке через пробел

a = '65 56 1 3 2 242 323 252'
print(' '.join(sorted(a.split(), key=lambda x: (-len(x), x))))
'''
'''                                                             Напишите программу для вычисления степени числа с помощью рекурсии без
использования циклов.
Входные данные:
Вводится два целых числа через пробел — основание и степень.
Выходные данные:
Выводится одно целое число.
Пример ввода:
2 5
Пример вывода:
32

def stepa(ch, st):
    if st==0:
        return 1
    return ch * stepa(ch, st-1)
print(stepa(2, 5))
'''
'''                                                                     Напишите программу, в которой будет создан класс Time. Реализуйте в нем
следующие методы:
● __init__(h, m) — добавляет объекту атрибуты h и m (часы и минуты);
● __str__() — возвращает текстовое представление объекта в формате: h:m.
Определите методы арифметических операций:
● сложение self + other — возвращает новый объект класса Time;
Python
● вычитание self - other — возвращает новый объект класса Time. Если разность
будет отрицательной, то считать ее равной 0 (h и m равны 0);
● умножение на число self * n — возвращает новый объект класса Time

class time:
    def __init__(self, h, m):
        self.h = h
        self.m = m
    def __str__(self):
        return f'{self.h}:{self.m}'
    def __sub__(self, other):
        return divmod(self.h * 60 + self.m - other.h *60 - other.m, 60)
    def __add__(self, other):
        return divmod(self.h * 60 + self.m + other.h *60 + other.m, 60)
    def __mul__(self, other):
        return divmod((self.h * 60 + self.m) * other, 60)
a = time(2, 30)
b = time(3, 45)
print(a * 4)
'''
'''                                                                                     Напишите программу, в которой создайте класс Date. Реализуйте в классе следующие
методы:
● __init__(d, m, y) — добавляет объекту атрибуты d, m, y (день, месяц и год);
● __str__() — возвращает текстовое представление объекта в формате: d.m.y;
● методы сравнения.
Входные данные:
Вводится три строки — на первой и второй строке вводятся даты в формате d.m.y, на
третьей строке вводится одна из операций сравнения ==, !=, >, >=, <, <=.
Выходные данные:
Выводится True или False — результат сравнения объектов
from functools import total_ordering

@total_ordering
class date:
    def __init__(self, d, m, y):
        self.d = int(d)
        self.m = int(m)
        self.y = int(y)
    def __eq__(self, other):
        return (self.d, self.m, self.y)==(other.d, other.m, other.y)
    def __gt__(self, object):
        if self.y>object.y:
            return True
        elif self.y==object.y and self.m> object.m:
            return True
        elif self.m == object.m and self.d > object.d:
            return True
        else:
            return False

a = input().split('.')
b = input().split('.')
a = date(a[0], a[1], a[2])
b = date(b[0], b[1], b[2])
print(a < b)
'''
'''                                                                                         Напишите программу, в которой создайте класс Student. Реализуйте в классе
следующие методы:
● __init__(name, course) — добавляет объекту атрибуты name (строка) и course
(целое число от 5 до 11), status со значением 'student'.
● next_course() — увеличивает course на единицу, пока студент не закончит
обучение (11 класс — последний год обучения). Если после вызова метода
next_course, класс становится больше 11, то значение атрибута course
устанавливается на None, a status на строку 'graduate'.
● deduction() — изменяет значение атрибута course на None, a status на строку
'expelled'.
● get_info() — возвращает строку вида Student: {name} ({course}), status: {status},
например, Student: Иванов Иван Иванович (None), status: expelled.

class Student:
    def __init__(self, n, c):
        self.__c = c
        self.__n = n
        self.__status = 'student'

    def get_info(self):
        return f'{self.__n} ({self.__c}), статус: {self.__status}'

    def deduction(self):
        self.__c = None
        self.__status = 'expelled'
    def next_course(self):
        if self.__c<11:
            self.__c +=1
        else:
            self.__status = 'graduate'
            self.__c = None
student1 = Student('Михайлов Петр', 10)
print(student1.get_info())
student1.next_course()
student1.next_course()
print(student1.get_info())
student2 = Student('Васильев Сергей', 5)
print(student2.get_info())
student2.deduction()
print(student2.get_info())
'''
'''                                                             Напишите программу, в которой создайте класс Person (человек). Реализуйте в классе
следующие методы:
● __init__(name, age) — добавляет объекту атрибуты name (строка), age (целое
число);
● get_name() — возвращает строковое представление объекта в формате:
Человек: {name}, например Человек: Иванов Иван;
● get_age() — возвращает строку в формате Возраст: {age}, например Возраст:
15.
Создайте класс Student (ученик), выполнив наследование от Person. Переопределите
следующие методы:
● __init__(name, age, course) — добавляет объекту атрибуты, как у экземпляра
класса Person, и атрибут course (целое число);
● get_name() — возвращает строковое представление объекта в формате:
Ученик: {name} ({course} класс), например Ученик: Иванов Иван (7 класс).

class person:
    def __init__(self, n, a):
        self.n  = n
        self.a = a
    def get_name(self):
        return f'ученик: {self.n}'
    def get_age(self):
        return f'Возраст: {self.a}'
class student(person):
    def __init__(self, n, a, c):
        super().__init__(n, a)
        self.c = c
    def get_name(self):
        return f'ученик: {self.n} ({self.c} класс)'
b = student('Иван', 15, 7)
print(b.get_name())
print(b.get_age())
print(person('абвгд', 4).get_name())
'''
'''                                                                 Напишите программу, в которой создай класс Time. Реализуйте в классе следующие
методы:
● __init__(h, m) — добавляет объекту атрибуты h и m — часы и минуты;
● __str__() — возвращает текстовое представление объекта в формате: «h:m».
● методы сравнения.

from functools import total_ordering
@total_ordering
class dio:
    def __init__(self, h, m):
        self.h = h
        self.m = m
    def __str__(self):
        return f'{self.h}:{self.m}'
    def __eq__(self, other):
        return (self.h,self.m) == (other.h, other.m)
    def __lt__(self, other):
        return (self.h, self.m) < (other.h, other.m)
a = dio(1,0)
b = dio(0, 59)
print(a>b)
'''
'''                                                             Создайте класс Sequence (последовательность). Реализуйте в классе следующие
методы:
● __init__(lst) — принимает один аргумент lst — список элементов
последовательности;
● __str__() — который будет возвращать текстовое представление объекта в
формате: «Последовательность {элементы через запятую и пробел}».
● сложение self + other — возвращает новый объект Sequence, в которой сначала
находятся элементы первой последовательности, затем элементы второй
последовательности, если их не было в первой последовательности в том же
порядке. Например, операция Sequence([1, 1, 2, 4]) + Sequence([3, 4, 5, 1, 6])
должна возвращать Sequence([1, 1, 2, 4, 3, 5, 6]).

class posl:
    def __init__(self, lst):
        self.lst = lst
    def __str__(self):
        return f'последовательность'
    def __add__(self, other):
        return posl(self.lst + list(filter(lambda x: x not in self.lst, other)))
a = [1,1,2,4]
b = [3,4,5,1,6]
print(posl(a).__add__(b))
'''
'''                                                                                     Напишите программу, в которой создайте класс Product (товар). Реализуй в классе
следующие методы:
● __init__(name, price, amount) — добавляет объекту атрибуты name, price,
amount;
● sale() — продажа, уменьшает количество товара (amount), при этом количество
товара не может быть меньше 0. При продаже товара, у которого значение
количества равно 0, необходимо выводить сообщение «Нет в наличии».
● refund() — возврат товара, увеличивает количество товара (amount);
● get_info() — возвращает строку вида «Товар: {name}, цена: {price}, количество:
{amount}», например, «Товар: футболка, цена: 200, количество: 130».

class product:
    def __init__(self, n, p, a):
        self.n = n
        self.p = p
        self.a = a
    def sale(self):
        if self.a==0:
            print(f'нет в наличии')
        else:
            self.a -= 1
    def refund(self):
        self.a +=1
    def get_info(self):
        return f'Товар: {self.n}, цена: {self.p}, количество: {self.a}'
product = product('Телефон', 20000, 2)
product.sale()
product.sale()
product.sale()
product.refund()
print(product.get_info())
'''
'''                                                                             Создайте класс Password для хранения и проверки пароля. Инициализатор класса
принимает один параметр — строку с паролем — и выполняет проверку его
корректности. Правильный пароль должен иметь длину не менее восьми символов и
включать хотя бы один знак из набора ?,.!@#$%^&*()<>. Если пароль корректен, то он
сохраняется в атрибут password. В противном случае вызывается одно из собственных
исключений MinLengthPasswordError (не выполнено условие минимальной длины) или
NoSpecialCharactersError (нет символа из набора).
Python
Считайте с клавиатуры одну строку — пароль. Создайте с ним экземпляр класса, если
он корректный, и выведите на экран текст «Пароль: {password}», например, «Пароль:
12345678@. Если пароль некорректный, с помощью вызова исключений
MinLengthPasswordError или NoSpecialCharactersError выведите на экран текст
«Короткий пароль» или «Нет специального символа». Сначала проверяется условие
необходимой длины: если оба условия ложны, то выводится одно сообщение —
«Короткий пароль».
При написании кода программы используйте обработку исключений. Создайте
собственные исключения MinLengthPasswordError и NoSpecialCharactersError.

class lenerror(Exception):
    pass
class nospecerror(Exception):
    pass
class parol:
    def __init__(self, p):
        if len(p) < 8:
            raise lenerror('не менее 8 символов')
        if set(' ?,.!@#$%^&*()<>') & set(p)==set():
            raise nospecerror('должны быть спец символы')
        else:
            self.p = p
try:
    p = parol(input('пароль: '))
except lenerror as e:
    print(e)
except nospecerror as e:
    print(e)
else:
    print('parolb is ok')
'''
'''                                                                         Скачайте файл numbers.txt, который содержит произвольное количество строк. В
каждой из них есть целые числа, разделенные пробелом. Напишите программу, с
помощью которой найдите сумму всех введенных чисел.
Пример файла numbers.txt:
1 2 3
4 5
6
7 8
9
Python
Python
Python
Ответ:
45

c = 0
with open('abaldetb.txt', 'r') as f:
    for i in f:
        c += sum(map(int, i.split()))
print(c)
'''
'''                                                                 Дано некоторое число. Проверьте, что цифры этого числа расположены по возрастанию
a = '12345'
if sorted(a)==list(a) or sorted(a, key=lambda x: -int(x))==list(a):
    print('да')
else:
    print('нет')
'''
'''                                                                   Дан список:

[1, '', 2, 3, '', 5]
Удалите из списка все пустые строки.

a = [1, '', 2, 3, '', 5]
print(list(filter(lambda x: x!='', a)))
'''
'''
[
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]
Выведите в консоль все элементы этого списка

a = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]
for i in a:
    for g in i:
        print(g)
'''
'''                                                         Дано число. Получите список делителей этого числа.

a = 1234
b = list()
for i in range(1, a+1):
    if a%i==0:
        b.append(i)
print(b)
'''
'''                                             Найдите сумму элементов этого словаря
a = dct = {
	1: {
		1: 11,
		2: 12,
		3: 13,
	},
	2: {
		1: 21,
		2: 22,
		3: 23,
	},
	3: {
		1: 24,
		2: 25,
		3: 26,
	},
}
c = 0
for i in a.values():
    for g in i.values():
        c +=g
print(g)
'''
'''                                                 Создайте простейший в мире класс SimplePass. Затем создайте экземпляр класса и выведите на экран его тип.

class SimpleClass:
    pass
a = SimpleClass
print(type(a))
'''
'''                                                         Определите класс A, включающий:
- строку документирования класса ''Класс A'';
- метод set_a() для установки значения атрибута a;
- метод get_a() для получения значения этого атрибута.
 
Выведите на экран документацию класса. Затем создайте первый экземпляр класса и при помощи определенных методов установите и 
выведите значение его атрибута a. Далее создайте второй экземпляр класса, после чего также установите и выведите на экран значение атрибута 
a, но уже при помощи прямого доступа к атрибуту по точке.

class a:
    def __str__(self):
        return 'класс a'
    def set_a(self, a):
        self.a = a
    def get_a(self):
        return self.a
print(a.__dict__)
c = a()
c.set_a(5)
print(c.get_a())
b = a()
b.set_a(10)
print(a.get_a(b))
'''
'''                                                             Определите класс B, включающий:
- строку документирования класса ''Класс B'';
- конструктор, инициализирующий атрибут данных b создаваемых экземпляров;
- метод get_b() для получения значения этого атрибута.

class b:
    def __init__(self, b):
        self.b =b
    def get_b(self):
        return self.b
b = b(2)
print(b.get_b())
'''
'''                                                                 Определите класс C, наследующий классы A (задача 13.2) и B (задача 13.3) и включающий:
- строку документирования класса 'Класс C = A + B';
- конструктор, инициализирующий дополнительно атрибуты данных a и c создаваемых экземпляров;
- собственные методы set_b() и set_c() для установки значений соответствующих атрибутов;
- собственный метод get_c() для получения значения атрибута c.
 
Выведите на экран документацию класса. Затем создайте экземпляр класса obj, после чего при помощи соответствующих методов экземпляра выведите значения его атрибутов a, b и c.

class a:
    def __str__(self):
        return f'класс a{self.a})'
    def __init__(self, a):
        self.a = a
    def get_a(self):
        return f'A = {self.a}'

class b():
    def __init__(self, b, a):
        super().__init__(a)
        self.b =b
    def str(self):
        return f'класс b({self.b})'
    def get_b(self):
        return f'B = {self.b}'

class c(b, a):
    def __init__(self, a, b, c):
        super().__init__(a,b)
        self.c = c
    def __str__(self):
        return f'класс с({self.c}) = а({self.a}) + b({self.b})'
    def set_b(self, b):
        self.b = b
    def set_c(self,c):
        self.c = c
    def get_c(self):
        return f'C = {self.c}'
c1 = c(10, 15, 20)
print(c1.get_c())
print(c1.get_b())
print(c1.get_a())
c1.set_c(30)
print(c1.get_c())
c1.set_b(25)
print(c1.get_b())
print(c.__mro__)
'''
'''                                                                         Определите класс D, включающий:
- статический метод stat_print_dict, выводящий на экран словарь атрибутов переданного ему объекта класса;
- метод класса cls_print_dict, выводящий на экран словарь атрибутов своего класса.

class d:
    c = 0
    e = 1
    @staticmethod
    def stat_dict(**kwargs):
        return kwargs
    @classmethod
    def class_dict(cls):
        return {cls.c: cls.e}
print(d.class_dict(), d.stat_dict(a=23))
'''
'''                                                                     Определите класс E, наследующий класс D (задача 13.5) и включающий единственный 
атрибут данных класса e = 'Класс E'. Создайте экземпляр obj_1 класса D 
и, вызвав оба метода из этого экземпляра, выведите на экран словарь атрибутов класса. 
Затем создайте экземпляр obj_2 класса E и также, вызвав оба метода из этого экземпляра,
 выведите на экран словарь атрибутов этого класса. Объясните результаты.

class d:
    c = 0
    j = 'le le le'
    @staticmethod
    def stat_dict(**kwargs):
        return kwargs
    @classmethod
    def class_dict(cls):
        return {cls.c: cls.j}
class e(d):
    c = 100
    j = 'попа'
d1 = d()
e1 = e()
print(d1.class_dict(), d1.stat_dict(a=5))
print(e1.class_dict(), e1.stat_dict(a=5))
'''
'''                                                                                                 Определите класс F, наследующий класс A (задача 13.2), включающий:
- конструктор, обновляющий строку документации создаваемых экземпляров на 'Объект класса F';
- расширенный метод set_a() для установки значения атрибута a, который должен дополнительно выводить сообщение 'Атрибут a установлен!'.

class a:
    def __str__(self):
        return 'класс a'
    def set_a(self, a):
        self.a = a
    def get_a(self):
        return self.a
class f(a):
    def set_a(self, a):
        self.a = a
        print('атрибут а установлен')
    def __str__(self):
        return 'класс f'
f1 = f()
a1 = a()
a1.set_a(5)
f1.set_a(5)
'''
'''                                                                                         Определите класс PiNum, хранящий значение числа Пи и включающий:
- конструктор, инициализирующий текущую точность представления числа Пи создаваемым экземпляром (по умолчанию два знака после запятой);
- переопределяемый магический метод __str__, возвращающий строку с текущим значением числа Пи;
- управляемый атрибут max_pi, хранящий значение числа Пи с максимальной точностью в 13 знаков после запятой и недоступный для изменения или удаления;
- метод set_pi_prec, устанавливающий значение атрибута cur_pi экземпляра для хранения значения числа Пи с текущей точностью (по умолчанию два знака после запятой).
 
Используя созданный класс, создайте экземпляр числа Пи с точностью в три знака после запятой и выведите его 
строковое представление на экран. Измените точность представления числа до пяти знаков после запятой и выведите 
новое значение на экран. Также выведите значение числа Пи с максимальной точностью.

class PiNum:
    pi = 3.1415926535897
    cur = 2
    @classmethod
    def __str__(cls):
        return str(cls.pi)[:cls.cur]
    @classmethod
    def set_pi(cls, c):
        cls.cur = c+2
        print(f'установленно знаков после запятой: {c}')
    @classmethod
    def max_pi(cls):
        return cls.pi
p = PiNum()
p.set_pi(3)
print(p)
p.set_pi(5)
print(p)
print(PiNum.max_pi())
'''
'''                                                                             Определите класс Circle, представляющий окружность и включающий:
- статический метод, переводящий метры в сантиметры или наоборот;
- конструктор, инициализирующий радиус r экземпляра и атрибут pi для хранения числа Пи с точностью в три знака после запятой 
(для получения требуемого значения используйте класс PiNum из предыдущей задачи);
- методы экземпляров для получения длины и площади окружности с точностью в три знака после запятой.
 
Используя созданный класс, рассчитайте и выведите на экран длину и площадь окружности в сантиметрах, зная что ее радиус равен 2.57 метра.

class circle:
    def __init__(self, r):
        self.r = r
    def perevod(self):
        self.r *=100
    def get_long(self):
        a = 2* 3.141 *self.r
        if a!=int:
            return '%.3f' % a
        else:
            return a
    def get_square(self):
        a = 3.141*self.r**2
        if a!=int:
            return '%.3f' % a
        else:
            return a
r = circle(2.57)
r.perevod()
print(r.get_long(), r.get_square())
'''
'''                                                                     Определите суперкласс Сотрудник, включающий:
- конструктор, инициализирующий имя работника, его должность (по умолчанию None) и оклад (по умолчанию 0);
- метод экземпляра для повышения оклада на какую-то часть (например, на 0.3, то есть на 30%) с округлением результата до копеек;
- магический метод __str__ для перегрузки строкового представления объекта, который должен выводить данные о работнике в формате 'Атрибут: объект.атрибут' 
по одной записи на каждой строке.
Также определите подкласс Менеджер, наследующий суперкласс Сотрудник и переопределяющий метод повышения оклада таким образом, чтобы он еще больше повышал оклад

class sotr:
    def __init__(self, n, i, d):
        self.d = d
        self.n, self.i = n, i
    def __str__(self):
        return f'имя: {self.n}, должность: {self.i}, зарплата: {self.d}'
    def povys(self):
        a = self.d* 1.335
        if a!=int:
            self.d ='%.2f' % (self.d* 1.335)
        else:
            self.d = a
        print('запрлата повышена на 30%')
class mened(sotr):
    def povys(self):
        a = self.d * 1.335 * 1.25
        if a!=int:
            self.d = '%.2f' % a
        else:
            self.d = a
        print('зарплата повышена на 30% + надбавка за должность менеджера 25%')
ivan = sotr('Иван', 'Сотрудник', 1700)
print(ivan)
ivan.povys()
print(ivan)
print()
igor = mened('Игорь', 'Менеджер', 3000)
print(igor)
igor.povys()
print(igor)
'''
'''                                                                         Создайте абстрактный класс геометрической фигуры Shape с конструктором, 
принимающим длину стороны и высоту, проведенную к этой стороне. Определите в классе абстрактный метод area(), 
который будет использоваться подклассами для расчета площади соответствующих им геометрических фигур. Далее 
создайте классы Triangle и Rectangle, наследующие суперкласс Shape и реализующие его абстрактный метод под 
свои нужды. Продемонстрируйте использование созданных классов для нахождения площади треугольника и прямоугольника
 по известным значениям длины стороны и высоты, проведенной к этой стороне.
 
 class shape:
    def __init__(self, c, v):
        self.c = c
        self.v = v
    def area(self):
        return self.c*self.v
class rectangle(shape):
    def area(self):
        return self.v*2 * self.c
class triangle(shape):
    def area(self):
        return self.c * self.v /2
    
pryamoygolnik = rectangle(6, 1.5)
print(pryamoygolnik.area())
treygolnik = triangle(6, 3)
print(treygolnik.area())
 '''
'''                                                                     Определите класс Counter, реализующий десятичный счетчик, который может увеличивать или уменьшать свое значение на единицу в заданном диапазоне, включая границы диапазона. В классе должны быть предусмотрены следующие возможности:
- конструктор для инициализации счетчика значениями по умолчанию (стартовое значение, нижняя и верхняя границы диапазона),
- метод для его инициализации произвольными значениями,
- а также методы для увеличения и уменьшения текущего значения счетчика.
Все методы класса должны принимать только именованные параметры и проверять выход текущего значения счетчика за 
допустимый диапазон. Создайте экземпляр счетчика со значениями по умолчанию и выведите его начальные параметры. 
Далее проверьте его работу циклом в пределах диапазона, увеличивая и выводя на экран его текущее значение от 
минимально возможного до максимального. Затем переустановите счетчик, задав отрицательную нижнюю и положительную
 верхнюю границы, а также установив положительное стартовое значение для отсчета. Опять же, проверьте его работу 
 циклом, уменьшая и выводя на экран его текущее значение от стартового до минимально возможного. Задайте заведомо 
 большее количество итераций циклов в обоих случаях, обеспечив прерывание их работы при попытке выхода счетчика за 
 пределы диапазона.
 
 class deapathonError(Exception):
    pass
class counter:
    def __init__(self, ch, m, m1):
        self.ch = ch
        self.m = m
        self.m1 = m1
    def __str__(self):
        return str(self.ch)
    def plus(self):
        if self.ch<self.m1:
            self.ch += 1
        else:
            raise deapathonError('число достигло максимума')
    def minus(self):
        if self.ch>self.m:
            self.ch -=1
        else:
            raise deapathonError('число достигло минимума')

a = counter(10, 5, 20)
print(a)
while True:
    try:
        a.plus()
        print(a)
    except deapathonError as e:
        print(e)
        break

b = counter(3, -10, 4)
print(b)
while True:
    try:
        b.minus()
        print(b)
    except deapathonError as e:
        print(e)
        break
 '''
'''                                                             сделал простую таблицу с помощью пандаса
import pandas as pd

df = pd.DataFrame({'цвет': ['оранжевый', 'красный', 'синий'], 'номер': map(lambda x:x*x, [2,3,4])})
print(df)
'''
'''                                                                 делает таблицу с именами и изменяет ее если кому-то меньше 18

import pandas as pd

file = {'имя': ['Иван','Игорь','Мария'], 'возраст': [16, 30, 25], 'город': ['Москва', 'Омск', 'Казань']}
file['возраст'] = list(i if i>18 else 'несовершенолетний' for i in file['возраст'])
a = pd.DataFrame(file)
print(a)
'''