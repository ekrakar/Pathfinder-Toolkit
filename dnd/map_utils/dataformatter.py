import numpy as np
from dnd.map_utils import region, corner, center, dedge, vedge
from collections import Counter


def create_data(pointarr, regionarr, linearr, triarr, verticearr, size):
    mapobjs = np.empty([size, size], dtype=object)
    regionsarr = []
    x = 0
    for i in regionarr:
        regionsarr.append(region.region(i, x))
        x += 1
    print('regions made')
    pointsarr = []
    x = 0
    for i in pointarr:
        pointsarr.append(center.center(i, x))
        mapobjs[int(i[0]), int(i[1])] = pointsarr[x]
        x += 1
    print('centers made')
    cornersarr = []
    x = 0
    for i in verticearr:
        cornersarr.append(corner.corner(i, x))
        mapobjs[int(i[0]), int(i[1])] = cornersarr[x]
        x += 1
    print('corners made')
    vedges = []
    x = 0
    for i in linearr:
        vedges.append(vedge.vedge(mapobjs[int(i[0]), int(i[1])], mapobjs[int(i[2]), int(i[3])], x))
        mapobjs[int(i[0]), int(i[1])].addProtrudes(vedges[x])
        mapobjs[int(i[2]), int(i[3])].addProtrudes(vedges[x])
        x += 1
    print('vedges done')
    hold = []

    for i in triarr:
        hold.append([i[0], i[1]])
        hold.append([i[0], i[2]])
        hold.append([i[1], i[2]])
    dedges = []
    x = 0
    for i in hold:
        if mapobjs[int(i[0][0]), int(i[0][1])].dedges == []:
            dedges.append(dedge.dedge(mapobjs[int(i[0][0]), int(i[0][1])], mapobjs[int(i[1][0]), int(i[1][1])], x))
            mapobjs[int(i[0][0]), int(i[0][1])].addDedge(dedges[x])
            mapobjs[int(i[1][0]), int(i[1][1])].addDedge(dedges[x])
            x += 1
        else:
            valid = True
            for y in mapobjs[int(i[0][0]), int(i[0][1])].dedges:
                if (y.point1 == mapobjs[int(i[0][0]), int(i[0][1])] and y.point2 == mapobjs[int(i[1][0]), int(i[1][1])]) or (y.point2 == mapobjs[int(i[0][0]), int(i[0][1])] and y.point1 == mapobjs[int(i[1][0]), int(i[1][1])]):
                    valid = False
            if valid:
                dedges.append(dedge.dedge(mapobjs[int(i[0][0]), int(i[0][1])], mapobjs[int(i[1][0]), int(i[1][1])], x))
                mapobjs[int(i[0][0]), int(i[0][1])].addDedge(dedges[x])
                mapobjs[int(i[1][0]), int(i[1][1])].addDedge(dedges[x])
                x += 1
    print('dedges done')
    tempreg = []
    for i in regionsarr:
        tempreg.append(i)
    for i in pointsarr:
        notfound = True
        x = 0
        while notfound:
            found = tempreg[x].contain(i)
            if found:
                i.setRegion(tempreg[x])
                hold = []
                for y in i.inregion.points:
                    i.addCorner(mapobjs[int(y[0]), int(y[1])])
                    hold.append(mapobjs[int(y[0]), int(y[1])])
                holdedges = []
                for y in hold:
                    for z in y.protrudes:
                        holdedges.append(z)
                for y in holdedges:
                    if holdedges.count(y) == 2 and i.borders.count(y) == 0:
                        i.addBorder(y)
                        y.addCenter(i)
                tempreg.remove(tempreg[x])
                notfound = False
            x += 1
    print('regions center.borders and center.corners found')
    for i in pointsarr:
        hold = []
        for x in i.dedges:
            hold.append(x.point1)
            hold.append(x.point2)
        for x in hold:
            if x.point[0] == i.point[0] and x.point[1] == i.point[1]:
                a = 1
            else:
                i.addNeighbor(x)
    print('neighbors found')
    for i in cornersarr:
        hold = []
        mids = []
        for x in i.protrudes:
            hold.append(x.point1)
            hold.append(x.point2)
            for y in x.centers:
                mids.append(y)
        for x in mids:
            if i.touches == []:
                i.addTouch(x)
            else:
                valid = True
                for y in i.touches:
                    if x.number == y.number:
                        valid = False
                if valid:
                    i.addTouch(x)
        for x in hold:
            if x.point[0] == i.point[0] and x.point[1] == i.point[1]:
                a = 1
            else:
                i.addAdjacent(x)
    print('adjacent and touches found')
    return regionsarr, pointsarr, cornersarr, dedges, vedges





