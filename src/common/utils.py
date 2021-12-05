#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in dependencies
from math import (
    pow,
    sqrt
)

# external dependencies
import numpy as np


class Utils:

    """
    Class utils
    """

    @classmethod
    def vector(cls, vertex1:np.array, vertex2: np.array) -> np.array:
        """
        Create vector between two vertices
        """
        return vertex2 - vertex1

    @classmethod
    def module(cls, vector: np.array) -> float:
        """
        Get the module of a vector
        """
        return sqrt(pow(vector[0], 2)+pow(vector[1], 2)+pow(vector[2], 2))
    
    @classmethod
    def unit(cls, vector:np.array) -> np.array:
        """
        Create unit vector of parametrized vector
        """
        return np.around(vector / cls.module(vector))
