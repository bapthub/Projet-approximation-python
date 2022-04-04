import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set(xlim=(0, 100), ylim=(0, 100))
ax.grid()

coordonnee = []
stop = False

def onClick(event):
    try:
        x, y = event.xdata, event.ydata
        print(x, y)
        coordonnee.append((round(x, 2), round(y, 2)))
        plt.scatter(x, y, color="black", marker="x")
    except:
        print("Please click on the grid !")

def onKey(event):
    global stop
    if (event.key == "enter"):
        stop = True

while True:
    key = fig.canvas.mpl_connect('key_press_event', onKey)
    click = fig.canvas.mpl_connect('button_press_event', onClick)
    plt.pause(1)
    if (stop):
        break

print(coordonnee)