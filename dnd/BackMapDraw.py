import cv2
import numpy as np

class MapDraw(object):

    def __init__(self, imgName):
        self.img = cv2.imread(imgName, 3)

    def drawLines(self, lines, color):
        for i in lines:
            cv2.line(self.img, (int(i[0]), int(i[1])), (int(i[2]), int(i[3])), color)
        #self.show()

    def drawPolys(self, polys, color, size):
        for i in polys:
            if i.ocean:
                color = (176, 164, 46)
            else:
                color = (42, 115, 12)
            length = len(i.points)
            poly = np.zeros((length, 2), dtype=np.int32)
            for x in range(0, length):
                x1, y1 = i.points[x]
                poly[x] = [x1, y1]
            cv2.fillConvexPoly(self.img, poly, color)

    def setMapColor(self, size, color):
        cv2.rectangle(self.img, (0, 0), (size-1, size-1), color, -1)

    def show(self):
        cv2.imshow('Map', self.img)
        cv2.waitKey(0)

    def getImage(self):
        return self.img
