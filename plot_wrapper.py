import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



class Plotter:
    x = y =0
    def __init__(self,width,height,
                 init_state=[(0.0)],
                 boundary = "A",
                 bounds  = [-2, 2, -2, 2],
                 interval = 100,
                 size = 10,
                 type="line",
                 fill = 'b',
                 environment = 'none',
                 allow_multiple= False):

        # self.fig = plt.figure()
        # self.ax1 = self.fig.add_subplot(1,1,1,xlim = (0,600),ylim = (0,400),title = 'test')
        self.w = width
        self.h = height
        self.type = type
        self.boundary = boundary
        self.interval = interval
        self.bounds = bounds
        self.size = size
        self.fill = fill
        self.xdata, self.ydata = [], []
        self.points=[]
        self.points.append(init_state)
        self.environment = environment
        self.allow_multiple = allow_multiple
        self.initialize()

    def initialize(self):

        xlim,ylim = self.boundaries(self.boundary)
        if not self.allow_multiple:
            # if self.type in ['-','--','-.',':','.']:
            #     self.fig_line = plt.figure()
            #     self.ax_line = self.fig_line.add_subplot(xlim=xlim, ylim=ylim)
            #     self.line, = self.ax_line.plot([], [], lw=2)
            #     self.ax_line.grid()
            #     self.type = "line"

            if self.type in ['o','s','p','*','+','x','d','|','_','-','--','-.',':','.']:
                self.fig_circle = plt.figure()
                # self.fig_circle.subplots_adjust(left=0, right=1, bottom=0, top=1)
                self.ax_circle = self.fig_circle.add_subplot(111, aspect='equal', autoscale_on=False,
                                                             xlim=xlim, ylim=ylim)
                 # particles holds the locations of the particles
                self.particles, = self.ax_circle.plot([], [], '{}{}'.format(self.fill,self.type), ms=6)
                # rect is the box edge
                self.rect = plt.Rectangle(self.bounds[::2],self.bounds[1] - self.bounds[0],self.bounds[3] - self.bounds[2],
                         ec='none', lw=2, fc='none')
                self.type = "circle"
            if self.environment != "none":
                if "circle" in self.type: self.fig_circle.add_subplot()
                if "line" in self.type: self.fig_line.add_subplot()

        else:
            pass #todo



    def boundaries(self,quad):
        xlim = ylim = (0,0)
        if "A" in quad:
            xlim =(0,self.w)
            ylim =(0,self.h)

            if "A" in quad and "B" in quad:
                xlim =(-self.w,self.w)
                ylim =(0,self.h)

                if "A" in quad and "B" in quad and "C" in quad and "D" in quad:
                    xlim =(-self.w,self.w)
                    ylim =(-self.h,self.h)

        return xlim,ylim

    def init(self):
        if "line" in self.type:
            self.ax_line.set_ylim(-self.h, self.h)
            self.ax_line.set_xlim(0, self.w)
            del self.xdata[:]
            del self.ydata[:]
            self.line.set_data(self.xdata, self.ydata)
            return self.line,

        if "circle" in self.type:
            self.particles.set_data([], [])
            self.rect.set_edgecolor('green')
            return self.particles, self.rect


    def animate(self,num,dat,line):
        points = self.get_data()
        self.xdata.append(points[:,0].tolist())
        self.ydata.append(points[:,1].tolist())
        print('x={} y={}'.format(self.xdata,self.ydata))
        print('x ={} y ={}'.format(self.x,self.y))
        print('t ={} y ={}'.format(points[:,0],points[:,1]))

        if "line" in self.type:
            xmin, xmax = self.ax_line.get_xlim()
            vec = points[:,0]
            if vec[vec>xmax]:
                self.ax_line.set_xlim(xmin, 2 * xmax)
                self.ax_line.figure.canvas.draw()
            line.set_data(self.xdata, self.ydata)

            return line,

        if "circle" in self.type:
            ms = int(self.fig_circle.dpi * 2 * self.size * self.fig_circle.get_figwidth()
                     / np.diff(self.ax_circle.get_xbound())[0])

            # update pieces of the animation
            self.rect.set_edgecolor('k')
            self.particles.set_data(points[:,0],points[:,1])
            self.particles.set_markersize(ms)
            return self.particles, self.rect


    def set_data(self,func):
        self.func = func

    def get_data(self):

        if len(self.points) > 1:
            points,self.size =  self.func(self.points[len(self.points)-1])
        else:
            points,self.size =  self.func()

        return points

    def data(self,t=0):
        return self.func

    def onclick(self,event):
        ix, iy = event.xdata, event.ydata
        # print('x={} y={}'.format(ix,iy))
        self.points.append((ix, iy))
        return self.points

    def connect(self):
        if "line" in self.type: self.cid = self.fig_line.canvas.mpl_connect('button_press_event', self.onclick)
        if "circle" in self.type: self.cid = self.fig_circle.canvas.mpl_connect('button_press_event', self.onclick)
        print(self.cid)

    def disconnect(self):
        self.fig_line.canvas.mpl_disconnects(self.cid)

    def plotter(self):
        # fig = self.fig_line
        # animate = self.animate
        # data=self.data
        # init = self.init
        if "line" in self.type:
            ani_line = animation.FuncAnimation(self.fig_line,self.animate,1000,fargs=(self.data,self.line),
                                      interval=self.interval,blit=True,repeat=False,init_func=self.init)

        if "circle" in self.type:
            ani_circle =animation.FuncAnimation(self.fig_circle, self.animate,fargs=(self.data,self.particles),
                                                frames=500,interval=self.interval, blit=False, init_func=self.init)
        plt.show()


class LineBuilder:
    def __init__(self):
        pass

class CircleBuilder:
    def __init__(self):
        pass




if __name__ == '__main__':

    plotter = Plotter(600,400)

    plotter.plotter()