import pymel.core as pm


def cube_in_locators(locator_a, locator_b):
    locator_a, locator_b = pm.ls(locator_a, locator_b)
    cube_transform, cube_creator = pm.polyCube(name='cuboA')
    cone_transform, cone_creator = pm.polyCone(name='up_vector_coneA')
    print(cone_transform, cone_creator)
    pm.pointConstraint(locator_a, cube_transform)
    pm.pointConstraint(locator_b, cube_transform)

    pm.aimConstraint(locator_a, cube_transform,
                     aimVector=[0, 1, 0],
                     upVector=[1, 0, 0],
                     worldUpObject=cone_transform,
                     worldUpType='object'
                     )
    distance_node=pm.createNode('distanceBetween')
    locator_a.worldPosition[0] >> distance_node.point1
    locator_b.worldPosition[0] >> distance_node.point2
    distance_node.distance >> cube_creator.height

cube_in_locators('locator1', 'locator2')






