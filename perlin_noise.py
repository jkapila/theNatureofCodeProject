

"""
Implementation of Classic Perlin Noise
For further reads refer : https://en.wikipedia.org/wiki/Perlin_noise

And Implementation of Simplex Noise
For further reading refer : https://en.wikipedia.org/wiki/Simplex_noise
"""

from vector import PVector

def lerp(a0, a1, w):
     """

     :param a0: float position
     :param a1: float position
     :param w: Weight w should be in the range [0.0, 1.0]
     :return: linearly interpolate between a0 and a1
     """
     return (1.0 - w)*a0 + w*a1



def dotGridGradient(ix, iy, x, y, vec = PVector()):
    """
    Computes the dot product of the distance and gradient vectors.

    :param ix:
    :param iy:
    :param x:
    :param y:
    :return:
    """
    # // Precomputed (or otherwise) gradient vectors at each grid point X,Y
    if vec != PVector():
        vector = PVector(x,y)
    else:
        vector = vec


    # // Compute the distance vector
    dx = x - ix
    dy = y - iy

    # // Compute the dot-product
    return (dx*vector.x + dy*vector.y)


def perlin(x = 0, y = 0):
    """
    Compute Perlin noise at coordinates x, y

    :param x: x coordiante
    :param y: y coordinate
    :return: noise value
    """

    # Determine grid cell coordinates
    x0 = x if x > 0.0 else x - 1
    x1 = x0 + 1
    y0 =  y  if y > 0.0 else y - 1
    y1 = y0 + 1

    # // Determine interpolation weights
    # // Could also use higher order polynomial/s-curve here
    sx = x - x0
    sy = y - y0

    # // Interpolate between grid point gradients
    # float n0, n1, ix0, ix1, value;
    n0 = dotGridGradient(x0, y0, x, y)
    n1 = dotGridGradient(x1, y0, x, y)
    ix0 = lerp(n0, n1, sx)
    n0 = dotGridGradient(x0, y1, x, y)
    n1 = dotGridGradient(x1, y1, x, y)
    ix1 = lerp(n0, n1, sx)
    value = lerp(ix0, ix1, sy)

    return value
