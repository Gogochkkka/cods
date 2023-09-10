print('Прошу, введите коэффициенты квадратичного уравнения:')
a, b, c = map(int, input().split())
D = b**2 - 4 * a * c
if D < 0:
    print('Корней во множетсве R отсутвуют')
else:
    x_one = (-b + D**0.5)/(2*a)
    x_two = (-b - D**0.5)/(2*a)
    if x_one == int(x_one):
        x_one = int(x_one)
    if x_two == int(x_two):
        x_two = int(x_two)
    print(f'''Корни: {x_one}, {x_two}''')
