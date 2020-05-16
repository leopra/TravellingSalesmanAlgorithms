import matplotlib.pyplot as plt
import networkx as nx
import utilities as ut
import os 
import sys
import itertools as itol
import time
import HeldKarp as HK
import ClosestInsertion as ClIn

assert len(sys.argv) == 2
filename = sorted(os.listdir('tsp_dataset'))[int(sys.argv[1])]
a = ut.parseFile(filename)

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


example = parseFileCoords(filename)

######################################
# DRAW HELD KARP
G = nx.Graph()
print(example)
for i, x, y in example:
    G.add_node(i, pos=(x,y))

path, length = HK.calcHeldKarpRecursiveVersion(a)

for i in range(len(path)-1):
    G.add_edge(path[i], path[i+1])
#connect last to first    
G.add_edge(path[0], path[-1])

pos=nx.get_node_attributes(G,'pos')
nx.draw(G, pos)
plt.show()

#######################################
# DRAW CLOSEST INSERTION
G = nx.Graph()

for i, x, y in example:
    print(i, x, y)
    G.add_node(i, pos=(x,y))

path, length = ClIn.closestInsertion(a)

for i in range(len(path)-1):
    G.add_edge(path[i], path[i+1])
#connect last to first    
G.add_edge(path[0], path[-1])

pos=nx.get_node_attributes(G,'pos')
nx.draw(G, pos)
plt.show()