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

    def __init__(self) -> None:
        pass

    def draw(self):
        """
        Draw wall
        """
        glPushMatrix()
        glTranslated(-20,-1,-10)
        for _ in range(-20, 20):
            glPushMatrix()
            for _ in range(-20, 20):
                self.__draw_cell()
                glTranslated(0, 0, 1)
            glPopMatrix()
            glTranslated(1, 0, 0)
        glPopMatrix()

    def __draw_cell(self):
        """
        Draw floor cell 1x1 (center at 0,0,0 and over XZ axis)
        """
        glColor3f(0,0,1) # desenha QUAD preenchido
        glBegin ( GL_QUADS )
        glNormal3f(0,1,0)
        glVertex3f(-0.5,  0.0, -0.5)
        glVertex3f(-0.5,  0.0,  0.5)
        glVertex3f( 0.5,  0.0,  0.5)
        glVertex3f( 0.5,  0.0, -0.5)
        glEnd()
        
        glColor3f(1,1,1) # desenha a borda da QUAD 
        glBegin ( GL_LINE_STRIP )
        glNormal3f(0,1,0)
        glVertex3f(-0.5,  0.0, -0.5)
        glVertex3f(-0.5,  0.0,  0.5)
        glVertex3f( 0.5,  0.0,  0.5)
        glVertex3f( 0.5,  0.0, -0.5)
        glEnd()
