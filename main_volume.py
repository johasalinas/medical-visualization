import vtk
import sys
import sys
import vtk

# 1 get data path from the first argument given

# 2 set up the source

# 3 set up the volume mapper

# 4 create a transfer function for color 
#   for now: map value 0   -> black: (0., 0., 0.) 
#                      512 -> black: (1., 1., 1.) 

# 5 create a scalar transfer function for opacity
#   for now: map value 0   -> 0. 
#                      256 -> .01

# 6 set up the volume properties with linear interpolation 

# 7 set up the actor and connect it to the mapper and the volume properties

# 8 set up the camera
#   for now: up-vector:       (0., 1., 0.)
#            camera position: (-500, 100, 100)
#            focal point:     (100, 100, 100)

# 9 create a renderer and set the color of the renderers background to black (0., 0., 0.)

# 10 set the renderers camera as active

# 11 add the volume actor to the renderer

# 12 create a render window

# 13 add renderer to the render window

# 14 create an interactor

# 15 connect interactor to the render window

# 16 start displaying the render window

# 17 make the window interactive (start the interactor)
