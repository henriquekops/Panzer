#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in dependencies
from math import (
    sin,
    cos
)

# project dependencies
from src.common.opengl_object import OpenGlObject
from src.common.utils import Utils

# external dependencies
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np


OpenGlObject.register
class Player():

    """
    Player class
    """

    def __init__(self) -> None:
        super().__init__()
        self.alpha = 0.45
        self.step_size = 1
        self.obs = np.array((0.0, 0.0, 10.0))
        self.tgt = np.array((0.0, 0.0, 0.0))
        self.cam = np.array((0.0, 1.0, 0.0))

    def set_position(self, aspect_ratio):
        """
        Position user
        """
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        gluPerspective(40, aspect_ratio, 0.01, 50)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(
            self.obs[0], self.obs[1], self.obs[2],
            self.tgt[0], self.tgt[1], self.tgt[2],
            self.cam[0], self.cam[1], self.cam[2]
        )

    def draw(self):
        """
        Draw Player
        """
        pass

    def forward(self) -> None:
        """
        Move forwards
        """
        tgt_unit = Utils.unit(Utils.vector(self.obs, self.tgt))
        self.obs += (tgt_unit * self.step_size)
        self.tgt += (tgt_unit * self.step_size)

    def backward(self) -> None:
        """
        Move backwards
        """
        tgt_unit = Utils.unit(Utils.vector(self.obs, self.tgt))
        self.obs -= (tgt_unit * self.step_size)
        self.tgt -= (tgt_unit * self.step_size)

    def left(self) -> None:
        """
        Look left 
        """
        self.tgt -= self.obs
        self.tgt[0] = self.tgt[0] * cos(self.alpha) + self.tgt[2] * sin(self.alpha) 
        self.tgt[1] = self.tgt[1]
        self.tgt[2] = -self.tgt[0] * sin(self.alpha) + self.tgt[2] * cos(self.alpha)
        self.tgt += self.obs
    
    def right(self) -> None:
        """
        Look right
        """
        self.tgt -= self.obs
        self.tgt[0] = self.tgt[0] * cos(-self.alpha) + self.tgt[2] * sin(-self.alpha)
        self.tgt[1] = self.tgt[1]
        self.tgt[2] = -self.tgt[0] * sin(-self.alpha) + self.tgt[2] * cos(-self.alpha)
        self.tgt += self.obs