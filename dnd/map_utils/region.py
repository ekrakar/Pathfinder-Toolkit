from dnd.map_utils import *
from shapely.geometry import Polygon, Point


class region(object):

    def __init__(self, points, number):
        self.number = number
        self.points = points
        self.ocean = True

    def contain(self, point):
        polygon = Polygon(self.points)
        return polygon.contains(Point(point.getcoord()))
