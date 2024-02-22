import pymel.core as pm


def create_equidistant_jnt(number_of_joints):
    pm.select(clear=True)
    list_of_joints = []
    for each_index in range(number_of_joints):
        new_joint = pm.joint()
        new_joint.translateX.set(1)
        list_of_joints.append(new_joint)
    pm.select(clear=True)
    return list_of_joints


def create_curve_based_on_locators(locators_list):
    list_of_points = []
    for each_point in locators_list:
        list_of_points.append(each_point.translate.get())
    new_curve = pm.curve(point=list_of_points)

    for index, each_point in enumerate(locators_list):
        # pm.connectAttr(each_point.worldPosition[0],new_curve.controlPoints[index])
        each_point.worldPosition[0] >> new_curve.controlPoints[index]
    return new_curve


def creates_joints_on_curve(curve, number_of_joints):
    list_joints = create_equidistant_jnt(number_of_joints)
    pm.ikHandle(startJoint = list_joints[0],
                endEffector = list_joints[-1],
                solver='ikSplineSolver',
                createCurve=False, curve=curve)

# selection = pm.ls(selection=True)
# curve = create_curve_based_on_locators(selection)
# creates_joints_on_curve(curve, 20)
# create_equidistant_jnt(5)
selection = pm.ls(selection=True)
create_curve_based_on_locators(selection)

