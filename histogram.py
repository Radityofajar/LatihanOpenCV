import cv2
import matplotlib.pyplot as plt
import numpy as np

imgDEF = cv2.imread("hotspot3.png")

colors = ('b', 'g', 'r')

hist = {}
for i, col in enumerate(colors):
    hist[i] = cv2.calcHist([imgDEF], [i], None, [256], [1, 256])
    plt.plot(hist[i], color=col)

blue = hist[0]
green = hist[1]
red = hist[2]

ahist = (hist[0] + hist[1] + hist[2]) / 3

meanb = np.mean(blue)
stdb = np.std(hist[0])

meang = np.mean(green).item()
stdg = np.std(hist[1])

meanr = np.mean(hist[2])
stdr = np.std(hist[2])


mean = np.mean(ahist).item()
std = np.std(ahist).item()
print ("Mean = {:.1f}, standard deviation = {:.1f}".format(mean, std))
#print('Mean = ' + str(meanb) + ' standard deviation = ' + str(stdb))
#print('Mean = ' + str(meang) + ' standard deviation = ' + str(stdg))
#print('Mean = ' + str(meanr) + ' standard deviation = ' + str(stdr))
print ("Mean = {:.1f}, standard deviation = {:.1f}".format(meanb, stdb))
print ("Mean = {:.1f}, standard deviation = {:.1f}".format(meang, stdg))
print ("Mean = {:.1f}, standard deviation = {:.1f}".format(meanr, stdr))

plt.plot(ahist, color='m')
plt.show()