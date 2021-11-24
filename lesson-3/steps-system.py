position_x = 0
position_y = 0

print('''
a - шаг влево
d - шаг вправо
w - шаг вверх
s - шаг вниз
''')
step = input("Выберите цифру шага: ")
if step == 'a':
    position_x -= 1
    print(f"Позиция игрока: x={position_x},y={position_y}")
elif step == 'd':
    position_x += 1
    print(f"Позиция игрока: x={position_x},y={position_y}")
elif step == 'w':
    position_y += 1
    print(f"Позиция игрока: x={position_x},y={position_y}")
elif step == 's':
    position_y -= 1
    print(f"Позиция игрока: x={position_x},y={position_y}")
else:
    print("Нет такой команды!")