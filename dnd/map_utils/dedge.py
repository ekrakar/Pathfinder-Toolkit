from dnd.map_utils import *


class dedge(object):

    def __init__(self, point1, point2, number):
        self.number = number
        self.point1 = point1
        self.point2 = point2
        self.river = 0
