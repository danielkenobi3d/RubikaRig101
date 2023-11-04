import pymel.core as pm


def create_control_on_transform(maya_node):
    control, create_circle = pm.circle(name='reset_control')
    reset_control = pm.group(empty=True, name='reset_control')
    pm.matchTransform(control, maya_node)
    pm.matchTransform(reset_control, maya_node)
    pm.parent(control, reset_control)
    return reset_control, control


def constraint_nodes(source_list, destination_list):
    # creates a control on the first element of the source_list
    reset_control, control = create_control_on_transform(source_list[0])
    pm.addAttr(control, longName='ikControl', keyable=True, min=0, max=1)
    reverse_node = pm.createNode('reverse', name='flip_value')

    # this is connecting the attributes of the control to the reverse node
    control.ikControl >> reverse_node.inputX

    # zip cycles through 2 iterables, and matches one on one the content of the lists
    parent_constraints_list = []
    for source, destination in zip(source_list, destination_list):
        output = pm.joint(name='output')
        pm.parentConstraint(source, output, mo=False)
        parent_constraint_node = pm.parentConstraint(destination, output, mo=False)
        parent_constraints_list.append(parent_constraint_node)
        weight_alias = parent_constraint_node.getWeightAliasList()

        control.ikControl >> weight_alias[0]
        reverse_node.outputX >> weight_alias[1]


ik_joints_list = pm.ls('ik_joint*')
fk_joints_list = pm.ls('fk_joint*')
constraint_nodes(ik_joints_list, fk_joints_list)