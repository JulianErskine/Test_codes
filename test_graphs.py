import networkx as nx
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from([1,2,3,'droneX'])
plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')

plt.show()
