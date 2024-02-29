import pymel.core as pm

def create_controls(point):
    transform, creator = pm.circle(normal=[1, 0, 0])
    pm.matchTransform(transform, point)
    reset_group = pm.group(empty=True)
    pm.matchTransform(reset_group, point)
    transform.setParent(reset_group)
    # in commands it would be like this
    # pm.parent(transform, reset_group)
    return reset_group, transform

reset_A, transform_A = create_controls('locator1')
reset_B, transform_B =create_controls('locator2')
reset_C, transform_C =create_controls('locator3')

reset_B.setParent(transform_A)
reset_C.setParent(transform_B)
