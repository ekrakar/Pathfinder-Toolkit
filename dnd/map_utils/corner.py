from dnd.map_utils import *


class corner(object):

    def __init__(self, point, number):
        self.number = number
        self.point = point
        self.ocean = False
        self.water = False
        self.coast = False
        self.elevation = 0
        self.moisture = 0

        self.touches = []
        self.protrudes = []
        self.adjacent = []

        self.river = 0
        self.downslope = object
        self.watershed = object
        self.watershedSize = 0

    def getcoord(self):
        return self.point[0], self.point[1]

    def setRegion(self, reg):
        self.inregion = reg

    def addTouch(self, center):
        self.touches.append(center)

    def addProtrudes(self, edge):
        self.protrudes.append(edge)

    def addAdjacent(self, point):
        self.adjacent.append(point)
