

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle,Rectangle
import time



array = [[1,2],[2,3],[3,6],[4,9],[5,4],[6,7],[7,7],[8,4],[9,3],[10,7]]
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1,xlim = (0,600),ylim = (0,400),title = 'test')
coords=[]
coords.append((20,20))
a=[]
counter = 1
# cir = Circle(xy=,radius=,animate=True)

def animateold(i):

    global array

    xar = []
    yar = []
    for l in range(i):
        if i <= len(array):
            x,y = array[l]
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar,yar)


def animate(i):

    # global array

    xar = []
    yar = []
    print('(x,y)={} len{}'.format(coords,len(coords)))
    for l in range(len(coords)):
        (x,y) = coords[l]
        print('x={} y={}'.format(x,y))
        xar.append(int(x))
        yar.append(int(y))

    # ax1.clear()
    ax1.plot(xar,yar,'bo-')

def animate_circle(i):
    (x,y) = coords[len(coords)-1]
    print('(x,y)={} len{}'.format(coords[len(coords)-1],len(coords)))

    global a

    if a == coords[len(coords)-1]:
        global counter
        cir = Circle(xy=(x,y),radius=counter)
        fig.draw(cir)
        counter+=1
    else:
        a = coords[len(coords)-1]

    ax1.plot(x,y,'bo-')


def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    print('x={} y={}'.format(ix,iy))

    # global coords
    coords.append((ix, iy))

    print(coords)

    if len(coords) == 10:
        fig.canvas.mpl_disconnect(cid)

    return coords

cid = fig.canvas.mpl_connect('button_press_event', onclick)
print(cid)
ani = animation.FuncAnimation(fig,animate,interval = 1000)
plt.show()

# def main():
#
#
#
#
#
#
# if __name__ == '__main__':main()