import random
import pymel.core as pm


def create_stairs(n_steps, max_height=5, min_height=1, offset_x=0, offset_z=0):
    for each_z in range(n_steps):
        for each_x in range(n_steps-each_z):
            transform, creation_node = pm.polyCube()
            creation_node.width.set(1)
            pm.setAttr(f'{creation_node}.height', 2)
            creation_node.height.set(min_height + random.random() * (max_height - min_height))
            transform.translateX.set(each_x + offset_x)
            transform.translateZ.set(each_z + offset_z)

create_stairs(5)

def create_stairs(n_steps, max_height=5, min_height=1, offset_x=0, offset_z=7):
    for each_z in range(n_steps):
        for each_x in range(each_z+1):
            transform, creation_node = pm.polyCube()
            creation_node.width.set(1)
            pm.setAttr(f'{creation_node}.height', 2)
            creation_node.height.set(min_height + random.random() * (max_height - min_height))
            transform.translateX.set(each_x + offset_x)
            transform.translateZ.set(each_z + offset_z)

create_stairs(5)

def create_stairs(n_steps, max_height=5, min_height=1, offset_x=10, offset_z=11):
    for each_z in range(n_steps):
        for each_x in range(n_steps-each_z):
            transform, creation_node = pm.polyCube()
            creation_node.width.set(1)
            pm.setAttr(f'{creation_node}.height', 2)
            creation_node.height.set(min_height + random.random() * (max_height - min_height))
            transform.translateX.set(offset_x - each_x)
            transform.translateZ.set(offset_z - each_z)

create_stairs(5)

def create_stairs(n_steps, max_height=5, min_height=1, offset_x=10, offset_z=4):
    for each_z in range(n_steps):
        for each_x in range(each_z+1):
            transform, creation_node = pm.polyCube()
            creation_node.width.set(1)
            pm.setAttr(f'{creation_node}.height', 2)
            creation_node.height.set(min_height + random.random() * (max_height - min_height))
            transform.translateX.set(offset_x - each_x)
            transform.translateZ.set(offset_z - each_z)

create_stairs(5)
