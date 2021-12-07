#!/usr/bin/env python
# -*- coding: utf-8 -*-

# project dependencies
from src.common.opengl_object import OpenGlObject
from src.wall import Cell

# external dependencies
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


OpenGlObject.register
class Projectile:

    def __init__(self, x, y, z, alpha) -> None:
        self.x = x
        self.y = y 
        self.z = z
        self.alpha = alpha
        self.delete = False
    
    def draw(self):
        if self.z < 50:
            glPushMatrix()
            glColor3f(1, 1, 1)
            glRotatef(self.alpha, 0, 1, 0)
            glTranslated(self.x, self.y, self.z)
            glutSolidSphere(0.2, 5, 5)
            glPopMatrix()
            self.z += 1
        else:
            self.delete = True

    def collision(self, cell: Cell) -> bool:
        x_dist = abs(self.x - cell.x)
        y_dist = abs(self.y - cell.y)
        z_dist = abs(self.z - cell.z)

        return x_dist < 1.2 and y_dist < 1.2 and z_dist < 1.2