import math
import numpy as np 

#convert single decimal number to radiants
def degToRad(x):
    PI = 3.141592
    deg = int(x)
    mina = x-deg
    rad= PI * (deg + 5.0 * mina/3.0) / 180
    return rad

#input point in format (name, lat, long) convert lat e long to rad
def convertPointToRad(point):
    assert len(point)==3
    a=degToRad(point[1])
    b=degToRad(point[2])
    return (point[0], a, b)

#input point in format (name, lat, long)
def calcDistGeo(pointa, pointb):
    assert len(pointa)==3
    assert len(pointb)==3

    RRR = 6378.388
    q1 = math.cos( pointa[2] - pointb[2] )
    q2 = math.cos( pointa[1] - pointb[1] )
    q3 = math.cos( pointa[1] + pointb[1] )
    dij = int( RRR * math.acos( 0.5*((1.0+q1)*q2 - (1.0-q1)*q3) ) + 1.0)

    return dij

#CREATE MATRIX OF DISTANCES GEO
#input array of coordinates 
#output matrix N x N where N is the length of coords array
def createDMatrixGeo(coords):
    matrix = []
    for pointa in coords:
        pointa = convertPointToRad(pointa)
        row = []
        for pointb in coords:
            pointb = convertPointToRad(pointb)
            row.append(calcDistGeo(pointa, pointb))

        matrix.append(row)

    return np.asmatrix(matrix)

#CREATE MATRIX OF DISTANCES EUCL
#input array of coordinates 
#output matrix N x N where N is the length of coords array
def createDMatrixEucl(coords):
    matrix = []
    for pointa in coords:
        row = []
        for pointb in coords:
            row.append(math.sqrt((pointa[1]-pointb[1])**2 + (pointa[2]-pointb[2])**2))
        matrix.append(row)

    return np.asmatrix(matrix)

#gets filename and return MATRIX OF DISTANCES check if geo of euclid
def parseFile(filename):
    with open('./tsp_dataset/' + filename, 'r') as f:
        lines = f.readlines()
        info = {}
        coords = []

        for line in lines:
            #close input
            line = line.strip()
            if line == 'EOF':
                break
            #read info on file
            elif line[0].isupper():
                if line != 'NODE_COORD_SECTION':
                    n, i = line.split(':')
                    info[n.strip()] = i.strip()

            #load coords
            else:
                #print('b', line)
                x,y,z = line.split()
                coords.append((int(x), float(y), float(z)))

    print(info)
    if info['EDGE_WEIGHT_TYPE'] == 'GEO':
        return createDMatrixGeo(coords)
    elif info['EDGE_WEIGHT_TYPE'] == 'EUC_2D':
        return createDMatrixEucl(coords)
         
#get the list of nodes
def parseFileCoords(filename):
    with open('./tsp_dataset/' + filename, 'r') as f:
        lines = f.readlines()
        info = {}
        coords = []

        for line in lines:
            #close input
            line = line.strip()
            if line == 'EOF':
                break
            #read info on file
            elif line[0].isupper():
                if line != 'NODE_COORD_SECTION':
                    n, i = line.split(':')
                    info[n.strip()] = i.strip()

            #load coords
            else:
                #print('b', line)
                x,y,z = line.split()
                coords.append((int(x), float(y), float(z)))

    return coords