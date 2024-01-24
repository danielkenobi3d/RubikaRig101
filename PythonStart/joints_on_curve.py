import pymel.core as pm


def spline_joints(number_of_joints, curve=None):
    joint_list = []
    pm.select(clear=True)
    for index in range(number_of_joints):
        new_joint = pm.joint(position=[1 * index, 0, 0])
        joint_list.append(new_joint)
    if not curve:
        ik_handle, effector, curve = pm.ikHandle(startJoint=joint_list[0],
                                                 endEffector=joint_list[-1],
                                                 createCurve=True,
                                                 solver='ikSplineSolver')
    else:
        curve = pm.ls(curve)[0]
        ik_handle, effector = pm.ikHandle(startJoint=joint_list[0],
                                          endEffector=joint_list[-1],
                                          curve=curve,
                                          createCurve=False,
                                          solver='ikSplineSolver')

    curve_info = pm.createNode('curveInfo')
    multiply_divide = pm.createNode('multiplyDivide')
    multiply_divide.operation.set(2)
    curve.worldSpace[0] >> curve_info.inputCurve
    curve_info.arcLength >> multiply_divide.input1X
    multiply_divide.input2X.set(number_of_joints - 1)
    for each_joint in joint_list[1:]:
        multiply_divide.outputX >> each_joint.translateX

    up_vector_start = pm.spaceLocator(name='up_vector_start')
    pm.matchTransform(up_vector_start, joint_list[0])
    pm.move(up_vector_start, 3, moveY=True, objectSpace=True, relative=True)

    up_vector_end = pm.spaceLocator(name='up_vector_end')
    pm.matchTransform(up_vector_end, joint_list[-1])
    pm.move(up_vector_end, 3, moveY=True, objectSpace=True, relative=True)

    ik_handle.dTwistControlEnable.set(1)
    ik_handle.dWorldUpType.set(2)
    up_vector_start.worldMatrix[0] >> ik_handle.dWorldUpMatrix
    up_vector_end.worldMatrix[0] >> ik_handle.dWorldUpMatrixEnd


spline_joints(50)


