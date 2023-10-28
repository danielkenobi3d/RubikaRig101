import maya.cmds as cmds

# Define the number of rows and columns
rows = 5
columns = 5

# Define the size of each box
box_size = 1

# Create a loop to create boxesf
for i in range(rows):
    for j in range(columns):
        cmds.polyCube(w=box_size, h=box_size, d=box_size)
        cmds.move(i*box_size, 0, j*box_size)