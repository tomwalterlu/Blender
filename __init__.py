bl_info = {
    "name" : "Perlin Berge",
    "author" : "Tom Walter",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from .createEmptyPlane import Generate_Terrain_Operation
from .configureMountains_op import Mountain_Configuration
from .smoothedges_op import Smooth_Edges
from .heightPaint_op import Paint_Height_Map
from .panel import Panel
from .perlin import PerlinNoiseFactory

classes = (Panel, Generate_Terrain_Operation,Mountain_Configuration, Paint_Height_Map, Smooth_Edges)

register, unregister = bpy.utils.register_classes_factory(classes)