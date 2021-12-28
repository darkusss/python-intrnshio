import csv
import json


def f1(x):
    return x / (x + 100.0)


def f2(x):
    if x != 0:
        return 1.0 / x
    else:
        raise ArithmeticError('Zero division')


def f3(x):
    if x != 0:
        return 20 * (f1(x) + f2(x)) / x
    else:
        raise ArithmeticError('Zero division')


def generate_x_values():
    for x in range(5, 91):
        f1x = f1(x)
        f2x = f2(x)
        f3x = f3(x)
        print('f1(' + str(x) + '): ' + str(f1x))
        print('f2(' + str(x) + '): ' + str(f2x))
        print('f3(' + str(x) + '): ' + str(f3x))
        yield [f1x, f2x, f3x]


x_values = {}
x_index = 5
for x_value in generate_x_values():
    x_values[x_index] = x_value
    x_index += 1

print(x_values)

with open('task2.csv', 'w') as file:
    csv_writer = csv.writer(file)

    csv_writer.writerow(['x', 'f1(x)', 'f2(x)', 'f3(x)'])
    for x in x_values:
        csv_writer.writerow([x] + x_values[x])

x_list = []
with open('task2.csv', 'r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        x_list.append([row['x'], row['f1(x)'], row['f2(x)'], row['f3(x)']])

print(x_list)

with open('task2.json', 'w') as file:
    json.dump(x_list, file)
