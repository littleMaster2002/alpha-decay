import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageSequence
import os
import time

print("Please enter how many Po-211 atoms you wish to start with.")
startingNo = int(input())

PoHalfLife = 0.516

timeLimit = 5
timeInterval = 0.001
Time = np.arange(0, timeLimit, timeInterval)

for i in range(1, Time.size):
    noAtomsNonDecay = startingNo*(0.5**(Time/PoHalfLife))

plt.plot(Time,noAtomsNonDecay)
plt.title("Alpha Decay of Po-211")
plt.xlabel("Time / s")
plt.ylabel("Number of atoms remaining")
plt.pause(1)
plt.show(block=False)

im1 = Image.open('nucleus.gif')
im2 = Image.open('decayedNucleus.gif')
frames = []

number = startingNo

fileCounter = 0
frameCounter = 0
frameMax = 5

for i in range(number):
    while frameCounter <= frameMax:
        for frame in ImageSequence.Iterator(im1):
            frame = frame.copy()
            frames.append(frame)
            frameCounter += 1
    for frame in ImageSequence.Iterator(im2):
        frame = frame.copy()
        frames.append(frame)

    frames[0].save('nucleusCombined{}.gif'.format(fileCounter), save_all=True, append_images=frames[1:],loop=1)
    if fileCounter > 10:
        time.sleep(0.5 * (fileCounter-10))
        os.startfile('nucleusCombined{}.gif'.format(fileCounter))
    else:
        os.startfile('nucleusCombined{}.gif'.format(fileCounter))
    fileCounter += 1
    frameMax = frameMax * 1.2
    frameCounter = 0
    frames = []


