def f(x):
    return x.isupper() or x.islower()


print('Прошу, введите коэффициенты квадратичного уравнения на следующей строке:')
a, b, c = map(str, input().split())
if not f(a) and not f(b) and not f(c):
    a, b, c = float(a), float(b), float(c)
    D = b**2 - 4 * a * c
    if D < 0:
        print('Корней во множетсве R отсутвует')
    else:
        x_one = (-b + D**0.5)/(2*a)
        x_two = (-b - D**0.5)/(2*a)
        if x_one == int(x_one):
            x_one = int(x_one)
        if x_two == int(x_two):
            x_two = int(x_two)
        print(f'''Корни: {x_one}, {x_two}''')
else:
    print('Введены некорректные данные')
