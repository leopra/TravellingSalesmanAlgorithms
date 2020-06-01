import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def plotBar():
    labels=['burma14', 'ulysses16', 'ulysses22', 'eil51', 'berlin52','kroD100', 'kroA100', 'ch150',
    'gr202', 'gr229', 'pcb442', 'd493', 'dsj1000']
    farthest=[0.0000, 0.0303, 0.0301, 0.0610, 0.0968, 0.0474, 0.1254, 0.1085, 0.0812, 0.1174, 0.1476, 0.0921, 0.1125]
    closest= [0.0156, 0.1158, 0.1030, 0.1526, 0.1913, 0.1963, 0.2153, 0.2166, 0.1402, 0.1645, 0.1558, 0.1170, 0.2199]
    approx=[0.0782, 0.0942, 0.1318, 0.3615, 0.2666, 0.2211, 0.2425, 0.2753, 0.2560, 0.3054, 0.3289, 0.2899, 0.3305]

    index = np.arange(13)
    bar_width = 0.15
    opacity = 0.8

    rects1 = plt.bar(index, farthest, bar_width, alpha=opacity,color='r',label='Farthest')
    rects2 = plt.bar(index + bar_width, closest, bar_width,alpha=opacity,color='b',label='Closest')
    rects3 = plt.bar(index + 2*bar_width, approx, bar_width,alpha=opacity,color='g',label='2-Approssimato')

    y_pos = np.arange(len(labels))
    plt.rcParams["figure.figsize"] = (14,10)
    plt.ylabel('Errore')
    plt.xlabel('Istanza Tsp')
    plt.xticks(y_pos, labels)
    plt.legend()
    plt.show()

plotBar()