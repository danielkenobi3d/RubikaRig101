import pymel.core as pm

blendshape = pm.blendShape('character')[0]
pm.blendShape(blendshape, edit=True, target=['character',0, 'muscle',  1.0])
pm.blendShape(blendshape, edit=True, target=['character',1, 'correctivoCodo',  1.0])

import RMPY.core.rig_core as rm
blend_shape = rm.BlendShape.by_node('character')
blend_shape.add_as_target('muscle', 'correctivoCodo')

import pymel.core as pm
import maya.cmds as cmds
joint2=pm.ls('joint2')[0]
blend_shape = pm.blendShape('character', frontOfChain =True)[0]
pm.reorderDeformers("skinCluster1" ,blend_shape, "character")
pm.blendShape(blend_shape, edit=True, target=['character',0, 'muscle',  1.0])
pm.blendShape(blend_shape, edit=True, target=['character',1, 'correctivoCodo',  1.0])

pm.setDrivenKeyframe(f'{blend_shape}.muscle', currentDriver = joint2.rotateZ, dv=0, v=0)
pm.setDrivenKeyframe(blend_shape.muscle, currentDriver = 'joint2.rotateZ', dv=100, v=1)
pm.setDrivenKeyframe(blend_shape.correctivoCodo, currentDriver = 'joint2.rotateZ', dv=0, v=0)
pm.setDrivenKeyframe(blend_shape.correctivoCodo, currentDriver = 'joint2.rotateZ',  dv=100, v=1)


import RMPY.core.rig_core as rm
blend_shape = rm.BlendShape.by_node('character')
blend_shape.add_as_target('muscle', 'correctivoCodo')
rm.connect.with_limits('joint2.rotateZ', blend_shape.node.muscle, [[0, 0],[100, 1]])
rm.connect.with_limits('joint2.rotateZ', blend_shape.node.correctivoCodo, [[0, 0],[100, 1]])



