import pymel.core as pm


def create_stairs(n_steps):
    for each in range(n_steps):
        transform, creation_node = pm.polyCube()
        creation_node.width.set(10)
        transform.translateY.set(each)
        transform.translateZ.set(each)


create_stairs(20)
