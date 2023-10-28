import pymel.core as pm
from random import random

def create_grid(cubes_per_side, distanceX=3,distanceZ=3, distanceY=3):
    index_name=0
    for each_x in range(cubes_per_side):
        for each_y in range(cubes_per_side):
            for each_z in range(cubes_per_side):
                index_name =index_name+1
                cube_transform, cube_creation = pm.polyCube(name=f'Cube{index_name}')
                pm.setAttr(f'{cube_transform}.translateX', distanceX *each_x)
                pm.setAttr(f'{cube_transform}.translateZ', distanceZ * each_z)
                pm.setAttr(f'{cube_transform}.translateY', distanceY * each_y)

create_grid(6)
