a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))
if a + b == c:
    print('Сумма a и b равна c: ', a + b)
else:
    print('Сумма a и b не равна c: ', a + b)
if a % b == c:
    print('При делении a на b c является их остатком: ', a % b)
else:
    print('При делении a на b c не является их остатком: ', a % b)
if a * c + b == 0:
    print('c является решением линейного уравнения ax + b = 0: ', c)
else:
    print('c не является решением линейного уравнения ax + b = 0: ', c)
