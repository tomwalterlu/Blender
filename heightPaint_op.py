import bpy
from bpy import context


class Paint_Height_Map(bpy.types.Operator):
  """Open the Add Cube Dialog Box"""
  bl_label = "Add Height Map Box"
  bl_idname = 'view3d.heightpaint'

  def execute(self, context):
    layout = self.layout
    bpy.ops.paint.weight_paint_toggle()
    return {'FINISHED'}

  def invoke(self, context, event):
    return context.window_manager.invoke_props_dialog(self)

