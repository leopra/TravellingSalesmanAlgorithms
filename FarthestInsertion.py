import utilities as ut
import networkx as nx
import matplotlib.pyplot as plt

MAX= 9223372036854775807


def distanza(k, C, matrix): #k nodo, C un insieme e matrice come matrice di adiacenza
    minimo=MAX
    for i in range(0, len(C)):
        if minimo> matrix[k, C[i]]:
            minimo= matrix[k, C[i]]
    return minimo

def selezione(V,C,matrix):
    ############ SELEZIONE #######################
    massimo=-1
    k=-1 #nodo selezionato 
    for i in range(0, len(V)):
        dist=distanza(V[i], C, matrix)
        if dist>massimo:
            massimo= dist
            k=V[i]
    return k

def printCycle(C):
    string=""
    for i in range(0, len(C)):
        string+= str(C[i]+1) + " "
    print(string)

def calcTot(C, matrix):
    ##calcolo peso del ciclo costruito 
    Tot=0
    for i in range(0, len(C)):
        if i+1< len(C):
            Tot+= matrix[C[i],C[i+1]]
        else:
            Tot+= matrix[C[i], C[0]]
    return Tot

def farthest(file_name):

    ############# LETTURA FILE ###############
    print(file_name)
    matrix=ut.parseFile(file_name)
    n=len(matrix)
    #print(matrix)

    ############ VARIABILI DA UTILIZZARE ############
    C=[] #insieme di archi risultanti
    V=[] #insieme di tutti i nodi iniziali che vengono estratti man mano
    for i in range(0, n):
        V.append(i)
    #print(V)

    ############# INIZIALIZZAZIONE ##################
    minimo= MAX
    j=-1
    for i in range(1, n):
        if matrix[0,i]<minimo:
            minimo=matrix[0,i]
            j=i
    
    #inserisco i primi due nodi nel circuito parziale
    C.append(0)
    C.append(j)
    #elimino i due nodi inseriti dall'insieme di tutti i vertici
    V.remove(0)
    V.remove(j)

    k=selezione(V,C,matrix)
    while k!=-1: #se ritorna -1 non ho più elementi da selezionare
        ########### INSERIMENTO #####################
        #arco {i, j} in C che minimizza matrix[i,k] + matrix[k,j] - matrix[i, j]
        minimo=MAX
        pos=-1 #dove inserire il nodo k dopo aver trovato la soluzione
        for i in range(0, len(C)): #controllo le coppie di archi all'interno di C
                if i+1< len(C):
                    val=matrix[C[i],k] + matrix[k,C[i+1]] - matrix[C[i], C[i+1]]
                    j=i+1
                else:
                    val=matrix[C[i],k] + matrix[k,C[0]] - matrix[C[i], C[0]]
                    j=0
                if val<minimo: 
                    minimo=val
                    pos=j

        #inserisco K tra i e j nella soluzione finale, elimino K da V e lo aggiungo a C
        V.remove(k)
        C.insert(pos, k)


        #TODO debug
        #G = nx.Graph()
        #plt.figure(3, figsize=(10,10))
        #if len(C) > 1:
        #    for i, x, y in ut.parseFileCoords(file_name):
        #        G.add_node(i, pos=(x,y))
        #    for i in range(len(C)-1):
        #        G.add_edge(C[i]+1, C[i+1]+1)
        #    G.add_edge(C[0]+1, C[-1]+1)
        #pos=nx.get_node_attributes(G,'pos')
        #nx.draw(G, pos, node_size=15, with_labels=True)
        #plt.show()

        k=selezione(V,C,matrix)

    
    printCycle(C)
    totale=calcTot(C, matrix)
    print(totale)

    return C, totale


string=""
f = open('result1.txt','w')
C, totale= farthest('ulysses22.tsp')
string+= 'ulysses22.tsp' + '  ' 
for i in range(0, len(C)):
    string+= str(C[i]+1) + ','
print(string)
f.write(string)
f.close()
    
        

