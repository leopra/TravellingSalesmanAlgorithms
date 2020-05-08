import os 
import math

filename = os.listdir('tsp_dataset')
matrix=[[]]

#gets filename and return array with info and array with coordinates
def parseFile(filename):
    with open('./tsp_dataset/' + filename, 'r') as f:
        lines = f.readlines()
        info = {}
        coords = []

        for line in lines:
            #close input
            if line == 'EOF\n':
                break
            #read info on file
            elif line[0].isupper():
                if line != 'NODE_COORD_SECTION\n':
                    n, i = line.rstrip().split(': ')
                    info[n]=i

            #load coords
            else:
                x,y,z = line.split(' ')
                coords.append((int(x), float(y), float(z)))

    return info, coords
            
    
a,b = parseFile(filename[0])

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


#TESTING
k1 = convertPointToRad(b[0])
k2 = convertPointToRad(b[1])
print(b[0],b[1])
print(k1, k2)
print(calcDistGeo(k1,k2))

#CREATE MATRIX OF DISTANCES
#input array of coordinates 
#output matrix N x N where N is the length of coords array
def createDMatrix(coords):
    matrix = []
    for pointa in coords:
        pointa = convertPointToRad(pointa)
        row = []
        for pointb in coords:
            pointb = convertPointToRad(pointb)
            row.append(calcDistGeo(pointa, pointb))

        matrix.append(row)

    return matrix

#testing
print(len(createDMatrix(b)), len(createDMatrix(b)[0]))