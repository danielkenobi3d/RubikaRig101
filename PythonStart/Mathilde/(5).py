import pymel.core as pm
if not pm.objExists('myCube'):
    plane_transform, creation_plane = pm.polyPlane(name='myCube')
else :
    plane_transform = pm.ls('myCube')[0]

print(plane_transform)
print(type(plane_transform))
print(dir(plane_transform))
plane_transform.translateX.set(12)
plane_transform.translateX.get()

#pm.setAttr('{}.translateX'.format(plane_transform),8)
#pm.getAttr('{}.translateX'.format(plane_transform))
