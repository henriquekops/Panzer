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
            glTranslate(self.x, self.y, self.z)
            glutSolidCube(1)
            glPopMatrix()

    def __init__(self) -> None:
        self.cells: self.Cell = []

    def build(self, width, height, dist): # texture
        """
        Build wall
        """
        for x in range(0, width-1):
            for y in range(-1, height-2):
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
                cell.draw()
                glPopMatrix()