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
    pm.ikHandle(startJoint=list_joints[0],
                endEffector=list_joints[-1],
                solver='ikSplineSolver',
                createCurve=False, curve=curve)
    return list_joints

def make_stretchy_spline_ik(curve, list_of_joints):
    curve_info_node = pm.createNode('curveInfo')
    divide_node = pm.createNode('multiplyDivide')
    curve.worldSpace[0] >> curve_info_node.inputCurve
    curve_info_node.arcLength >> divide_node.input1X
    divide_node.input2X.set(len(list_of_joints)-1)
    divide_node.operation.set(2)
    for each_joint in list_of_joints[1:]:
        divide_node.outputX >> each_joint.translateX


if __name__ == '__main__':
    selection = pm.ls(selection=True)
    curve = create_curve_based_on_locators(selection)
    new_joints = creates_joints_on_curve(curve, 20)
    make_stretchy_spline_ik(curve, new_joints)



