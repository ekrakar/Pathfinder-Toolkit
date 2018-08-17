from dnd import BackMapGen
import numpy as np
import cv2
from random import randint


if __name__ == '__main__':
    maps = []
    info = []
    image = np.zeros((3900, 3900, 3), np.float32)
    print("image Made")
    dirs = ["Empty", "East", "South-West", "Empty", (str)(randint(1, 4)) + " Island",
            (str)(randint(1, 3)) + " Island", "Empty", "North", "Empty", (str)(randint(1, 4)) + " Island",
            "South-East", "South-West", "Empty", (str)(randint(1, 3)) + " Island", "South",
            "North-East", "North-West", "Empty", (str)(randint(1, 3)) + " Island", "North",
            (str)(randint(1, 3)) + " Island", (str)(randint(1, 3)) + " Island", (str)(randint(1, 3)) + " Island", (str)(randint(1, 3)) + " Island", (str)(randint(1, 3)) + " Island"]
    for i in dirs:
        print(i)
        map, data = BackMapGen.genMap(i)
        maps.append(map[25:805, 25:805])
        info.append(data)
    xoffset = 0
    yoffset = 0
    for i in maps:
        for x in range(0, 780):
            for y in range(0, 780):
                for z in range(0, 3):
                    image[xoffset * 780 + x, yoffset * 780 + y, z] = i[x, y, z]


        yoffset += 1
        if yoffset >= 5:
            yoffset = 0
            xoffset += 1
    cv2.imwrite('voronoi.jpg', image)
    image = cv2.imread('voronoi.jpg', 3)
    cv2.imshow('Map', image)
    cv2.waitKey(0)
