import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Plotter:

    fig = plt.figure()


    def __init__(self, width, height,
                 boundary="A", bounds=[-2, 2, -2, 2],
                 interval=100, type="o", fill='b', environment='none', title="The Nature of Code"):
        """

        :param width:
        :param height:
        :param boundary:
        :param bounds:
        :param interval:
        :param type:
        :param fill:
        :param environment:
        :param title:
        :return: Plotter object
        """

        self.w = width
        self.h = height
        self.type = type
        self.boundary = boundary
        self.interval = interval
        self.bounds = bounds
        self.size = 0
        self.fill = fill
        self.xdata, self.ydata = [], []
        self.points = []
        self.press = None
        self.environment = environment
        self.initialize()

    def initialize(self):

        xlim, ylim = self.boundaries(self.boundary)

        if self.type in ['o', 's', 'p', '*', '+', 'x', 'd', '|', '_', '-', '--', '-.', ':', '.']:

            # self.fig_circle.subplots_adjust(left=0, right=1, bottom=0, top=1)
            self.ax = Plotter.fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=xlim, ylim=ylim)

            # particles holds the locations of the particles
            self.objects, = self.ax.plot([], [], '{}{}'.format(self.fill, self.type), ms=6)

            # rect is the box edge
            self.rect = plt.Rectangle(self.bounds[::2],
                                      self.bounds[1] - self.bounds[0],
                                      self.bounds[3] - self.bounds[2],
                                      ec='none', lw=2, fc='none')

        if self.environment != "none":
            pass  #todo

    def boundaries(self, quad):
        xlim = ylim = (0, 0)
        if "A" in quad and "B" in quad and "C" in quad and "D" in quad:  # this is all quadrant
            xlim = (-self.w, self.w)
            ylim = (-self.h, self.h)

        elif  "A" in quad and "B" in quad and ("C" in quad or "D" in quad):  # this is not possible hence making all quadrant
            xlim = (-self.w, self.w)
            ylim = (-self.h, self.h)

        elif "A" in quad and "B" in quad:  # this is first and second quadrant
            xlim = (-self.w, self.w)
            ylim = (0, self.h)

        elif "A" in quad and "D" in quad:  # this is first and fourth quadrant
            xlim = (0, self.w)
            ylim = (-self.h, self.h)

        elif "A" in quad:  # this is first quadrant only
            xlim = (0, self.w)
            ylim = (0, self.h)

        elif "B" in quad:  # this is second quadrant only
            xlim = (-self.w, 0)
            ylim = (0, self.h)

        elif "C" in quad:  # this is third quadrant only
            xlim = (-self.w, 0)
            ylim = (-self.h, 0)

        elif "D" in quad:  # this is fourth quadrant only
            xlim = (0, self.w)
            ylim = (-self.h, 0)

        return xlim, ylim

    def init(self):

        del self.xdata[:]
        del self.ydata[:]
        self.objects.set_data([], [])
        self.rect.set_edgecolor('green')
        return self.objects, self.rect

    def animate(self, num, data, object):

        points = self.get_data()
        self.xdata.append(points[:, 0].tolist())
        self.ydata.append(points[:, 1].tolist())

        print('num = {} data = {} line = {}'.format(num, data, object))
        # print('x={} y={}'.format(self.xdata,self.ydata))
        # print('x ={} y ={}'.format(self.x,self.y))
        # print('t ={} y ={}'.format(points[:,0],points[:,1]))

        xmin, xmax = self.ax.get_xlim()
        vec = points[:, 0]
        if vec[vec > xmax]:
            self.ax.set_xlim(xmin, 2 * xmax)
            self.ax.figure.canvas.draw()

        ms = int(self.fig.dpi * 2 * self.size * self.fig.get_figwidth()
                 / np.diff(self.ax.get_xbound())[0])

        # update pieces of the animation
        self.rect.set_edgecolor('k')
        self.objects.set_data(points[:, 0], points[:, 1])
        self.objects.set_markersize(ms)
        return self.objects, self.rect

    def set_data(self,func):
        self.func = func

    def get_data(self):
        if len(self.points) > 1:
            points, self.size = self.func(self.points[len(self.points)-1])
        else:
            points, self.size = self.func()
        return points

    def data(self,t=0):
        return self.func

    def plotter(self):

        anim = animation.FuncAnimation(self.fig, self.animate, fargs=(self.data, self.objects),frames=500,
                                       interval=self.interval, blit=False, init_func=self.init)
        plt.show()