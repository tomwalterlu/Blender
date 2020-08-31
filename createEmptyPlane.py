import bpy
import bmesh
from bpy import context
import math
import random
from .perlin import PerlinNoiseFactory


class Generate_Terrain_Operation(bpy.types.Operator):
  bl_label = "Fläche hinzufügen Dialog"
  bl_idname = "view3d.terrainop"

  text = bpy.props.StringProperty(name = "Enter Text", default= "")
  size = bpy.props.FloatProperty(name="Flächenhoehe-/weite", default=10)
  amountCells = bpy.props.IntProperty(name="Zellen in jede Richtung", default = 15)
  
  def execute(self, context):
    t = self.text
    s = self.size
    amountCells = self.amountCells
    layout = self.layout

    #Initializieren der Knoten für gegebene Parameter
    utils = Utils()
    #Dynamisch generierte Knoten und Faces erhalten
    v,f = utils.generateOrderedVerticesAndFaces(amountCells, s)
    #2 Dimensionales Array in ein 1D Array formen ("array flattening")
    v_flat = [j for sub in v for j in sub]

    # Mesh von Knoten and Faces erstellen
    mesh = bpy.data.meshes.new(t)
    mesh.from_pydata(v_flat, [], f)
    mesh.update()

    # Mesh zu neuem Object hinzufügen    
    new_object = bpy.data.objects.new(self.text, mesh)
    new_object.data = mesh

    #Setup Scene
    scene = bpy.context.scene
    scene.collection.objects.link(new_object)

    return {'FINISHED'}

  def invoke(self, context, event):
    return context.window_manager.invoke_props_dialog(self)


class Utils:
#Generiert Knoten basierend auf der Anzahl horizontaler und vertikaler Zellen, jede Zelle mit Größe "Size" und geordnet mit (x,y)
  def generateOrderedVerticesAndFaces(Utils,amountCells, size):
      size = size / 2
      v = [[(0,0,0)] * (amountCells+1) for i in range(amountCells+1)] 
      f = [(0,0,0,0)] * amountCells * amountCells
      e = [(0,0)] * amountCells * amountCells * 5
      #Generiert Knoten in Gittermuster
      for x in range(amountCells+1):
          for y in range(amountCells+1):
              xCoord = -size + x * (size/ (amountCells / 2))
              yCoord = -size + y * (size/ (amountCells / 2))
              zCoord = 0
              v[y][x] = (xCoord, yCoord, zCoord)
              if(x < amountCells and y < amountCells):
                #Generiert Faces in Gittermuster
                down_left = x + y * (amountCells + 1)
                down_right = down_left + 1
                up_left = down_left + amountCells + 1
                up_right = up_left + 1
                newX = x * 4
                f[amountCells * y + x] = (down_left, down_right, up_right, up_left)
      return v,f
  def isBorderVertex(Utils,vertex):
    '''
        Überprüft ob dieser Knoten sich auf dem Rand des Plane Objekts befindet oder einer seiner Nachbarknoten nicht auf der Heightmap liegt
        Return 0 => Knoten ist weder am Rand noch selektiert
        Return 1 => Knoten ist am Rand der Plane
        Return 2 => Knoten ist am Rand der Selektion und nicht am Rand
    '''
    #jeder Knoten hat max. 4 Nachbarknoten
    ob = bpy.data.objects[0]
    vertices = ob.data.vertices
    dimension = math.sqrt(len(vertices))-1     #10x10 Zellen => returns 10
    gi = 0
    #Spezialfall: Aktuell betrachtener Knoten ist am Rand
    if(vertex.index == 0 or vertex.index % (dimension + 1) == 0): #linker Rand
        return 1
    elif(vertex.index < dimension + 1): #unterer Rand
        return 1
    elif((vertex.index - (vertex.index // dimension - 1) * (dimension+1) == dimension)): #rechter Rand
        return 1
    elif(vertex.index >= (dimension + 1) * dimension - 1): #Rand oben
        return 1
    else:   #Falls kein Randknoten , überprüfe ob Nachbarknoten nicht selektiert ist.
        neighbour_right =  vertices[vertex.index + 1]
        neighbour_left = vertices[vertex.index - 1]
        neighbour_up = vertices[int(vertex.index - 1) + int(dimension+1)]
        neighbour_down = vertices[int(vertex.index - 1) - int(dimension+1)]
        neighbours = [neighbour_right, neighbour_left, neighbour_up, neighbour_down]

        for n in neighbours:
            for g in n.groups:
                if((g.group == gi) == 0):
                    return 2
        return 0
    return 0

