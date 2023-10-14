this_is_a_list = ['daniel', 'ruiz', 'color']
my_awesome_list = ['caroline', 'blue', 'new_name']
# 'append', 'clear', 'copy', 'count', 'extend',
# 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
print(type(this_is_a_list ))
print(dir(this_is_a_list))

this_is_a_list.append('tania')
print(this_is_a_list)
this_is_a_list.extend(this_is_a_list)
print(this_is_a_list)
print(this_is_a_list[0])# index starts at 0

print(this_is_a_list[-1])# index starts at 0
print(this_is_a_list[2:7])# indexing
print(list(range(20))) # this returns an Iterator casting
print('the number is ' + str(23))
print(int('34') + 45)