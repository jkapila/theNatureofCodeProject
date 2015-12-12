

"""
This is main class
"""

from __future__ import division, print_function

from environments import *

from force import AirResistance, WaterResistance, Friction,Gravity
from genrics import *
from mover import Movement
from plot_wrapper import Plotter


def main():

    # mover = []
    width = 400
    height = 300
    location = PVector(width/2,height/2)
    velocity = PVector(0,0)
    acceleration = PVector(-0.001,0.005)

    move = Movement(location,velocity,acceleration,width=width,height=height,topspeed=10,
                    counter=1000,checkcondition="two",size=50)

    bounds = [-width/2,height/2,width,-height]

    # pl = Plotter(width,height,size=0.1,type="circle",bounds=bounds)
    # pl.set_data(move.next)
    # pl.plotter()

    liquid = Liquid(0,height/2,width/2,height/2,0.1)

    air = AirResistance(mass=0.1,unitvector=PVector(0.0001,0))
    gravity =  Gravity(100)
    friction = Friction(100,0.03,PVector(-0.03,-0.004))
    water = WaterResistance(0.01,0.3,PVector(-0.001,-0.01))

    move.applyForce(air.applyForceWith(move.acc))
    move.applyForce(gravity.applyForceWith(move.acc))
    move.applyForce(friction.applyForceWith(move.acc))

    if isInside(vec=move.loc,l=liquid):
        move.applyForce(water.applyForceWith(move.acc))

    pl2 = Plotter(width,height,type="circle",bounds=bounds,fill='r',boundary="ABCD",
                  interval=10)

    pl2.set_data(move.next)

    pl2.plotter()




if __name__ == '__main__': main()