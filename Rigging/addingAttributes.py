import pymel.core as pm
pm.addAttr('nurbsCircle1', ln='rig_scale',
           k=True, attributeType='float', min=0)
pm.addAttr('nurbsCircle1', ln='enable_someting',
           k=True, attributeType='bool')


pm.addAttr('nurbsCircle1', ln='color',
           k=True, attributeType='enum',
           enumName=['green', 'blue', 'yellow','red'])