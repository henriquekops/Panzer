#!/usr/bin/env python
# -*- coding: utf-8 -*-

# project dependencies
from src.common.opengl_object import OpenGlObject


OpenGlObject.register
class Npc:

    """
    Npc class
    """

    def __init__(self, is_friendly) -> None:
        self.is_friendly = is_friendly
        pass

    def draw(self):
        """
        Draw npc
        """
        pass