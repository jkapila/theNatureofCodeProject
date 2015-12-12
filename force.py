
"""
Implementation of Forces form the book

"""

from vector import PVector
from mover import Movement
from genrics import *

class Force(PVector):
    """

    """

    def __init__(self,mass, const, unitvector):
        """

        :param mass:
        :param const:
        :param unitvector:
        :return:
        """
        super(Force, self).__init__(unitvector.x,unitvector.y,unitvector.z,unitvector.ang)
        self.mass = mass
        self.const = const
        self.unitvector = unitvector

    def applyForceWith(self, moving_vector, **kwargs):
        """

        :param force:
        :param kwargs:
        :return:
        """
        moving_vector.mult(self.mass)
        # f.mult(self.mass)
        self.add(moving_vector)
        return addition(moving_vector,self.get())


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
        return addition(moving_vector,f)


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
        return addition(moving_vector,f)


