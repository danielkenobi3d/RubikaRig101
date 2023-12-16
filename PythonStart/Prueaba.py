import random
import pymel.core as pm


def create_triangle(n_steps, type='A', max_height=5, min_height=1, offset_x=0, offset_z=0):
    for each_z in range(n_steps):
        if type in 'AC':
            x_range = n_steps-each_z
        else:
            x_range = each_z+1
        for each_x in range(x_range):
            transform, creation_node = pm.polyCube()
            creation_node.width.set(1)
            pm.setAttr(f'{creation_node}.height', 2)
            creation_node.height.set(min_height + random.random() * (max_height - min_height))
            if type in 'AB':
                final_offset = each_x
            else:
                final_offset = (n_steps - each_x)
            transform.translateX.set(offset_x + final_offset)
            transform.translateZ.set(each_z + offset_z)
size = 5
for each_z_square in range(10):
    for each_x_square in range(10):
        create_triangle(size, type='ABCD'[int(random.random()*4)],
                        offset_x=size * each_x_square,
                        offset_z=size * each_z_square)

