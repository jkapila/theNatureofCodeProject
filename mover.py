

"""

This in implementation of vector

"""
from __future__ import division
from random import Random
from vector import PVector


class Mover:

    def __init__(self, impl, width=400, height=200):

        self.width = width
        self.height = height
        self.location = PVector()
        self.velocity = PVector()
        self.accleration = PVector()
        self.topspeed = 1

        self.initialze(impl)

    def initialze(self, impl):

        if impl == "simple":
            self.location = PVector(self.width/2, self.height/2)
            self.velocity = PVector()
            self.accleration = PVector(-0.001, 0.01)
            self.topspeed = 10

    def update(self):

        self.velocity.add(self.accleration)
        self.velocity.limit(self.topspeed)
        self.location.add(self.velocity)

    def draw(self):
        pass

    def check_edges(self):
        self.location.x = 0 if self.location.x > self.width else self.width
        self.location.y = 0 if self.location.y > self.width else self.width



def add(vec1, vec2):

    return PVector(vec1.x+vec2.x, vec1.y+vec2.y, vec1.z+vec2.z)

def subtract(vec1, vec2):

    return PVector(vec1.x-vec2.x, vec1.y-vec2.y, vec1.z-vec2.z)


