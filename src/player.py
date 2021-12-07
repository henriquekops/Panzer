#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in dependencies
from math import (
    sin,
    cos,
    radians
)

# project dependencies
from src.common.opengl_object import OpenGlObject
from src.common.utils import Utils
from src.projectile import Projectile

# external dependencies
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np


OpenGlObject.register
class Player:

    """
    Player class
    """

    def __init__(self, x:float, z:float) -> None:
        self.alpha_camera = 5
        self.alpha_cannon = 0.0
        self.alpha_aim = 0.0
        self.step_size = 1
        self.obs = np.array((x, 0.5, z))
        self.tgt = np.array((x, 0.5, z+10.0))
        self.cam = np.array((0.0, 1.0, 0.0))
        self.projectiles = []
        self.cooldown = 0

    def set_position(self, aspect_ratio):
        """
        Position user
        """
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        gluPerspective(40, aspect_ratio, 0.05, 100)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(
            self.obs[0], self.obs[1], self.obs[2],
            self.tgt[0], self.tgt[1], self.tgt[2],
            self.cam[0], self.cam[1], self.cam[2]
        )

    def draw(self) -> None:
        """
        Draws player
        """
        quadric = gluNewQuadric()
        glPushMatrix()
        glTranslated(self.obs[0], -0.5, self.obs[2])
        glRotatef(self.alpha_cannon, 0, 1, 0)
        glRotatef(self.alpha_aim, 1, 0, 0)
        gluCylinder(quadric, 0.2, 0.2, 5, 5, 5)
        glPopMatrix()

    def shoot(self) -> None:
        """
        Add projectile
        """
        self.projectiles.append(Projectile(self.obs[0], self.obs[1], self.obs[2], self.alpha_cannon))

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
        self.tgt[0] = (self.tgt[0] * cos(radians(self.alpha_camera))) + (self.tgt[2] * sin(radians(self.alpha_camera)))
        self.tgt[1] = self.tgt[1]
        self.tgt[2] = (-self.tgt[0] * sin(radians(self.alpha_camera))) + (self.tgt[2] * cos(radians(self.alpha_camera)))
        self.tgt += self.obs
        self.alpha_cannon += self.alpha_camera

    def right(self) -> None:
        """
        Look right
        """
        self.tgt -= self.obs
        self.tgt[0] = (self.tgt[0] * cos(radians(-self.alpha_camera))) + (self.tgt[2] * sin(radians(-self.alpha_camera)))
        self.tgt[1] = self.tgt[1]
        self.tgt[2] = (-self.tgt[0] * sin(radians(-self.alpha_camera))) + (self.tgt[2] * cos(radians(-self.alpha_camera)))
        self.tgt += self.obs
        self.alpha_cannon -= self.alpha_camera


