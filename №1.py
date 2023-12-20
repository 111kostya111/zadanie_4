import math

try:
    ugol = float(input("Введите величину угла: "))
except ValueError:
    print("Введено неккорктное значение")
    exit()

vibor = input("Введите единицу изверения (rad или deg): ")

if vibor == "rad":
    pass
elif vibor == "deg":
    ugol = math.radians(ugol)
else:
    print("Введено неккоректное значение")
    exit()

sinx = round(math.sin(ugol), 2)
cosx = round(math.cos(ugol), 2)
print("sinx = ", sinx)
print("cosx = ", cosx)

if math.degrees(ugol) % 90 == 0 and math.degrees(ugol) % 180 != 0:
    print("ERROR")
    exit()

tanx = round(math.tan(ugol), 2)
print("tanx = ", tanx)
