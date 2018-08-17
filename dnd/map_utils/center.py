from dnd.map_utils import region


class center(object):

    def __init__(self, point, number):
        self.number = number

        self.point = point
        self.water = False
        self.coast = False
        self.biome = ""
        self.elevation = 0
        self.moisture = 0
        self.inregion = region.region

        self.neighbors = []
        self.borders = []
        self.corners = []

        self.river = 0
        self.downslope = object
        self.watershed = object
        self.watershedSize = 0

        self.dedges = []

    def getcoord(self):
        return self.point[0], self.point[1]

    def setRegion(self, reg):
        self.inregion = reg

    def addDedge(self, edge):
        self.dedges.append(edge)

    def addBorder(self, border):
        self.borders.append(border)

    def addCorner(self, corner):
        self.corners.append(corner)

    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)
