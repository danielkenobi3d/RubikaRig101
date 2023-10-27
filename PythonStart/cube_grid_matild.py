import pymel.core as pm
from random import random

def create_grid(nb_cubes, distanceX, distanceZ):
    index_name = 0
    index_x = 0
    for each_x in range(nb_cubes):
        index_z = 0
        index_name = index_name + 1
        index_x = index_x + 1
        for each_z in range(nb_cubes):
            cube_transform, cube_creation = pm.polyCube(name=f'Cube{index_name}')
            cube_attrX = pm.setAttr(f'{cube_transform}.translateX', distanceX * index_x)

            index_z = index_z + 1
            cube_attrZ = pm.setAttr(f'{cube_transform}.translateZ', distanceZ * index_z)

nb_cubes = int(random() * 20)
distanceX = 3
distanceZ = 3
create_grid(int(random() * 20), 3, 3)



