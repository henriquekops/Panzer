#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in dependencies
import abc


class OpenGlObject(abc.ABC):

    """
    Common abstract class
    """

    @abc.abstractclassmethod
    def draw(self):
        pass
