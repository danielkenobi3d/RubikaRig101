import pymel.core as pm

plane_transform, creation_plane = pm.polyPlane(name='myCube')
print(plane_transform)
print(creation_plane)
cmds.setAttr('{}.translateX'.format(plane_transform),20)
