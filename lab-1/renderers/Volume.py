__author__ = 'fabian sinzinger'
__email__ = 'fabiansi@kth.se'

import os
import sys

import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class VolumeRenderer:
    def __init__(self, filename, frame):
        # load the data
        reader_src = vtk.vtkNIFTIImageReader()
        reader_src.SetFileName(filename)

        # transfer function, colot luts
        
        # set the volume properties

        # setup the volume mapper

        # setup the actor

        # setup the camera and the renderer

        # window interaction (camera movement etc)
        self.interactor = QVTKRenderWindowInteractor(frame)
        style = vtk.vtkInteractorStyleTrackballCamera()
        self.interactor.SetInteractorStyle(style)

        self.interactor.Initialize()


