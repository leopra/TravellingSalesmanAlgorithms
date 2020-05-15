import utilities as ut
import os 
import sys
import itertools as itol
import time



filename = sorted(os.listdir('tsp_dataset'))
if (len(sys.argv)==2):
    a = ut.parseFile(filename[int(sys.argv[1])])
    #print(a)

##########
#HELD&KARP
##########
# Set like {1,2,3,4} can be encoded by 2^1 + 2^3 + 2^2 + 2^4 = 0b11110
# 2^3 can be calculated with bitwise shift: 2 << 3 
# a dictionary C is used where each key is a tuple (v,S) where S is the set encoded in binary
def calcHeldKarp(dmatrix):
    dim = len(dmatrix) 

    #inside C it saves all subset solutions
    C = { }
    
    for i in range(1, dim):
        C[(i, 1 << i)] = (dmatrix[i,0], 0)

    for j in range(2, dim):
        for subset in itol.combinations(range(1,dim), j):
            enc = 0
            #encode each city combination
            for bit in subset:
                enc |= 1 << bit

            #find the cheapest previus set to get to this subset
            for k in subset:
                #remove k from S and search on all these possibile sets
                prevsub = enc & ~ (1 << k)
                
                results= []
                for m in subset:
                    #the 0 node is the starting point so is ignored, also if j point is already traversed is ignored
                    if m==0 or m==k:
                        pass
                    # search for all possible paths and save them in results to then get the min cost path
                    else:
                        try:
                            results.append((C[(m, prevsub)][0] + dmatrix[m,k], m))
                        except:
                            raise Exception('error accessing key', (m,prevsub), ' in C')

                C[(k, enc)] = min(results)    
    

    #now we search for the encoding containing all cities (0b11111...0) except the first
    final = 2**dim-2
    fresults = []
    #print('C: ', C)

    for k in range(1,dim):
        #for each node of final combination (all nodes except 0) check distance to 0
        fresults.append((C[(k, final)][0] + dmatrix[k,0], k))
    
    opt, parent = min(fresults)

    path = []
    for i in range(dim - 1):
        path.append(parent)
        new_bits = final & ~(1 << parent)
        _, parent = C[(parent, final)]
        final = new_bits

    path.append(0)

    print('il path: ', list(map(lambda x: x+1,reversed(path))))
    # Add implicit start state
    path.append(0)

    return opt

#bigger recursion limit to avoid error
sys.setrecursionlimit(1000)

#recursive version of the Held Karp algorithm
#receives a matrix of distances and returns the min circular path traversing al nodes once
def calcHeldKarpRecursiveVersion(dmatrix):
    dim = len(dmatrix)
    dist = {}
    py = {}   
    
    #recursive function to be called
    def HK_Visit(v, S):
        #print(v,encToList(S)) #Debug
        #case base
        if 1<<v == S:
            return dmatrix[0,v]

        #already calculated distance
        elif (v,S) in dist.keys():
            return dist[v,S]

        else:
            mindist = 2147483647
            minprec = -1

            prevsub = S & ~ (1 << v)
            listanodi = encToList(prevsub)

            for u in listanodi:
                distance = HK_Visit(u, prevsub)

                if distance + dmatrix[u,v] < mindist:
                    mindist = distance + dmatrix[u,v]
                    #print(v, encToList(S))
                    minprec = u
            
            dist[v,S] = mindist
            py[v,S] = minprec

            return mindist

    def build_path():
        percorso = []
        k=0
        S=2**dim-1
        while len(percorso) < len(dmatrix)-1:
            temp = py[(k,S)]
            percorso.append(temp)
            S = S & ~ (1 << k)
            k = temp
        
        percorso.append(0)
        
        return percorso


    risultato = HK_Visit(0, 2**dim-1) #(1,V)
    #indexes were used 1 off so 1 add one to all so they represent the real nodes name
    print('il path: ', list(reversed(list(map(lambda x: x+1, build_path())))))
    return risultato


#convert the binary encoding in the corresponding list
def encToList(binary):
    t = bin(binary)[2:]
    sett = []
    num=0
    for i in t[::-1]:
        if i == '1':
            sett.append(num)
        num += 1
    return sett

#print(a)
s = time.time()
pathlen = calcHeldKarp(a)
print('Iterative: ', pathlen)
e = time.time()
print(e-s)
s = time.time()
print('Recursive: ', calcHeldKarpRecursiveVersion(a)) 
e = time.time()
print(e-s)

#################################################################################################################
# Part for Graph Plotting
#################################################################################################################
import matplotlib.pyplot as plt

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
                x,y,z = line.split(' ')
                coords.append((int(x), float(y), float(z)))

    return coords

# plotting = parseFile(filename[int(sys.argv[1])])
# plt.scatter([x for n,x,y in plotting], [y for n,x,y in plotting])
# for i in range(len(plotting)):
#     n,x,y = plotting[i]
#     plt.plot(x, y, 'bo')
#     plt.text(x * (1 + 0.01), y * (1 + 0.01) , n, fontsize=12)


# for k in range(len(path)-1):
#     t1 = [path[k], path[k+1]]
#     t2 = [path[k], path[k+1]]
# plt.show()
