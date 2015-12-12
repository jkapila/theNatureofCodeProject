import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



class Plotter:
    x = y =0
    def __init__(self,width,height,init_state=[(0.0)],type="line"):

        # self.fig = plt.figure()
        # self.ax1 = self.fig.add_subplot(1,1,1,xlim = (0,600),ylim = (0,400),title = 'test')
        self.w = width
        self.h = height
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], lw=2)
        self.ax.grid()
        self.xdata, self.ydata = [], []
        self.points=[]
        self.points.append(init_state)


    def init(self):
        self.ax.set_ylim(-self.h, self.h)
        self.ax.set_xlim(0, self.w)
        del self.xdata[:]
        del self.ydata[:]
        self.line.set_data(self.xdata, self.ydata)
        return self.line,

    def animate(self,num,dat,line):
        t, y = self.get_data()
        self.xdata.append(t)
        self.ydata.append(y)
        xmin, xmax = self.ax.get_xlim()

        if t >= xmax:
            self.ax.set_xlim(xmin, 2*xmax)
            self.ax.figure.canvas.draw()
        line.set_data(self.xdata, self.ydata)

        return line,

    def set_data(self,func):
        self.func = func

    def get_data(self):
        (x,y) =  self.func()
        return x,y

    def data(self,t=0):
        return self.func

    def onclick(self,event):
        global ix, iy
        ix, iy = event.xdata, event.ydata
        print('x={} y={}'.format(ix,iy))

        # global coords
        self.points.append((ix, iy))

        print(self.points)

        return self.points

    def connect(self):
        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        print(self.cid)

    def disconnect(self):
        self.fig.canvas.mpl_disconnects(self.cid)

    def plotter(self):
        fig = self.fig
        animate = self.animate
        data=self.data
        init = self.init

        ani = animation.FuncAnimation(fig,animate,1000,fargs=(data,self.line),interval=50,blit=True,repeat=False,init_func=init)
        plt.show()

if __name__ == '__main__':

    plotter = Plotter(600,400)

    plotter.plotter()