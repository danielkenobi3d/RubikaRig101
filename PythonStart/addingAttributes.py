import pymel.core as pm
def add_custom_attr():
    selection = pm.ls(selection=True)[0]
    pm.addAttr(selection, longName='heightMultiplier', type='float', min=0, keyable=True)
    pm.addAttr(selection, longName='cubeSelection', type='enum',
               enumName=['cubosA', 'cubosB', 'cubosC', 'cubosD'],
               keyable=True)
    pm.addAttr(selection, longName='variaciones', type='long', min=0, dv=0, k=True)


def connecting_attributes():
    distance_between = pm.createNode('distanceBetween')
    circle_a = pm.ls('nurbsCircle2')[0]
    circle_b = pm.ls('nurbsCircle1')[0]
    creation_cube = pm.ls('polyCube4')[0]
    print(pm.ls('polyCube4'))
    print(pm.ls('polyCube4')[0])
    pm.connectAttr(circle_a.translate, distance_between.point1)
    pm.connectAttr(circle_b.translate, distance_between.point2)

    distance_between.distance >> creation_cube.height
    # pm.connectAttr(distance_between.distance, creation_cube.height)

if __name__ == '__main__':
    connecting_attributes()





