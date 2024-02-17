my_dictionary = {1: ['Daniel', 'Chiquin'],
                 2: {'Qian':{'age': 23,
                             'last_name':'Xiong',
                             'height': 160},
                     'Raphael':{'age':25,
                                'last_name':'vandewalle',
                                'height':180}
                                },
                 3:'Mathilde'}
print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary[1])
print(my_dictionary[2]['Qian']['age'])
print(my_dictionary[2]['Qian'].keys())
for each_name in my_dictionary[2].keys():
    print('{} info'.format(each_name))
    # print(f'{each_name} info')
    for each in my_dictionary[2][each_name].keys():
        print( f"{each}= {my_dictionary[2][each_name][each]}")

