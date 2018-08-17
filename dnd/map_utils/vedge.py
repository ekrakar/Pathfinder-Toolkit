from dnd.map_utils import *


class vedge(object):

    def __init__(self, point1, point2, number):
        self.number = number
        self.point1 = point1
        self.point2 = point2
        self.centers = []
        self.midpoint = [0, 0]

    def addCenter(self, point):
        self.centers.append(point)