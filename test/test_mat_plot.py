

"""
Testing Matplotlib animation to make processing like objects.

"""

import matplotlib.pyplot as plt
import numpy as np

from test.matwrap import DraggableRectangle


def main():

    # pl = Plotting(600,400)
    # pl.print_all()
    # dr = []
    # for i in range(10):
    #     an = Animation("",pl.get_figure())
    #     an.connect()
    #     cor =an.get_coords()
    #     pl.set_plot(cor)
    #     dr.append(cor)
    #
    #     print(cor.get())
    #
    # pl.plot_start()


    fig = plt.figure()
    ax = fig.add_subplot(111)
    rects = ax.bar(range(10), 20*np.random.rand(10))
    drs = []
    for rect in rects:
        dr = DraggableRectangle(rect)
        dr.connect()
        drs.append(dr)

    plt.show()

    # #method 1
    # fig, ax = plt.subplots()
    #
    # x = np.arange(0, 2*np.pi, 0.01)
    # line, = ax.plot(x, np.sin(x))
    #
    #
    # def animate(i):
    #     line.set_ydata(np.sin(x + i/10.0))  # update the data
    #     return line,
    #
    #
    # # Init only required for blitting to give a clean slate.
    # def init():
    #     line.set_ydata(np.ma.array(x, mask=True))
    #     return line,
    #
    # ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
    #                           interval=25, blit=True)

    # #method 2
    # fig = plt.figure()
    # ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
    # line, = ax.plot([], [], lw=2)
    #
    # # initialization function: plot the background of each frame
    # def init():
    #     line.set_data([], [])
    #     return line,
    #
    # # animation function.  This is called sequentially
    # def animate(i):
    #     x = np.linspace(0, 2, 1000)
    #     y = np.sin(2 * np.pi * (x - 0.01 * i))
    #     line.set_data(x, y)
    #     return line,
    #
    # # call the animator.  blit=True means only re-draw the parts that have changed.
    # anim = animation.FuncAnimation(fig, animate, init_func=init,frames=200, interval=20, blit=True)

    #method to get clicks / coordiantes form plot
    # x = np.arange(-10,10)
    # y = x**2

    # x = 600
    # y = 400
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.plot(x,y)
    #
    # coords = []
    #
    # def onclick(event):
    #     global ix, iy
    #     ix, iy = event.xdata, event.ydata
    #     print 'x = %d, y = %d'%(ix, iy)
    #
    #     # global coords
    #     coords.append((ix, iy))
    #
    #     if len(coords) == 10:
    #         fig.canvas.mpl_disconnect(cid)
    #
    #     return coords
    #
    # cid = fig.canvas.mpl_connect('button_press_event', onclick)
    #
    # plt.show()


    # Method to draw Rectangle by drag
    # draggable rectangle with the animation blit techniques; see


if __name__ == '__main__': main()