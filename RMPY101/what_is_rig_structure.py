from RMPY.rig import SystemStructure
import pymel.core as pm
my_rig_structure = SystemStructure.SystemStructure()
my_joint = pm.joint()
my_joint.setParent(my_rig_structure.joints)
my_group = pm.group(empty=True)
my_group.setParent(my_rig_structure.kinematics)
control, creator = pm.circle()
control.setParent(my_rig_structure.controls)
