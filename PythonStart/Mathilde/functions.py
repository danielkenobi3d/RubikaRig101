def operate_in_two_values(*values, **kwargs):
    operation = kwargs.pop('operation', 'addition')

    print(f'the functio is getting {values}')
    if operation == 'addition':
        result = 0
        for each in values:
            # result = result +  each
            result += each
    elif operation == 'substraction':
        result = 0
        for each in values:
            # result = result +  each
            result -= each
    elif operation == 'multiply':
        result = 1
        for each in values:
            # result = result +  each
            result *= each
    return result


list_of_numbers = list(range(91))
list_of_numbers =[4,9,13,20,45]
my_keword_arg = {
    'operation': 'addition'
}

print(f"adding 4, 9, 13,20,45 = {operate_in_two_values(4,9,13,20,45)}" )
print(f"adding 4, 9, 13,20,45 = {operate_in_two_values(*list_of_numbers, **my_keword_arg)}")
