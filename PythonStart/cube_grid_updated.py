import pymel.core as pm
from random import random
from random import randrange


def create_grid(cubes_per_side, distanceX=3, distanceZ=3):
    index_name = 0
    for each_x in range(cubes_per_side):
        index_name = index_name + 1
        for each_z in range(cubes_per_side):
            cube_transform, cube_creation = pm.polyCube(name=f'Cube{index_name}')
            pm.setAttr(f'{cube_transform}.translateX', distanceX * each_x)
            pm.setAttr(f'{cube_transform}.translateZ', distanceZ * each_z)
            random() * 10# A number between 0 and 10
            random_number = random()*10+5     # A number between 30 and 70
            # pymel object oriented
            cube_creation.height.set(random_number)
            # pymel as in commands
            # pm.setAttr(f'{cube_creation}.height', random()*10+5)


create_grid(int(random() * 20))



