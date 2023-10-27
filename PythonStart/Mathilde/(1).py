import maya.cmds as cmds
if not cmds.objExists('myCube'):
    plane_transform, creation_plane = cmds.polyPlane(name='myCube')
else :
    plane_transform = cmds.ls('myCube')[0]

cmds.setAttr('{}.translateX'.format(plane_transform),8)

#print(plane_transform)
#print(creation_plane)
