


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class EventHandeler(object):

    def __init__(self,plt_figure,plt_objects,point=[0,0,0,0],**kwargs):
        self.figure = plt_figure
        self.objects = plt_objects
        self.points=point


    def onclick(self,event):
        """
        on the click of mouse
        :param event:
        :return:
        """

        ix, iy = event.xdata, event.ydata
        # print('x={} y={}'.format(ix,iy))
        self.points.append((ix, iy))
        return self.points

    def onmotion(self, event):
        """
        on motion we will move the rect if the mouse is over us
        :param event:
        :return:
        """
        if self.press is None : return
        if event.inaxes != self.rect.axes : return
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        #print 'x0=%f, xpress=%f, event.xdata=%f, dx=%f, x0+dx=%f'%(x0, xpress, event.xdata, dx, x0+dx)
        self.objects.set_x(x0+dx)
        self.objects.set_y(y0+dy)

        self.objects.figure.canvas.draw()

    def onrelease(self, event):
        """
        on release we reset the press data
        :param event:
        :return:
        """
        self.press = None
        self.objects.figure.canvas.draw()

    def connect(self):
        self.cid_bp = self.figure.canvas.mpl_connect('button_press_event', self.onclick)
        self.cid_rp = self.figure.canvas.mpl_connect('button_release_event', self.onrelease)
        self.cid_mn = self.figure.canvas.mpl_connect('motion_notify_event', self.onmotion)
        print('bp = {} rp = {} mn = {}'.format(self.cid_bp, self.cid_rp, self.cid_mn))

    def disconnect(self):
        self.figure.canvas.mpl_disconnects(self.cid_bp)
        self.figure.canvas.mpl_disconnects(self.cid_rp)
        self.figure.canvas.mpl_disconnects(self.cid_mn)