import utilities as ut
import Prim as pr


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
        string+= str(H[i]) + ' '
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

    print('Cycle')

    H=[]

    Preorder(mst, root, H)

    printH(H)

    total=0
    #calcolo costo totale
    for i in range(0, n-1):
        #print('i ', H[i], 'i+1 ', H[i+1])
        #print(i)
        total+= matrix[H[i], H[i+1]]
    #aggiunta ultimo arco
    #print('i ', H[n-1], 'j ', H[0])
    total+= matrix[H[n-1], H[0]]
    print(total)
    print('--------------------------------')


approx('burma14.tsp', 0)

#approx('ulysses22.tsp', 0)
