import matplotlib.pyplot as plt

file = open("../data/full_flight.csv")

parameters = file.readline().rstrip("\n").split(",")
parameters_count = len(parameters)
data = {parameter: [] for parameter in parameters}

parameters_rus = [ ("Время", 0), 
        ("Вертикальная скорость", 4),
        ("Орбитальная скорость", 5),
        ("Масса", 6),
        ("Ускорение", 7),
        ("Удельная теплоемкость", 8),
        ("Высота", 12),
        ("Гравитационные потери", 14),
        ("Потери сопротивления", 15),
        ("Потери управления", 16),
        ("Delta-V", 17) ]

for line in file:
    values = line.rstrip("\n").split(",")
    for i in range(parameters_count):
        data[parameters[i]].append(float(values[i]))
file.close()

print(f'ВЫБЕРИТЕ 2 ПАРАМЕТРА ИЗ ПРИВЕДЕННЫХ НИЖЕ, ЧТОБЫ ПОСТРОИТЬ ГРАФИК:\n')

parameters_rus_count = len(parameters_rus)
for i in range(parameters_rus_count):
    print(f'{i + 1}) {parameters_rus[i][0]}')
print()

parameter2 = int(input("ВВЕДИТЕ ПОРЯДКОВЫЙ НОМЕР ЗАВИСИМОГО ПАРАМЕТР: ")) - 1
parameter1 = int(input("ВВЕДИТЕ ПОРЯДКОВЫЙ НОМЕР НЕЗАВИСИМОГО ПАРАМЕТР: ")) - 1
if (parameter1 <= -1) or (parameter1 >= parameters_rus_count) or \
    (parameter2 <= -1) or (parameter2 >= parameters_rus_count):
    raise ValueError("Incorrect parameters has been entered")

values1 = data[parameters[parameters_rus[parameter1][1]]]
values2 = data[parameters[parameters_rus[parameter2][1]]]

plt.plot(values1, values2)

plt.title(f'Название графика')
plt.xlabel(parameters_rus[parameter1][0])
plt.ylabel(parameters_rus[parameter2][0])

plt.savefig('../../pictures/KSP_Graphic.png')