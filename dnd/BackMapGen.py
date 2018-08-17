from PIL import Image, ImageDraw
from scipy.spatial import Delaunay, Voronoi
import random
from random import randint
from dnd import BackMapDraw
from dnd.map_utils import dataformatter
import numpy as np
from shapely.geometry import Polygon, Point
import cv2

def voronoi(points, shape=(500, 500), size=500, recur=1):
    print(recur)
    vor = Voronoi(points)
    regions = []
    holdregions = []
    for i in vor.regions:
        if -1 in i[:] or i == []:
            regions.append([])
        else:
            hold = []
            check = True
            for y in i:
                x1 = vor.vertices[y, 0]
                y1 = vor.vertices[y, 1]
                if x1 >= 0 and x1 < size and y1 >= 0 and y1 < size:
                    hold.append((x1, y1))
                else:
                    hold.append((x1, y1))
                    check = False
            if recur != 0:
                check = True
            if check:
                regions.append(hold)
            else:
                holdregions.append(hold)
                regions.append([])
    newPoints = []
    newRegions = []
    holdpoints = []
    matrix = np.zeros((size, size), dtype=np.int32)
    matrix.fill(-1)
    x = 0
    for i in points:
        holdpoints.append(i)
        if i[0] >= 0 and i[0] < size and i[1] >= 0 and i[1] < size:
            if matrix[int(i[0]), int(i[1])] == -1:
                matrix[int(i[0]), int(i[1])] = x
        x += 1
    for i in regions:
        if i != []:
            x_min = size
            x_max = 0
            y_min = size
            y_max = 0
            polygon = Polygon(i)
            for x in i:
                if x[0] > x_max:
                    x_max = x[0]
                if x[0] < x_min:
                    x_min = x[0]
                if x[1] > y_max:
                    y_max = x[1]
                if x[1] < y_min:
                    y_min = x[1]
            if x_min >= 0 and x_max < size and y_min >= 0 and y_max < size:
                testregion = matrix[int(x_min): int(x_max), int(y_min): int(y_max)]
                testregion = testregion.flatten()
                z = 0
                search = True
                while search:
                    y = testregion[z]
                    if y != -1:
                        if polygon.contains(Point(points[y])):
                            search = False
                            newPoints.append(points[y])
                            newRegions.append(i)
                            holdpoints.remove(points[y])
                            #print(len(newPoints))
                    z += 1
                    if z == len(testregion):
                        search = False

    if recur > 0:
        for i in holdpoints:
            newPoints.append(i)
        dif = len(newPoints) - len(newRegions)
        for i in range(0, dif):
            newRegions.append([])
        z = 0
        for i in newRegions:
            if i != []:
                polygon = Polygon(i)
                x1, y1 = polygon.centroid.coords[0]
                newPoints[z] = [x1, y1]
                z += 1
        return voronoi(newPoints, shape, size, recur-1)
    else:
        tri = Delaunay(newPoints)
        voroLines = []
        verts = []
        for i in vor.ridge_vertices:
            if i[0] != -1 and i[1] != -1:
                x1 = vor.vertices[i[0], 0]
                y1 = vor.vertices[i[0], 1]
                x2 = vor.vertices[i[1], 0]
                y2 = vor.vertices[i[1], 1]
                hold = [x1, y1, x2, y2]
                check = True
                for x in hold:
                    if x < 0 or x >= size:
                        check = False
                if check:
                    voroLines.append([x1, y1, x2, y2])
        for i in vor.vertices:
            check = True
            for x in i:
                if x < 0 or x >= size:
                    check = False
            if check:
                verts.append(i)
        return voroLines, verts, newPoints, newRegions, tri


def create_image(lines, verts, points, shape):
    image = Image.new('RGB', shape, (255, 255, 255))
    image.save('voronoi.png')

def generate_shape(points, size, dir):
    verts = []
    num = 50
    dist = (int)(size/num)
    offset = dist * (num + 1)
    off = dist * 2
    varience = 12
    if dir == "Full":
        verts = [(0, 0), (size, 0), (size, size), (0, size)]
    elif dir == "Empty":
        verts = [(0, 0), (0, 1), (1, 1)]
    elif dir == "North":
        for i in range(0, (int)(size/num) + 3):
            verts.append([num * (i), 15])
        for i in range(num - 4):
            verts.append([randint(430, 815), randint(off + dist * (i - 1), off + dist * (i + 1))])
        for i in range(num):
            verts.append([randint(offset - dist * (i + 1), offset - dist * (i - 1)), randint(430, 815)])
        for i in range(num - 4):
            verts.append([randint(15, 400), randint(offset - off - dist * (i + 1), offset - off - dist * (i - 1))])
        for i in range(0, len(verts) * 2):
            cur = i
            if cur >= len(verts):
                cur -= len(verts)
            if cur > (int)(size/num):
                prev = cur - 1
                if prev == -1:
                    prev = len(verts) - 1
                if (verts[cur][1] - verts[prev][1]) > varience:
                    verts[cur][1] = verts[prev][1] + randint(0, 2 * varience)
                if (verts[cur][1] - verts[prev][1]) < -varience:
                    verts[cur][1] = verts[prev][1] - randint(0, 2 * varience)
                if (verts[cur][0] - verts[prev][0]) > varience:
                    verts[cur][0] = verts[prev][0] + randint(0, 2 * varience)
                if (verts[cur][0] - verts[prev][0]) < -varience:
                    verts[cur][0] = verts[prev][0] - randint(0, 2 * varience)
    elif dir == "East":
        for i in range(num):
            verts.append([randint(dist * (i - 1), dist * (i + 1)), randint(15, 400)])
        for i in range(0, (int)(size/num) + 1):
            verts.append([815, num * i])
        for i in range(num):
            verts.append([randint(offset - dist * (i + 1), offset - dist * (i - 1)), randint(430, 815)])
        for i in range(num - 4):
            verts.append([randint(15, 400), randint(offset - off - dist * (i + 1), offset - off - dist * (i - 1))])
        for i in range(0, len(verts) * 2):
            cur = i
            if cur >= len(verts):
                cur -= len(verts)
            if cur < num or cur >= num + (int)(size/num) + 1:
                prev = cur - 1
                if prev == -1:
                    prev = len(verts) - 1
                if (verts[cur][1] - verts[prev][1]) > varience:
                    verts[cur][1] = verts[prev][1] + randint(0, 2 * varience)
                if (verts[cur][1] - verts[prev][1]) < -varience:
                    verts[cur][1] = verts[prev][1] - randint(0, 2 * varience)
                if (verts[cur][0] - verts[prev][0]) > varience:
                    verts[cur][0] = verts[prev][0] + randint(0, 2 * varience)
                if (verts[cur][0] - verts[prev][0]) < -varience:
                    verts[cur][0] = verts[prev][0] - randint(0, 2 * varience)
    elif dir == "South":
        for i in range(num):
            verts.append([randint(dist * (i - 1), dist * (i + 1)), randint(15, 400)])
        for i in range(num - 4):
            verts.append([randint(530 + 2 * i, 815 + 2 * i), randint(off + dist * (i - 1), off + dist * (i + 1))])
        for i in range(0, (int)(size/num) + 3):
            verts.append([offset - num * (i - 1), 815])
        for i in range(num - 4):
            verts.append([randint(15, 400), randint(offset - off - dist * (i + 1), offset - off - dist * (i - 1))])
        for i in verts:
            if i[0] > 815:
                i[0] = 815
            if i[1] > 815:
                i[1] = 815
            if i[0] < 15:
                i[0] = 15
            if i[1] < 15:
                i[1] = 15
        for i in range(0, len(verts) * 2):
            cur = i
            if cur >= len(verts):
                cur -= len(verts)
            if cur < 2 * num - 4 or cur >= 2 * num - 4 + (int)(size / num) + 3:
                prev = cur - 1
                if prev == -1:
                    prev = len(verts) - 1
                if (verts[cur][1] - verts[prev][1]) > varience:
                    verts[cur][1] = verts[prev][1] + randint(0, 2 * varience)
                if (verts[cur][1] - verts[prev][1]) < -varience:
                    verts[cur][1] = verts[prev][1] - randint(0, 2 * varience)
                if (verts[cur][0] - verts[prev][0]) > varience:
                    verts[cur][0] = verts[prev][0] + randint(0, 2 * varience)
                if (verts[cur][0] - verts[prev][0]) < -varience:
                    verts[cur][0] = verts[prev][0] - randint(0, 2 * varience)
    elif dir == "West":
        for i in range(num):
            verts.append([randint(dist * (i - 1), dist * (i + 1)), randint(15, 400)])
        for i in range(num - 4):
            verts.append([randint(430, 815), randint(off + dist * (i - 1), off + dist * (i + 1))])
        for i in range(num):
            verts.append([randint(offset - dist * (i + 1), offset - dist * (i - 1)), randint(430, 815)])
        for i in range(0, (int)(size/num) + 2):
            verts.append([15, offset + num - num * i])
        for i in range(0, len(verts) * 2):
            cur = i
            if cur >= len(verts):
                cur -= len(verts)
            if cur < 3 * num - 4:
                prev = cur - 1
                if prev == -1:
                    prev = len(verts) - 1
                if (verts[cur][1] - verts[prev][1]) > varience:
                    verts[cur][1] = verts[prev][1] + randint(0, 2 * varience)
                if (verts[cur][1] - verts[prev][1]) < -varience:
                    verts[cur][1] = verts[prev][1] - randint(0, 2 * varience)
                if (verts[cur][0] - verts[prev][0]) > varience:
                    verts[cur][0] = verts[prev][0] + randint(0, 2 * varience)
                if (verts[cur][0] - verts[prev][0]) < -varience:
                    verts[cur][0] = verts[prev][0] - randint(0, 2 * varience)
    elif dir == "North-East":
        for i in range(0, (int)(size/num) + 3):
            verts.append([num * (i), 15])
        for i in range(0, (int)(size/num) + 1):
            verts.append([815, num * i])
        for i in range(num):
            verts.append([randint(offset - dist * (i + 1), offset - dist * (i - 1)), randint(430, 815)])
        for i in range(num - 4):
            verts.append([randint(15, 400), randint(offset - off - dist * (i + 1), offset - off - dist * (i - 1))])
        for i in range(0, len(verts) * 2):
            cur = i
            if cur >= len(verts):
                cur -= len(verts)
            if cur >= 2 * (int)(size/num) + 4:
                prev = cur - 1
                if prev == -1:
                    prev = len(verts) - 1
                if (verts[cur][1] - verts[prev][1]) > varience:
                    verts[cur][1] = verts[prev][1] + randint(0, 2 * varience)
                if (verts[cur][1] - verts[prev][1]) < -varience:
                    verts[cur][1] = verts[prev][1] - randint(0, 2 * varience)
                if (verts[cur][0] - verts[prev][0]) > varience:
                    verts[cur][0] = verts[prev][0] + randint(0, 2 * varience)
                if (verts[cur][0] - verts[prev][0]) < -varience:
                    verts[cur][0] = verts[prev][0] - randint(0, 2 * varience)
    elif dir == "North-West":
        for i in range(0, (int)(size/num) + 3):
            verts.append([num * i, 15])
        for i in range(num - 4):
            verts.append([randint(430, 815), randint(off + dist * (i - 1), off + dist * (i + 1))])
        for i in range(num):
            verts.append([randint(offset - dist * (i + 1), offset - dist * (i - 1)), randint(430, 815)])
        for i in range(0, (int)(size/num) + 2):
            verts.append([15, offset + num - num * i])
        for i in range(0, len(verts) * 2):
            cur = i
            if cur >= len(verts):
                cur -= len(verts)
            if cur >= (int)(size/num) + 2 and cur < len(verts) - (int)(size/num) - 2:
                prev = cur - 1
                if prev == -1:
                    prev = len(verts) - 1
                if (verts[cur][1] - verts[prev][1]) > varience:
                    verts[cur][1] = verts[prev][1] + randint(0, 2 * varience)
                if (verts[cur][1] - verts[prev][1]) < -varience:
                    verts[cur][1] = verts[prev][1] - randint(0, 2 * varience)
                if (verts[cur][0] - verts[prev][0]) > varience:
                    verts[cur][0] = verts[prev][0] + randint(0, 2 * varience)
                if (verts[cur][0] - verts[prev][0]) < -varience:
                    verts[cur][0] = verts[prev][0] - randint(0, 2 * varience)
    elif dir == "South-East":
        for i in range(num):
            verts.append([randint(dist * (i - 1), dist * (i + 1)), randint(15, 400)])
        for i in range(0, (int)(size/num) + 1):
            verts.append([815, num * i])
        for i in range(0, (int)(size/num) + 3):
            verts.append([offset - num * (i - 1), 815])
        for i in range(num - 4):
            verts.append([randint(15, 400), randint(offset - off - dist * (i + 1), offset - off - dist * (i - 1))])
        for i in range(0, len(verts) * 2):
            cur = i
            if cur >= len(verts):
                cur -= len(verts)
            if cur < num or cur >= num + 2 * (int)(size/num) + 4:
                prev = cur - 1
                if prev == -1:
                    prev = len(verts) - 1
                if (verts[cur][1] - verts[prev][1]) > varience:
                    verts[cur][1] = verts[prev][1] + randint(0, 2 * varience)
                if (verts[cur][1] - verts[prev][1]) < -varience:
                    verts[cur][1] = verts[prev][1] - randint(0, 2 * varience)
                if (verts[cur][0] - verts[prev][0]) > varience:
                    verts[cur][0] = verts[prev][0] + randint(0, 2 * varience)
                if (verts[cur][0] - verts[prev][0]) < -varience:
                    verts[cur][0] = verts[prev][0] - randint(0, 2 * varience)
    elif dir == "South-West":
        for i in range(num):
            verts.append([randint(dist * (i - 1), dist * (i + 1)), randint(15, 400)])
        for i in range(num - 4):
            verts.append([randint(430, 815), randint(off + dist * (i - 1), off + dist * (i + 1))])
        for i in range(0, (int)(size/num) + 3):
            verts.append([offset - num * (i - 1), 815])
        for i in range(0, (int)(size/num) + 3):
            verts.append([15, offset + num - num * i])
        for i in range(0, len(verts) * 2):
            cur = i
            if cur >= len(verts):
                cur -= len(verts)
            if cur < 2 * num - 4:
                prev = cur - 1
                if prev == -1:
                    prev = len(verts) - 1
                if (verts[cur][1] - verts[prev][1]) > varience:
                    verts[cur][1] = verts[prev][1] + randint(0, 2 * varience)
                if (verts[cur][1] - verts[prev][1]) < -varience:
                    verts[cur][1] = verts[prev][1] - randint(0, 2 * varience)
                if (verts[cur][0] - verts[prev][0]) > varience:
                    verts[cur][0] = verts[prev][0] + randint(0, 2 * varience)
                if (verts[cur][0] - verts[prev][0]) < -varience:
                    verts[cur][0] = verts[prev][0] - randint(0, 2 * varience)
    elif dir == "1 Island":
        for i in range(num):
            verts.append([randint(dist * (i - 1), dist * (i + 1)), randint(15, 400)])
        for i in range(num - 4):
            verts.append([randint(430, 815), randint(off + dist * (i - 1), off + dist * (i + 1))])
        for i in range(num):
            verts.append([randint(offset - dist * (i + 1), offset - dist * (i - 1)), randint(430, 815)])
        for i in range(num - 4):
            verts.append([randint(15, 400), randint(offset - off - dist * (i + 1), offset - off - dist * (i - 1))])
        for i in range(0, len(verts) * 2):
            cur = i
            if cur >= len(verts):
                cur -= len(verts)
            prev = cur - 1
            if prev == -1:
                prev = len(verts) - 1
            if (verts[cur][1] - verts[prev][1]) > varience:
                verts[cur][1] = verts[prev][1] + randint(0, 2 * varience)
            if (verts[cur][1] - verts[prev][1]) < -varience:
                verts[cur][1] = verts[prev][1] - randint(0, 2 * varience)
            if (verts[cur][0] - verts[prev][0]) > varience:
                verts[cur][0] = verts[prev][0] + randint(0, 2 * varience)
            if (verts[cur][0] - verts[prev][0]) < -varience:
                verts[cur][0] = verts[prev][0] - randint(0, 2 * varience)
    elif dir == "2 Island":
        first = []
        second = []
        x1 = randint(0, 500)
        y1 = randint(0, 500)
        x2 = randint(0, 500)
        y2 = randint(0, 500)
        for i in range(num):
            verts.append([randint(dist * (i - 1), dist * (i + 1)), randint(15, 400)])
        for i in range(num - 4):
            verts.append([randint(430, 815), randint(off + dist * (i - 1), off + dist * (i + 1))])
        for i in range(num):
            verts.append([randint(offset - dist * (i + 1), offset - dist * (i - 1)), randint(430, 815)])
        for i in range(num - 4):
            verts.append([randint(15, 400), randint(offset - off - dist * (i + 1), offset - off - dist * (i - 1))])
        for i in range(0, len(verts) * 2):
            cur = i
            if cur >= len(verts):
                cur -= len(verts)
            prev = cur - 1
            if prev == -1:
                prev = len(verts) - 1
            if (verts[cur][1] - verts[prev][1]) > varience:
                verts[cur][1] = verts[prev][1] + randint(0, 2 * varience)
            if (verts[cur][1] - verts[prev][1]) < -varience:
                verts[cur][1] = verts[prev][1] - randint(0, 2 * varience)
            if (verts[cur][0] - verts[prev][0]) > varience:
                verts[cur][0] = verts[prev][0] + randint(0, 2 * varience)
            if (verts[cur][0] - verts[prev][0]) < -varience:
                verts[cur][0] = verts[prev][0] - randint(0, 2 * varience)
        for i in verts:
            first.append([(int)(i[0] / 2) + x1, (int)(i[1] / 2) + y1])
        verts = []
        for i in range(num):
            verts.append([randint(dist * (i - 1), dist * (i + 1)), randint(15, 400)])
        for i in range(num - 4):
            verts.append([randint(430, 815), randint(off + dist * (i - 1), off + dist * (i + 1))])
        for i in range(num):
            verts.append([randint(offset - dist * (i + 1), offset - dist * (i - 1)), randint(430, 815)])
        for i in range(num - 4):
            verts.append([randint(15, 400), randint(offset - off - dist * (i + 1), offset - off - dist * (i - 1))])
        for i in range(0, len(verts) * 2):
            cur = i
            if cur >= len(verts):
                cur -= len(verts)
            prev = cur - 1
            if prev == -1:
                prev = len(verts) - 1
            if (verts[cur][1] - verts[prev][1]) > varience:
                verts[cur][1] = verts[prev][1] + randint(0, 2 * varience)
            if (verts[cur][1] - verts[prev][1]) < -varience:
                verts[cur][1] = verts[prev][1] - randint(0, 2 * varience)
            if (verts[cur][0] - verts[prev][0]) > varience:
                verts[cur][0] = verts[prev][0] + randint(0, 2 * varience)
            if (verts[cur][0] - verts[prev][0]) < -varience:
                verts[cur][0] = verts[prev][0] - randint(0, 2 * varience)
        for i in verts:
            second.append([(int)(i[0] / 2) + x2, (int)(i[1] / 2) + y2])
    elif dir == "3 Island":
        first = []
        second = []
        third = []
        empty = randint(0, 4)
        x1 = randint(0, 535)
        y1 = randint(0, 535)
        x2 = randint(0, 535)
        y2 = randint(0, 535)
        x3 = randint(0, 535)
        y3 = randint(0, 535)
        for i in range(num):
            verts.append([randint(dist * (i - 1), dist * (i + 1)), randint(15, 400)])
        for i in range(num - 4):
            verts.append([randint(430, 815), randint(off + dist * (i - 1), off + dist * (i + 1))])
        for i in range(num):
            verts.append([randint(offset - dist * (i + 1), offset - dist * (i - 1)), randint(430, 815)])
        for i in range(num - 4):
            verts.append([randint(15, 400), randint(offset - off - dist * (i + 1), offset - off - dist * (i - 1))])
        for i in range(0, len(verts) * 2):
            cur = i
            if cur >= len(verts):
                cur -= len(verts)
            prev = cur - 1
            if prev == -1:
                prev = len(verts) - 1
            if (verts[cur][1] - verts[prev][1]) > varience:
                verts[cur][1] = verts[prev][1] + randint(0, 2 * varience)
            if (verts[cur][1] - verts[prev][1]) < -varience:
                verts[cur][1] = verts[prev][1] - randint(0, 2 * varience)
            if (verts[cur][0] - verts[prev][0]) > varience:
                verts[cur][0] = verts[prev][0] + randint(0, 2 * varience)
            if (verts[cur][0] - verts[prev][0]) < -varience:
                verts[cur][0] = verts[prev][0] - randint(0, 2 * varience)
        for i in verts:
            first.append([(int)(i[0] / 3) + x1, (int)(i[1] / 3) + y1])
        verts = []
        for i in range(num):
            verts.append([randint(dist * (i - 1), dist * (i + 1)), randint(15, 400)])
        for i in range(num - 4):
            verts.append([randint(430, 815), randint(off + dist * (i - 1), off + dist * (i + 1))])
        for i in range(num):
            verts.append([randint(offset - dist * (i + 1), offset - dist * (i - 1)), randint(430, 815)])
        for i in range(num - 4):
            verts.append([randint(15, 400), randint(offset - off - dist * (i + 1), offset - off - dist * (i - 1))])
        for i in range(0, len(verts) * 2):
            cur = i
            if cur >= len(verts):
                cur -= len(verts)
            prev = cur - 1
            if prev == -1:
                prev = len(verts) - 1
            if (verts[cur][1] - verts[prev][1]) > varience:
                verts[cur][1] = verts[prev][1] + randint(0, 2 * varience)
            if (verts[cur][1] - verts[prev][1]) < -varience:
                verts[cur][1] = verts[prev][1] - randint(0, 2 * varience)
            if (verts[cur][0] - verts[prev][0]) > varience:
                verts[cur][0] = verts[prev][0] + randint(0, 2 * varience)
            if (verts[cur][0] - verts[prev][0]) < -varience:
                verts[cur][0] = verts[prev][0] - randint(0, 2 * varience)
        for i in verts:
            second.append([(int)(i[0] / 3) + x2, (int)(i[1] / 3) + y2])
        verts = []
        for i in range(num):
            verts.append([randint(dist * (i - 1), dist * (i + 1)), randint(15, 400)])
        for i in range(num - 4):
            verts.append([randint(430, 815), randint(off + dist * (i - 1), off + dist * (i + 1))])
        for i in range(num):
            verts.append([randint(offset - dist * (i + 1), offset - dist * (i - 1)), randint(430, 815)])
        for i in range(num - 4):
            verts.append([randint(15, 400), randint(offset - off - dist * (i + 1), offset - off - dist * (i - 1))])
        for i in range(0, len(verts) * 2):
            cur = i
            if cur >= len(verts):
                cur -= len(verts)
            prev = cur - 1
            if prev == -1:
                prev = len(verts) - 1
            if (verts[cur][1] - verts[prev][1]) > varience:
                verts[cur][1] = verts[prev][1] + randint(0, 2 * varience)
            if (verts[cur][1] - verts[prev][1]) < -varience:
                verts[cur][1] = verts[prev][1] - randint(0, 2 * varience)
            if (verts[cur][0] - verts[prev][0]) > varience:
                verts[cur][0] = verts[prev][0] + randint(0, 2 * varience)
            if (verts[cur][0] - verts[prev][0]) < -varience:
                verts[cur][0] = verts[prev][0] - randint(0, 2 * varience)
        for i in verts:
            third.append([(int)(i[0] / 3) + x3, (int)(i[1] / 3) + y3])
    else:
        for i in range(num):
            verts.append([randint(dist * (i - 1), dist * (i + 1)), randint(15, 400)])
        for i in range(num - 4):
            verts.append([randint(430, 815), randint(off + dist * (i - 1), off + dist * (i + 1))])
        for i in range(num):
            verts.append([randint(offset - dist * (i + 1), offset - dist * (i - 1)), randint(430, 815)])
        for i in range(num - 4):
            verts.append([randint(15, 400), randint(offset - off - dist * (i + 1), offset - off - dist * (i - 1))])
        for i in range(0, len(verts) * 2):
            cur = i
            if cur >= len(verts):
                cur -= len(verts)
            prev = cur - 1
            if prev == -1:
                prev = len(verts) - 1
            if (verts[cur][1] - verts[prev][1]) > varience:
                verts[cur][1] = verts[prev][1] + randint(0, 2 * varience)
            if (verts[cur][1] - verts[prev][1]) < -varience:
                verts[cur][1] = verts[prev][1] - randint(0, 2 * varience)
            if (verts[cur][0] - verts[prev][0]) > varience:
                verts[cur][0] = verts[prev][0] + randint(0, 2 * varience)
            if (verts[cur][0] - verts[prev][0]) < -varience:
                verts[cur][0] = verts[prev][0] - randint(0, 2 * varience)
    if dir == "2 Island":
        polygon = Polygon(first)
        for i in points:
            if polygon.contains(Point(i.getcoord())):
                i.inregion.ocean = False
        polygon = Polygon(second)
        for i in points:
            if polygon.contains(Point(i.getcoord())):
                i.inregion.ocean = False
    elif dir == "3 Island":
        polygon = Polygon(first)
        for i in points:
            if polygon.contains(Point(i.getcoord())):
                i.inregion.ocean = False
        polygon = Polygon(second)
        for i in points:
            if polygon.contains(Point(i.getcoord())):
                i.inregion.ocean = False
        polygon = Polygon(third)
        for i in points:
            if polygon.contains(Point(i.getcoord())):
                i.inregion.ocean = False
    else:
        polygon = Polygon(verts)
        for i in points:
            if polygon.contains(Point(i.getcoord())):
                i.inregion.ocean = False

def genMap(dir):
    points = []
    size = 830
    mod = 6
    modif = mod/3
    for i in range(1, size, mod):
        for x in range(1, size, mod):
            points.append([i + random.uniform(-modif, modif), x + random.uniform(-modif, modif)])
    voroLines, verts, points, newRegions, tri = voronoi(points, (size+1, size+1), size)
    tris = []
    for i in tri.simplices:
        hold = []
        for x in i:
            hold.append(tri.points[x])
        tris.append(hold)
    voroRegions, centers, corners, dEdges, vEdges = dataformatter.create_data(points, newRegions, voroLines, tris, verts, size)
    create_image(voroLines, verts, points, (size, size))
    generate_shape(centers, size, dir)
    mapImage = BackMapDraw.MapDraw('voronoi.png')
    mapImage.setMapColor(size, (176, 164, 46))
    mapImage.drawPolys(voroRegions, (42, 115, 12), size)
    #mapImage.drawLines(voroLines, (0, 0, 0))
    image = mapImage.getImage()
    return image, [voroRegions, centers, corners, dEdges, vEdges]

if __name__ == '__main__':
    image, data = genMap("South")
    cv2.imwrite('voronoi.png', image)
    image = cv2.imread('voronoi.png', 3)
    cv2.imshow('Map', image)
    cv2.waitKey(0)
