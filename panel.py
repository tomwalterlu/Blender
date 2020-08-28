import bpy

class Panel(bpy.types.Panel):
  bl_idname = "Test_PT_Panel"
  bl_label = "Perlin Berge"
  bl_category = "Perlin Berge"
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"

  def draw(self, context):
    layout = self.layout
    
    row1 = layout.row()
    row2 = layout.row()
    row3 = layout.row()
    row4 = layout.row()


    row1.operator('view3d.terrainop', text="Fläche erzeugen")
    row2.operator('view3d.heightpaint', text="Gebirgeareal zeichnen")
    row3.operator('view3d.configuremountains', text="Hügel anpassen und erzeugen")
    row4.operator('view3d.smoothedges', text ="(Optional) Glätten")