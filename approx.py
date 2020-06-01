import utilities as ut
import Prim as pr
import time


def printChild(mst):
    string= ""
    for i in range(0, 14):
        string+= str(mst[i].name) + ': ' + str(mst[i].pi)
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

    mst, matrix, extract= pr.Prim(file_name, root) 
    n= len(mst)

    #pr.print_mst(mst,n) #print mst finale

    #aggiungi lista figli
    for i in range(0, len(extract)):
        j=extract[i]
        if mst[j].pi!=None:
            r=int(mst[j].pi)
            mst[r].child.append(j)

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

