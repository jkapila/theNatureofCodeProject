

"""

This in implementation of vector

"""

from __future__ import (absolute_import, division, print_function, unicode_literals)
import six

import numpy as np
from vector import PVector
from environments import *



class Movement(object):

    def __init__(self, location,
                 velocity,
                 acceleration,
                 width=400,
                 height=200,
                 topspeed = 10,
                 checkcondition = "one",
                 counter = 1000,
                 size = 10):

        self.w = width
        self.h = height
        self.loc = location
        self.vel = velocity
        self.acc = acceleration
        self.checkcondition= checkcondition
        self.counter = counter
        self.size = size
        self.vel.limit(topspeed)
        self.pointer=[]

    def __iter__(self):
        return self

    def next(self,point=[]):

        if not len(point):
            pass
        elif point not in self.pointer:
            self.loc.x,self.loc.y = point[0]
            self.pointer.append(point[0])

        if self.vel.counter < self.counter:
            print("loc : {} vel : {} acc : {}".format(self.loc.get(),self.vel.get(),self.acc.get()))
            self.update()
            self.check_values()
            return self.loc.x,self.loc.y,self.size
        else:
            raise StopIteration

    def update(self):
        # print('calling update')
        self.vel.add(self.acc)
        self.loc.add(self.vel)


    def check_values(self):

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
            elif self.loc.x < -self.w:
                self.loc.x = self.w


    def get(self):
        return self.loc, self.vel, self.acc

    def get_loc(self):
        return self.loc.x,self.loc.y

    def applyForce(self, force, **kwargs):

        f =  force.unitvector
        print("force applied : {}".format(force))
        if 'value' in kwargs:
            f.div(kwargs['value'])
        else:
            f.div(force.mass)

        if "evn" in kwargs:
            if isInside(self.loc,kwargs["env"]):
                self.applyForce(force)

        self.acc.add(f)