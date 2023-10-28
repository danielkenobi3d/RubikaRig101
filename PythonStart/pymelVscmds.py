import maya.cmds as cmds

transform, creation_node = cmds.polyCube()
cmds.setAttr(f'{transform}.translateX', 10)
cmds.rename(transform, 'my_cmds_group')
cmds.setAttr(f'{transform}.translateX', 30)

import pymel.core as pm
transform_pm, creation_node_pm = pm.polyCube()
transform_pm.translateX.set(10)
transform.rename('my_pymel_group')
transform_pm.translateX.set(30)


# pm.rename(transform, 'my_cmds_group')

