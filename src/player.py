#!/usr/bin/env python
# -*- coding: utf-8 -*-

# project dependencies
from src.common.opengl_object import OpenGlObject

# external dependencies
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


OpenGlObject.register
class Player():

    """
    Player class
    """

    def __init__(self) -> None:
        super().__init__()

    def set_position(self, aspect_ratio):
        """
        Position user
        """
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        gluPerspective(40,aspect_ratio,0.01,50) # Projecao perspectiva
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 4, 10, 0, 0, 0, 0, 1.0, 0.0) 

    def draw(self):
        """
        Draw Player
        """
        pass