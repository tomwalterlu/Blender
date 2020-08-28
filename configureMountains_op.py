import bpy
from bpy import context
from .perlin import PerlinNoiseFactory
import math
from .createEmptyPlane import Utils


class Mountain_Configuration(bpy.types.Operator):
  bl_label = "Berge konfigurieren Dialog"
  bl_idname = 'view3d.configuremountains'
  scale = bpy.props.IntProperty(name="Skalierfaktor des Terrains", default=1)

  def execute(self, context):
    scale_factor = self.scale
    layout = self.layout
    utils = Utils()
    ob = bpy.context.object
    gi = 0 #Index der Vertex Gruppe
    iteration = 0
    vg = ob.vertex_groups['Group']
    #Perlin Noise hinuzufügen
    perlin = PerlinNoiseFactory(2, octaves=4, tile=(0, 1))

    for v in ob.data.vertices:
        for g in v.groups:
            if g.group == gi:   #mit Index in der Vertex Gruppe vergleichen
                noise = perlin.get_plain_noise((1 / scale_factor) *v.co.x, (1 / scale_factor) * v.co.y)
                if (utils.isBorderVertex(v) == 1):
                    v.co[2] = 0
                elif(utils.isBorderVertex(v) == 0):
                    if(noise < 0):
                        noise = - noise
                    v.co[2] = v.co[2]  + noise * scale_factor
    # Vertex Gruppe entfernen
    if vg is not None:
        ob.vertex_groups.remove(vg)
    return {'FINISHED'}

  def invoke(self, context, event):
    return context.window_manager.invoke_props_dialog(self)



