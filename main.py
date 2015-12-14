

"""
This is main class
"""

from __future__ import division, print_function
import numpy as np
from environments import *

from force import AirResistance, WaterResistance, Friction,Gravity
from genrics import *
from mover import Movement
# from plot_wrapper import Plotter
from plot_wrap import Plotter
from vector import *


def main():

    # mover = []
    width = 400
    height = 300
    # location = PVector(width/2,height/2)
    # velocity = PVector(0,0)
    # acceleration = PVector(-0.001,0.005)
    vec = PVectors()

    location = PVectors(array_count=1)
    location.random2D(-1,5)
    velocity = PVectors(array_count=1)
    acceleration = PVectors(array_count=1)
    acceleration.alter_axis(1,-0.001,0)
    acceleration.alter_axis(0,-0.001,1)

    move = Movement(location,velocity,acceleration,
                    width=width,height=height,topspeed=5,
                    counter=1000,checkcondition="two",size=10)

    bounds = [0,width,0,height]

    print(move.get())
    # print(move.get_loc())
    # movers = []
    #
    # for i in range(5):
    #     location = PVector(width/(i*10+1),height/(i*10+1))
    #     acceleration = PVector(0.001*np.exp(i/10),0.005*np.exp(-i/2))
    #     size = np.random.rand(1,20)
    #     mover = Movement(location,velocity,acceleration,width=width,height=height,topspeed=10,
    #                 counter=1000,checkcondition="two",size=size)
    #     movers.append(mover)

    # pl = Plotter(width,height,size=0.1,type="circle",bounds=bounds)
    # pl.set_data(move.next)
    # pl.plotter()

    # liquid = Liquid(0,height/2,width/2,height/2,0.1)
    #
    # air = AirResistance(mass=0.1,unitvector=PVector(0.0001,0))
    # gravity =  Gravity(100)
    # friction = Friction(100,0.03,PVector(-0.03,-0.004))
    # water = WaterResistance(0.01,0.3,PVector(-0.001,-0.01))
    #
    # move.applyForce(air.applyForceWith(move.acc))
    # move.applyForce(gravity.applyForceWith(move.acc))
    # move.applyForce(friction.applyForceWith(move.acc))
    #
    # if isInside(vec=move.loc,l=liquid):
    #     move.applyForce(water.applyForceWith(move.acc))

    pl2 = Plotter(width,height,type="*",bounds=bounds,fill='r',boundary="ABCD",interval=10)

    # pl2.connect()
    # for mover in movers:
    pl2.set_data(move.next)

    pl2.plotter()




if __name__ == '__main__': main()