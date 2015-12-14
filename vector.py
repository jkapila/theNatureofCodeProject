

"""
This is code implementation of lessons from The Nature of Code using Processing

"""

from __future__ import (absolute_import, division, print_function, unicode_literals)
import six
import numpy as np
import random
import math


class PVector(object):
    """
    this will generate single vector
    """

    def __init__(self, x=0.0, y=0.0, z=0.0, ang=0):
        self.x = x
        self.y = y
        self.z = z
        self.ang = ang
        self.counter = 0
        self.terminal = 0

    def add(self, vec):
        self.x = self.x + vec.x
        self.y = self.y + vec.y
        self.z = self.z + vec.z
        self.limit_check()

    def sub(self, vec):
        self.x = self.x - vec.x
        self.y = self.y - vec.y
        self.z = self.z - vec.z

    def mult(self, a):
        self.x = self.x*a
        self.y = self.y*a
        self.z = self.z*a

    def div(self, d):
        if d != 0:
            self.x /= d
            self.y /= d
            self.z /= d

    def mag(self):
        return math.sqrt((self.x*self.x) + (self.y*self.y) + (self.z*self.z))

    def normalize(self, d=1):
        m = self.mag()
        if m != 0:
            self.div(m)
        self.mult(d)

    def limit(self, d):
        self.terminal = d

    def limit_check(self):
        if self.terminal != 0:
            d= self.terminal
            self.x = d if self.x > d else self.x
            self.y = d if self.y > d else self.y
            self.z = d if self.z > d else self.z
            self.counter += 1

    def get(self):
        return self.x, self.y, self.z, self.ang

    def set_mag(self, d):
        self.normalize()
        self.mult(d)

    def random2D(self):
        self.x = random.random
        self.y = random.random
        self.z = 0.0
        self.get()

    def random3D(self):
        self.x = random.random
        self.y = random.random
        self.z = random.random
        self.get()

class PVectors(object):
    """
    This is for arrays of vectors
    We need this because objects in Processing and Python(Matplotlib) are not same
    """

    def __init__(self, array=np.array([0, 0, 0, 0]), array_count=5):
        """

        :param array:   this is vector information array denoting [x,y,z,theta]
                        here we are considering only 2d plots only
                        for 3d plot we might need array like [x,y,z,theta(xy),theta(yz),theta(zx)]
                        for this we set self.parameters as 4
        :param array_count: number of points
        :return: a vector object
        """
        self.points = array_count
        self.parameters = 4
        if array.any():
            self.vector = array
        else:
            self.vector = np.zeros((array_count, self.parameters), dtype=np.float64)

        self.terminal = 0
        self.counter = 0

    def add(self, vector):

        self.vector = np.add(self.vector, vector)
        self.limit_check()

    def sub(self, vector):
        self.vector = np.subtract(self.vector, vector)

    def mult(self, value):
        self.vector *= value

    def mult_axis(self, value=0.1, axis=0):
        self.vector[:, axis] *= value

    def div(self, value):
        if value != 0:
            self.vector /= value

    def mag(self):
        return np.linalg.norm(self.vector, axis=1, ord=2, keepdims=True)

    def normalize(self, value=1):
        m = self.mag()
        if m.all():
            self.vector = np.divide(self.vector, m)
        self.mult(value)

    def limit(self, terminal):
        self.terminal = terminal

    def limit_check(self):
        if self.terminal != 0:
            vec = self.vector
            vec[vec > self.terminal] = self.terminal
            self.vector = vec
            self.counter += 1

    def alter_axis(self, additor=0, multiplier=0.10, axis=0, dimension=2):
        self.vector += additor
        self.vector[:, axis] *= multiplier
        if dimension <= self.parameters:
            for i in range(dimension, self.parameters):
                self.vector[:, i] = 0

    def get(self):
        return self.vector

    def random2d(self, additor=0, multiplier=10):
        self.vector = additor + np.random.random((self.points, self.parameters))
        self.mult(multiplier)
        for i in range(2, self.parameters):
            self.vector[:, i] = 0
        return self.vector

    def random3d(self, additor=0, multiplier=10):
        self.vector = additor + np.random.random((self.points, self.parameters))
        self.mult(multiplier)
        for i in range(3, self.parameters):
            self.vector[:, i] = 0
        return self.vector
