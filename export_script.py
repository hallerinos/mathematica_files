import bpy

scene = bpy.data.scenes['Scene']
objs = scene.objects
for frame in range(1,418):
    bpy.context.scene.frame_set(frame)
    # print(objs["Pulsar_Icosphere"].matrix_world)
    # bpy.data.node_groups['NodeTree'].execute()
    # bpy.context.scene.render.filepath = './renderings/sphere%04d.png' % frame
    bpy.context.scene.render.filepath = './mantaflow%05d.png' % frame
    bpy.ops.render.render(write_still=True)
