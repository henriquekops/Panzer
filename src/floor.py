#!/usr/bin/env python
# -*- coding: utf-8 -*-

# project dependencies
from src.common.opengl_object import OpenGlObject

# external dependencies
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


@OpenGlObject.register
class Floor():

    """
    Floor class
    """

    def __init__(self, width, height) -> None:
        self.width = round(width)
        self.height = round(height)

    def draw(self):
        """
        Draw floor
        """
        glPushMatrix()
        glTranslated(0, -1, 0)
        for _ in range(0, self.width):
            glPushMatrix()
            for _ in range(0, self.height):
                self.__draw_cell()
                glTranslated(0, 0, 1)
            glPopMatrix()
            glTranslated(1, 0, 0)
        glPopMatrix()

    def __draw_cell(self):
        """
        Draw floor cell 1x1 (center at 0,0,0 and over XZ axis)
        """
        glColor3f(0.25,1.0,0.25) # quad
        glBegin ( GL_QUADS )
        glNormal3f(0, 1, 0)
        glVertex3f(-0.5,  0.0, -0.5)
        glVertex3f(-0.5,  0.0,  0.5)
        glVertex3f( 0.5,  0.0,  0.5)
        glVertex3f( 0.5,  0.0, -0.5)
        glEnd()
        
        # glColor3f(1, 1, 1) # border
        # glBegin ( GL_LINE_STRIP )
        # glNormal3f(0, 1, 0)
        # glVertex3f(-0.5,  0.0, -0.5)
        # glVertex3f(-0.5,  0.0,  0.5)
        # glVertex3f( 0.5,  0.0,  0.5)
        # glVertex3f( 0.5,  0.0, -0.5)
        # glEnd()
