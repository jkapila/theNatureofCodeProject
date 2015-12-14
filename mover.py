

"""

This in implementation of vector

"""

from __future__ import (absolute_import, division, print_function, unicode_literals)
import six

import numpy as np
from vector import PVectors
from environments import *


class Movement(object):

    def __init__(self, location, velocity, acceleration,
                 width=400, height=200, topspeed=10, checkcondition="two",
                 counter=1000, size=10):

        self.w = width
        self.h = height
        self.loc = location
        self.vel = velocity
        self.acc = acceleration
        self.checkcondition = checkcondition
        self.counter = counter
        self.size = size
        self.vel.limit(topspeed)
        self.pointer = []
        self.pointer.append((0, 0))

    def __iter__(self):
        return self

    def next(self, point=[]):

        if not len(point):
            pass
        elif point not in self.pointer:
            (x, y) = point
            print('new location : {}'.format(point))
            self.loc.vector[:, 0] = x
            self.loc.vector[:, 1] = y
            # self.acc.random2D(np.random.random(),np.sin(np.random.random()))
            self.pointer.append(point)

        if self.vel.counter < self.counter:
            # print("loc : {} vel : {} acc : {}".format(self.loc.get(),self.vel.get(),self.acc.get()))
            self.update()
            self.check_values()
            return self.loc.get(), self.size
        else:
            raise StopIteration

    def update(self):
        # print('calling update')
        x, y = self.pointer[len(self.pointer)-1]
        vector = PVectors(array=np.array([x, y, 0, 0]), array_count=1)
        vector.sub(self.loc.get())
        vector.normalize(10)
        vector.mult(1.5)
        self.acc.vector = vector.get()
        self.vel.add(self.acc.get())
        self.loc.add(self.vel.get())

    def check_values(self):

        if "one" in self.checkcondition:
            vec = self.loc.vector[:, 1]
            vec[vec >= self.h] = 0
            vec[vec < -self.h] = self.h
            self.loc.vector[:, 1] = vec

        if "two" in self.checkcondition:
            vec = self.loc.vector[:, 0]
            vec[vec > self.w] = 0
            vec[vec < -self.w] = -self.w
            self.loc.vector[:, 0] = vec

            vec = self.loc.vector[:, 1]
            vec[vec > self.h] = 0
            vec[vec < -self.h] = self.h
            self.loc.vector[:, 1] = vec

    def get(self):
        return self.loc, self.vel, self.acc

    def applyForce(self, force, **kwargs):

        f = force.unitvector
        print("force applied : {}".format(force))
        if 'value' in kwargs:
            f.div(kwargs['value'])
        else:
            f.div(force.mass)

        if "evn" in kwargs:
            if isInside(self.loc, kwargs["env"]):
                self.applyForce(force)

        self.acc.add(f)
