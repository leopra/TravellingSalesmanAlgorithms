import utilities as ut
import Prim as pr
import time


def printChild(mst):
    string= ""
    for i in range(0, 16):
        string+= str(mst[i].name) + ': '
        for j in range(0, len(mst[i].child)):
            string+= str(mst[i].child[j]) + ' '
        string+= '\n'
    print(string)    

def Preorder(tree, i, H):
    H.append(tree[i].name)
    if len(tree[i].child)>0:
        for j in range(0, len(tree[i].child)):
            Preorder(tree, tree[i].child[j], H)

def printH(H):
    string= ""
    for i in range(0, len(H)):
        string+= str(H[i]+1) + ' '
    print(string)


def approx(file_name, root):

    mst, matrix= pr.Prim(file_name, root) 
    n= len(mst)

    #pr.print_mst(mst,n) #print mst finale

    #aggiungi lista figli
    for i in range(0, n):
        if mst[i].pi!=None:
            r=int(mst[i].pi)
            mst[r].child.append(i)

    #printChild(mst)  #print figli di ogni nodo, per visita preorder

    H=[]
    Preorder(mst, root, H)

    total=0
    #calcolo costo totale
    for i in range(0, n-1):
        total+= matrix[H[i], H[i+1]]
    #aggiunta ultimo arco
    total+= matrix[H[n-1], H[0]]

    return H, total

###########################################################

#algoritmo 2 approssimazione, restituisce il ciclo
#ciclo, totale= approx('ulysses16.tsp', 0)
#print('Cycle')
#printH(ciclo)
#print(totale)

########### test su tutti i grafi ################
#string=""
#f = open('2approx.txt','w')
#files=['burma14.tsp', 'ulysses16.tsp', 'ulysses22.tsp', 'eil51.tsp', 'berlin52.tsp','kroD100.tsp', 'kroA100.tsp', 'ch150.tsp',
#'gr202.tsp', 'gr229.tsp', 'pcb442.tsp', 'd493.tsp', 'dsj1000.tsp']
#for i in range(0, len(files)):
#    start_time = time.time()
#    ciclo, totale= approx(files[i], 0)
#    string+= files[i] + '  ' + str(totale) + '  ' + str(time.time() - start_time) + '\n'
#    print("time : %s seconds " % (time.time() - start_time))
#f.write(string)
#f.close()

########## test per ogni nodo del grafo #########
#string=""
#f = open('dsj1000.txt','w')
#for i in range(0, 1000):
#    ciclo, totale= approx('dsj1000.tsp', i)
#    string+= str(i+1) + '   ' + str(totale) + '\n'
#    print(i+1)
#f.write(string)
#f.close()