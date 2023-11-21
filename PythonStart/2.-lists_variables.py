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


name_token = ["C","arm","rig","JNT"]
nombre='Randi'
edad=23
tio='daniel'

print("_".join(name_token))
print("el nombe es {} que tiene de edad {} y su tio es {}".format(nombre, edad, tio))
print(f"el nombe es {nombre} que tiene de edad {edad} y su tio es {tio}")

