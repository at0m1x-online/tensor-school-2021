print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
discr = b ** 2 - 4 * a * c
print(f"Дискриминант = {discr}")
if discr == 0:
    x = -b / (2 * a)
    print(f'x = {x}')
else:
    x1 = (-b + discr ** 0.5) / (2 * a)
    x2 = (-b - discr ** 0.5) / (2 * a)
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
