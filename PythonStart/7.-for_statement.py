import random

for each_element in ['daniel', 'ruiz', 'randi']:
    print(each_element)

for each_function in dir([]):
    print(each_function)

for each in 'maya':
    print(each)

for each in range(20):
    print(each)

names = ['daniel', 'juan', 'randi', 'pedro']
ages = [40, 23, 34, 45]


for name, age in zip(names, ages):
    print(f'{name} tiene {age} de edad')

for index, name in enumerate(names):
    print(f'{index}.{name}')

def give_random_element(element_list):
    index = int(random.random() * (float(len(element_list) - 0.0001)))
    return element_list.pop(index)

for name in names:
    print(f'{name} tiene edad de {give_random_element(ages)}')



