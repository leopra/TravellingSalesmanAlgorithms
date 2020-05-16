import networkx as nx
import matplotlib.pyplot as plt

G=nx.dodecahedral_graph()
labels=nx.draw_networkx_labels(G,pos=nx.spring_layout(G))
plt.show()