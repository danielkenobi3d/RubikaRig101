import pymel.core as pm
tCube, creation_node = pm.polyCube()
tCircle, create_circle = pm.circle()
script = f'{creation_node}.height = abs({tCircle}.translateY);\n'
script +=f'{tCube}.translateY = {tCircle}.translateY / 2;\n'
pm.expression(string=script, name='cube_height')


import pymel.core as pm
transform_cylinder, creation_cylinder = pm.polyCylinder()
transform_cylinder.rotateX.set(90)
space_loc = pm.spaceLocator()
transform_cylinder.setParent(space_loc)
script = f'{transform_cylinder}.rotateZ = -rad_to_deg({space_loc}.translateX/{creation_cylinder}.radius);'
pm.expression(string=script, name='rotation_script')


import pymel.core as pm
transform_cylinder, creation_cylinder = pm.polyCylinder(name='referenceCylinder')
transform_cylinder.rotateX.set(90)
space_loc = pm.spaceLocator(name='current_position')
reference_loc = pm.spaceLocator(name='reference_position')
transform_cylinder.setParent(space_loc)

script = f'if (frame > 10)\n'
script += '{\n'
script += f'   vector $current_position = `xform -q -worldSpace -translation  {space_loc}`;\n'
script += f'   vector $reference_position = `xform -q -worldSpace -translation  {reference_loc}`;\n'
script += f'   vector $distancia = $current_position - $reference_position;\n'
script += f'	  float $array_float[] = `xform -q -matrix {space_loc}`;\n'
script += f'	  vector $x_vector = <<$array_float[0],$array_float[1],$array_float[2]>>;\n'
script += f'   float $delta_rot = -dotProduct($distancia, $x_vector, 1) * rad_to_deg(mag($distancia)/{creation_cylinder}.radius);\n'
script += f'   {transform_cylinder}.rotateZ = {transform_cylinder}.rotateZ + $delta_rot;\n'
script += f'   vector $current_position_value = `xform -q -worldSpace -translation  {space_loc}`;\n'
script += f'   xform -translation ($current_position_value.x) ($current_position_value.y) ($current_position_value.z) -worldSpace  reference_position;\n'
script += '}'
script += f'else\n'
script += '{\n'
script += f' {transform_cylinder}.rotateZ=0;\n'
script += '}'
pm.expression(string=script, name='rotation_script')



