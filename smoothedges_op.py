import bpy
from bpy import context



class Smooth_Edges(bpy.types.Operator):
  bl_label = "Im Sculpt Mode 'Smooth' benutzen zur Randglättung"
  bl_idname = 'view3d.smoothedges'

  def execute(self, context):
    layout = self.layout
    bpy.ops.sculpt.sculptmode_toggle()
    return {'FINISHED'}

  def invoke(self, context, event):
    return context.window_manager.invoke_props_dialog(self)




