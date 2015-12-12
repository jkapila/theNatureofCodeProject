
"""
here we define wrappers for using matplotlib for animation
"""

from __future__ import (absolute_import, division, print_function, unicode_literals)
import six

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

from vector import PVector

class Animation:

    lock = None
    def __init__(self,vec,figure):
        self.vec =  vec
        self.fig = figure
        self.coords = PVector()
        self.iter = []


    def connect(self):
        # self.motion = self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.point = self.fig.canvas.mpl_connect('button_press_event', self.onclick)

    def disconnect(self):
        self.fig.canvas.mpl_disconnect(self.point)
        # self.fig.canvas.mpl_disconnect(self.motion)

    def on_motion(self, event):
        'on motion we will move the rect if the mouse is over us'
        if Animation.lock is not self:
            return
        if event.inaxes != self.plot.axes: return

    def onclick(self,event):
        self.coords = PVector(x=event.xdata,y=event.ydata)
        return self.coords

    def get_coords(self):
        return self.coords

    def init(self):
        self.plot.set_data([],[])



class Plotting:

    def __init__(self,width,height):
        self.figure = plt.figure()
        ax = self.figure.add_subplot(111)
        self.plot = ax.plot(width,height,lw = 2)

    def get_plot(self):
        return self.plot

    def set_plot(self,vec):
        self.plot = self.axes.plot(vec.x,vec.y)

    def get_figure(self):
        return self.figure

    def print_all(self):
        print(self.figure)
        print(self.axes)
        print(self.plot)

    def plot_start(self):
        plt.show()




















class DraggableRectangle:
    lock = None  # only one can be animated at a time
    def __init__(self, rect):
        self.rect = rect
        self.press = None
        self.background = None

    def connect(self):
        'connect to all the events we need'
        self.cidpress = self.rect.figure.canvas.mpl_connect( 'button_press_event', self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)

    def on_press(self, event):
        'on button press we will see if the mouse is over us and store some data'
        if event.inaxes != self.rect.axes: return
        if DraggableRectangle.lock is not None: return
        contains, attrd = self.rect.contains(event)
        if not contains: return
        print('event contains', self.rect.xy)
        x0, y0 = self.rect.xy
        self.press = x0, y0, event.xdata, event.ydata
        DraggableRectangle.lock = self

        # draw everything but the selected rectangle and store the pixel buffer
        canvas = self.rect.figure.canvas
        axes = self.rect.axes
        self.rect.set_animated(True)
        canvas.draw()
        self.background = canvas.copy_from_bbox(self.rect.axes.bbox)

        # now redraw just the rectangle
        axes.draw_artist(self.rect)

        # and blit just the redrawn area
        canvas.blit(axes.bbox)

    def on_motion(self, event):
        'on motion we will move the rect if the mouse is over us'
        if DraggableRectangle.lock is not self:
            return
        if event.inaxes != self.rect.axes: return
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        self.rect.set_x(x0+dx)
        self.rect.set_y(y0+dy)

        canvas = self.rect.figure.canvas
        axes = self.rect.axes
        # restore the background region
        canvas.restore_region(self.background)

        # redraw just the current rectangle
        axes.draw_artist(self.rect)

        # blit just the redrawn area
        canvas.blit(axes.bbox)

    def on_release(self, event):
        'on release we reset the press data'
        if DraggableRectangle.lock is not self:
            return

        self.press = None
        DraggableRectangle.lock = None

        # turn off the rect animation property and reset the background
        self.rect.set_animated(False)
        self.background = None

        # redraw the full figure
        self.rect.figure.canvas.draw()

    def disconnect(self):
        'disconnect all the stored connection ids'
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)
