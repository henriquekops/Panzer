#!/usr/bin/env python
# -*- coding: utf-8 -*-

# project dependencies
from src.common.opengl_object import OpenGlObject

@OpenGlObject.register
class Wall():

    """
    Wall class
    """

    def __init__(self) -> None:
        pass

    def draw(self):
        """
        Draw wall
        """
        pass