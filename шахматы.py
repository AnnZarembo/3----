ok = False
while ok==False:
    k = int(input('Введите номер вертикали для первой фигуры:'))
    l = int(input('Введите номер горизонтали для первой фигуры:'))
    m = int(input('Введите номер вертикали для второй фигуры:'))
    n = int(input('Введите номер горизонтали для второй фигуры:'))
    if (max(k,l,m,n)>8) or (min(k,l,m,n)<1):
        print('Можно вводить только числа от 1 до 8 ')
    else:
        ok=True

figure = input('Введите название первой фигуры(ферзь, ладья, конь, слон):')
zvet1 = k + l
zvet2 = m + n
if (zvet1//2)==(zvet2//2):
    print('Поля одного цвета')
else:
    print('Поля разных цветов')

def ygroza(k, l, m, n, figure):
    if figure=="ферзь":
        if k==m or l==n or abs(k-m) == abs(l-n):
            return True
    elif figure=="ладья":
        if k==m or l==n:
            return True
    elif figure=="конь":
        if abs(k-m)==2 and abs(l-n)==1:
            return True
        elif abs(k-m)==1 and abs(l-n)==2:
            return True
    elif figure=="слон":
        if abs(k-m) == abs(l-n):
            return True
    return False

def ygroza2(k,l,m,n,figure):
    for i in range(1,9):
        for j in range(1,9):
            if ygroza(k,l,i,j,figure) and ygroza(i,j,m,n,figure):
                return (i,j)
            else:
                return False
if ygroza(k,l,m,n,figure):
    print("Фигура угрожает полю")
else:
    print("Фигура не угрожает полю")

if ygroza2(k,l,m,n,figure):
    result = ygroza2(k,l,m,n,figure)
    if len(result)>1:
        print("Можно попасть на поле за два хода, первый ход в поле ({}, {})".format(result[0], result[1]))
    else:
        print("Нельзя попасть на поле за два хода")
else:
    print("Нельзя попасть на поле за два хода")