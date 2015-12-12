

"""
This is main class
"""

from __future__ import division, print_function

from environments import *

from force import AirResistance, WaterResistance, Friction
from genrics import *
from mover import Movement
from plot_wrapper import Plotter


def main():

    # mover = []
    width = 400
    height = 200
    location = PVector(4,30)
    velocity = PVector(0,0)
    acceleration = PVector(0.1,0.2)

    move = Movement(location,velocity,acceleration,"one",width,height,500)

    pl = Plotter(width,height)
    pl.set_data(move.next)
    pl.plotter()

    liquid = Liquid(0,height/2,width/2,height/2,0.1)
    air = AirResistance(mass=0.1,unitvector=PVector(1,0))
    friction = Friction(5,0.3,PVector(-1,-1))
    water = WaterResistance()

    air = air.applyForceWith(move.acc)
    friction = friction.applyForceWith(move.vel)
    water = water.applyForceWith(move.vel)

    # move.applyForce(air)
    # move.applyForce(friction)

    # if isInside(vec=move.loc,l=liquid):
    #     move.applyForce(water)

    pl2 = Plotter(width,height)

    pl2.set_data(move.next)

    pl2.plotter()




if __name__ == '__main__': main()