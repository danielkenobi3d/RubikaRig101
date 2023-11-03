from RMPY.rig import rigSingleJoint
my_rig = rigSingleJoint.RigSingleJoint()
my_rig.create_point_base('C_arm00_reference_pnt',
                         'C_arm01_reference_pnt',
                         'C_arm02_reference_pnt')

my_rig.create.curve.point_base('C_arm00_reference_pnt',
                                     'C_arm01_reference_pnt',
                                     'C_arm02_reference_pnt', ep=True)
my_rig.create.group.point_base('C_arm00_reference_pnt',
                                'C_arm01_reference_pnt',
                                'C_arm02_reference_pnt')