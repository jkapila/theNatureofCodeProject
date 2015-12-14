
"""
Implementation of Forces form the book

"""

from vector import PVector
from mover import Movement
from genrics import *


class Force(object):
    """

    """

    def __init__(self, mass, const, unitvector):
        """

        :param mass:
        :param const:
        :param unitvector:
        :return:
        """
        # super(Force, self).__init__(unitvector.x,unitvector.y,unitvector.z,unitvector.ang)
        self.mass = mass
        self.const = const
        self.unitvector = unitvector

    def applyForceWith(self, moving_vector, **kwargs):
        """

        :param force:
        :param kwargs:
        :return:
        """
        f=moving_vector
        f.mult(self.mass)
        # f.mult(self.mass)
        self.unitvector.add(f)
        return self


class Friction(Force):

    def __init__(self, mass = 10, const = 0.01 ,unitvector = PVector(0,-1)):
        """

        :param mass:
        :param const:
        :return:
        """
        super(Friction, self).__init__(mass, const, unitvector)

    def applyForceWith(self, moving_vector, **kwargs):
        """

        :param force:
        :param kwargs:
        :return:
        """
        f = moving_vector
        f.mult(-1)
        f.normalize()
        f.mult(self.const)
        self.unitvector.add(f)

        return self


class AirResistance(Force):

    def __init__(self, mass = 0.5, const = 0.01, unitvector = PVector(-0.1,-0.1)):
        """

        :param mass:
        :param const:
        :return:
        """
        super(AirResistance, self).__init__(mass, const, unitvector)

class WaterResistance(Force):

    def __init__(self, mass = 1, const = 0.1, unitvector = PVector(-1,-1)):
        """

        :param mass:
        :param const:
        :return:
        """
        super(WaterResistance, self).__init__(mass, const, unitvector)

    def applyForceWith(self, moving_vector, **kwargs):
        """

        :param force:
        :param kwargs:
        :return:
        """
        c = moving_vector.mag()
        val = self.const * c * c

        f = moving_vector
        f.mult(-1)
        f.normalize()
        f.mult(val)
        self.unitvector.add(f)
        return self

class Gravity(Force):

    def __init__(self, mass = 10, const = 9.8 ,unitvector = PVector(0,0)):
        """

        :param mass:
        :param const:
        :return:
        """
        super(Gravity, self).__init__(mass, const, unitvector)

    def applyForceWith(self, moving_vector, **kwargs):
        """

        :param force:
        :param kwargs:
        :return:
        """
        f = moving_vector
        # f.mult(-1)
        f.normalize()
        f.mult(self.const)
        f.div(self.mass)
        self.unitvector.add(f)

        return self
