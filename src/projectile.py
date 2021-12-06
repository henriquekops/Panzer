#!/usr/bin/env python
# -*- coding: utf-8 -*-

# project dependencies
from src.common.opengl_object import OpenGlObject

@OpenGlObject.register
class Projectile:

    """
    Projectile class
    """

    def __init__(self) -> None:
        pass

    def draw(self):
        """
        Draws projectile
        """
        glPushMatrix()
        glTranslated(posx,-0.2,posz)
        glutSolidSphere(0.2,10,10)
        glPopMatrix()