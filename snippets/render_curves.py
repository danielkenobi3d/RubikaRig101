import maya.cmds as cmds


def set_curve_attributes(render_curve, curve_width, sample_rate, curve_shader):
    # Check if the shape node is a NURBS curve
    if cmds.nodeType(render_curve) != "nurbsCurve":
        print("Not a NURBS curve:", render_curve)
        return

    # Check if the Arnold node exists for the curve shape
    if not cmds.objExists(render_curve + ".aiRenderCurve"):
        print("No Arnold node found", render_curve)
        return
    # Set render curve attribute to True
    cmds.setAttr(render_curve + ".aiRenderCurve", True)
    cmds.setAttr(f"{render_curve}.aiSampleRate", sample_rate)
    # Connect the shader to aiCurveShader attribute
    cmds.connectAttr(curve_shader + ".outColor", render_curve + ".aiCurveShader", force=True)
    print("Render curve enabled and shader connected for", render_curve)

    # Set the aiCurveWidth attribute
    cmds.setAttr(render_curve + ".aiCurveWidth", curve_width)
    print("Curve width set to", curve_width, "for", render_curve)


def apply_curve_settings(curve_width, sample_rate=50):
    # Get all NURBS curves in the scene
    curve_names = cmds.ls(type="nurbsCurve")

    if not curve_names:
        print("No NURBS curves found.")
        return

    # Get all shading nodes in the scene
    # shading_nodes = cmds.ls(type="shader")
    #  You should get the materials this is how it is done, the type flag is if you want a specific type node and this
    # materials flag is some DAG nodes that are tagged as shaders
    # if you want to apply a specific material you could just place the name there.
    shading_nodes = cmds.ls(materials=True)

    if not shading_nodes:
        print("No shader nodes found.")
        return

    for curve in curve_names:
        # Get the shape nodes connected to the curve
        # Dont think there is need of this you already have the shape selected
        # curve_shapes = cmds.listRelatives(curve, shapes=True, fullPath=True) or []
        set_curve_attributes(curve, curve_width, sample_rate, shading_nodes[0])

        # print("Curve Shapes for", curve, ":", curve_shapes)

 #        for render_curve in curve_shapes:
           ## you just need to do this with one shader, why do it with all the shaders?
            # for shader in shading_nodes:
            #     set_curve_attributes(render_curve, curve_width, sample_rate, shader)
            #so we do it with the first shader that it finds.
            # set_curve_attributes(render_curve, curve_width, sample_rate, shading_nodes[0])


    print("Settings applied successfully.")


# Example usage with dynamic curve and shader retrieval
apply_curve_settings(0.03, sample_rate=2)