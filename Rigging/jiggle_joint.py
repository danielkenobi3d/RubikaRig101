import pymel.core as pm


def create_jiggle_joint():
    circle_translate, circle_creator = pm.circle()
    locatorA = pm.spaceLocator()
    locatorB = pm.spaceLocator()
    locatorA.translateY.set(2)
    locatorB.translateY.set(-2)
    muscle_spline = pm.createNode('cMuscleSpline')
    locatorB.worldMatrix[0] >> muscle_spline.controlData[0].insertMatrix
    circle_translate.worldMatrix[0] >> muscle_spline.controlData[1].insertMatrix
    locatorA.worldMatrix[0] >> muscle_spline.controlData[2].insertMatrix
    time_node = pm.ls(type='time')[0]
    time_node.outTime >> muscle_spline.inTime
    output_joint = pm.joint(name='output')
    muscle_spline.outputData[0].outTranslate >> output_joint.translate
    muscle_spline.outputData[0].outRotate >> output_joint.rotate
    pm.addAttr(output_joint, longName='uValue', k=True)
    output_joint.uValue.set(0.5)
    output_joint.uValue >> muscle_spline.readData[0].readU
    output_joint.rotateOrder >> muscle_spline.readData[0].readRotOrder

    for each_attribute in ['tangentLength', 'jiggle', 'cycle', 'rest', 'jiggleX', 'jiggleY', 'jiggleZ',
                           'jiggleImpact', 'jiggleImpactStart', 'jiggleImpactStop']:
        pm.addAttr(circle_translate, ln=each_attribute, k=True)
        circle_translate.attr(each_attribute).set(muscle_spline.controlData[1].attr(each_attribute).get())
        circle_translate.attr(each_attribute) >> muscle_spline.controlData[1].attr(each_attribute)


create_jiggle_joint()