
"""
These are general methods definition
"""

from vector import PVector

def addition(vec1, vec2):

    return PVector(vec1.x+vec2.x, vec1.y+vec2.y, vec1.z+vec2.z)

def subtract(vec1, vec2):

    return PVector(vec1.x-vec2.x, vec1.y-vec2.y, vec1.z-vec2.z)

def multiply(vec1, d):

    return PVector(vec1.x,vec1.y,vec1.z).mult(d)

def divide(vec1, d):

    return PVector(vec1.x,vec1.y,vec1.z).div(d)