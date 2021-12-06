#!/usr/bin/env python
# -*- coding: utf-8 -*-

# project dependencies
from src.common.opengl_object import OpenGlObject

# external dependencies
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


@OpenGlObject.register
class Wall:

    """
    Wall class
    """

    @OpenGlObject.register
    class _Cell:

        """
        Wall cell class
        """

        def __init__(self, x, y ,z) -> None:
            self.destroyed = False
            self.x = x
            self.y = y
            self.z = z

        def destroy(self) -> None:
            self.destroyed = True
        
        def draw(self) -> None:
            glPushMatrix()
            glTranslated(self.x, self.y, self.z)
            glutSolidCube(1)
            glPopMatrix()

    def __init__(self, texture_id) -> None:
        self.cells: self.Cell = []
        self.texture_id = texture_id

    def build(self, width, height, dist):
        """
        Build wall
        """
        for x in range(0, width):
            for y in range(-1, height):
                self.cells.append(
                    self._Cell(x, y, dist)
                )

    def draw(self):
        """
        Draw wall
        """
        cell: self._Cell
        for cell in self.cells:
            if not cell.destroyed:
                glPushMatrix()
                glColor3f(1.0, 1.0, 1.0)
                glEnable(GL_TEXTURE_GEN_S)
                glEnable(GL_TEXTURE_GEN_T)
                glBindTexture(GL_TEXTURE_2D, self.texture_id)
                cell.draw()
                glDisable(GL_TEXTURE_GEN_S)
                glDisable(GL_TEXTURE_GEN_T)
                glPopMatrix()
