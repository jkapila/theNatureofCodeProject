

"""

This in implementation of vector

"""

from __future__ import (absolute_import, division, print_function, unicode_literals)
import six

import numpy as np
from vector import PVector
from environments import *



class Movement(object):

    def __init__(self, location, velocity, acceleration, checkcondition,width=400, height=200,topspeed = 10,):

        self.w = width
        self.h = height
        self.loc = location
        self.vel = velocity
        self.acc = acceleration
        self.checkcondition= checkcondition
        self.vel.limit(topspeed)

    def __iter__(self):
        return self

    def next(self):
        if self.vel.counter < 100:
            self.update()
            self.check_edges()
            return self.loc.x,self.loc.y
        else:
            raise StopIteration

    def update(self):

        self.vel.add(self.acc)
        self.loc.add(self.vel)


    def check_edges(self):

        if "one" in self.checkcondition:
            if self.loc.y >= self.h:
                self.loc.y = 0
            elif self.loc.y < -self.h:
                self.loc.y =  self.h

        if "two" in self.checkcondition:
            if self.loc.y >= self.h:
                self.loc.y = 0
            elif self.loc.y < -self.h:
                self.loc.y =  self.h

            if self.loc.x >= self.w:
                self.loc.x = 0
            elif self.loc.x < 0:
                self.loc.x =  self.w


    def get(self):
        return self.loc, self.vel, self.acc

    def get_loc(self):
        return self.loc.x,self.loc.y

    def applyForce(self, force, **kwargs):

        f =  PVector(force.x,force.y,force.z)
        if 'value' in kwargs:
            f.div(kwargs['value'])
        else:
            f.div(force.mass)

        if "evn" in kwargs:
            if isInside(self.loc,kwargs["env"]):
                self.applyForce(force)

        self.acc.add(f)