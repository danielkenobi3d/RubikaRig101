import maya.cmds as cmds
my_cubes=pm.ls('pCubes*', type='transform')
for index in range(len(my_cubes)):
    cmds.setAttr(f'{my_cubes[index]}.translateX',index)
    cmds.setAttr(f'{my_cubes[index]}.translateY',index)
