

"""
This is code implementation of lessons from The Nature of Code using Processing

"""

from __future__ import (absolute_import, division, print_function, unicode_literals)
import six

import random
import math


class PVector(object):

    def __init__(self, x=0.0, y=0.0, z=0.0, ang=0):
        self.x = x
        self.y = y
        self.z = z
        self.ang = ang
        self.counter = 0

    def add(self, vec):
        self.x = self.x + vec.x
        self.y = self.y + vec.y
        self.z = self.z + vec.z

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

    def normalize(self):
        m = self.mag()
        if m != 0:
            self.div(m)

    def limit(self, d):
        self.x = d if self.x > d else self.x
        self.y = d if self.y > d else self.y
        self.z = d if self.z > d else self.z
        self.counter += 1

    def get(self):
        return self.x,self.y,self.z,self.ang

    def set_mag(self, d):
        self.normalize()
        self.mult(d)

    def random2D(self):
        self.x = random.random
        self.y = random.random
        self.z = 0.0

    def random3D(self):
        self.x = random.random
        self.y = random.random
        self.z = random.random
