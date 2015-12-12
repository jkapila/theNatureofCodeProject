

"""
Here we will generate the environments for the system
"""

class Liquid(object):

    def __init__(self,x,y, width, height, coeff):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.coeff = coeff

    def display(self):
        pass


def isInside(vec,l):
    """

    :param vec: Location Vector
    :param l: Liquid environment
    :return: boolean whether location is inside liquid or not
    """

    if vec.x > l.x and vec.x < l.x+l.width and vec.y > l.y and vec.y < l.y+l.height:
        return True
    else:
        return False
