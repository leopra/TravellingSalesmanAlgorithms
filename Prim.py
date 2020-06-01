import sys
import math
import glob
import time
import utilities as ut

MAX= 9223372036854775807

class Node:
    def __init__(self, name, val):
        self.name=name
        self.val=val
        self.pi= None
        self.child=[]

    
class Heap:

    def __init__(self):
        self.heap= []
        self.size= 0
        self.map=[] #map to register the position of Node on heap
        self.exist= []


    #find parent of node i
    def parent(self, i):
        if i>1:
            parent= int((i-1)/2)
        else:
            parent= 0
        return parent
    
    #find left child of node i
    def left(self, i):
        return 2*i +1
        #2*i + 1

    #find right child of node i
    def right(self, i):
        return 2*i +2
        #2*i + 2

    #function to balance the heap tree
    #min-heap property is that for every node i other than the root, array[parent(i)]<= array[i]
    def minHeapify(self, i):

        k=i
        l= int(self.left(i))
        r= int(self.right(i))

        if r< self.size and self.heap[r].val<self.heap[k].val:
            k=r 
        if l< self.size and self.heap[l].val<self.heap[k].val:
            k=l
        if k!=i:
            self.swap(i, k)
            t=self.heap[i]
            self.heap[i]=self.heap[k]
            self.heap[k]=t
            self.minHeapify(k)

    def swap(self, i, j):
        self.map[self.heap[i].name]= j
        self.map[self.heap[j].name]= i


    #return the position in the heap for the node i
    def getMap(self, i):
        return self.map[i]

    #print element of heap
    def printHeap(self):
        string= ""
        if self.size>0 :
            for i in range(0,self.size):
                string += str(self.heap[i].val) + ' '
        print(string)
    
    #extract the minimum element from heap and reset the property of minHeap (through minHeapify) 
    def extract_min(self):
        if self.size<0:
            print('errore')
        else:
            smaller= self.heap[0]
            self.swap(0, self.size-1)
            self.heap[0]=self.heap[self.size-1]
            self.size=self.size-1
            self.minHeapify(0)
            return smaller
            

    #function to decrease element of heap, useful for Prim and aux function for heap_insert
    #change or insert element and reset heap property (array[parent(i)]<= array[i])
    #i= position in the heap, element= new value
    def heap_decrease(self, i, element):
        #self.setMap()
        pos=self.getMap(i)
        self.heap[pos].val=element
        while pos>0 and self.heap[pos].val<self.heap[self.parent(pos)].val:
            self.swap(pos, self.parent(pos))
            t=self.heap[pos]
            self.heap[pos]=self.heap[self.parent(pos)]
            self.heap[self.parent(pos)]=t
            pos=self.parent(pos)

    #return the size of heap
    def getSize(self):
        return self.size

    #function to create Heap
    #it's necessary to call minHeapify because the proprerty of MinHeap is already satisfied
    def buildHeap(self, size, radice):
        self.size=size
        for i in range(0, size):
            self.map.append(i)
            if i==radice:
                self.heap.append(Node(i, 0))
            else:
                self.heap.append(Node(i, MAX))
            self.exist.append(True)
        for i in range(int(size/2), -1, -1):
            self.minHeapify(i)


    
    #print Map array
    def printMap(self):
        string="map "
        for i in range(0, len(self.map)):
            string+= str(self.map[i])+ ' ' 
        print(string)


    def setExist(self, i):
        self.exist[i]= False

    def getExist(self, i):
        return self.exist[i]

    def printExist(self):
        for i in range(0, 16):
            print(self.exist[i])


import glob
import time
import utilities as ut #library to create matrix for graph

def print_mst(mst, n):
    for i in range(0, n):
        print(str(mst[i].name) + ': ' + str(mst[i].val) + ' ' + str(mst[i].pi))

def Prim(file_name, radice): 
    print(file_name)
    matrix=ut.parseFile(file_name)
    n=len(matrix)
   
    #initialization for Prim algorithm 
    #radice a zero e il resto infinito 
    #lista grande n Node
    mst=[]
    for i in range(0, n):
        if i==radice:
            mst.append(Node(i, 0))
        else:
            mst.append(Node(i, MAX))
    
    hp= Heap()
    hp.buildHeap(n, radice) #create heap structure
    Extract=[]

    totale = 0 #variable to count the weight of mst
    while hp.getSize()>0: 
        u= hp.extract_min() #extract min from heap
        totale += u.val
        Extract.append(u.name)
        hp.setExist(u.name) #set that the node is extracted
        for i in range(0, n):
            if(hp.getExist(i) and i!=u.name and matrix[u.name,i] < mst[i].val):
               mst[i].val= matrix[u.name,i]
               mst[i].pi= u.name #the attribute label is like π
               hp.heap_decrease(i, matrix[u.name,i]) #function to change the weight of node v in the heap
    
    return mst, matrix, Extract



