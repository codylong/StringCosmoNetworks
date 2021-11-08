import sys
from random import randint
import networkx as nx
import matplotlib.pyplot as plt

nnodes, nedges = int(sys.argv[1]), int(sys.argv[2])
print nnodes, nedges

filename = "rgN"+str(nnodes)+"E"+str(nedges)+".txt"
file = open(filename,"w")
count = 0
while count < nedges:
    file.write(str(randint(1,nnodes)) + " " + str(randint(1,nnodes))+ "\n")
    count += 1
    
file.close()

print 'Reading Graph from Edgelist'
g = nx.read_edgelist(filename,create_using=nx.Graph(),nodetype=int)

#print 'Drawing Graph'
#nx.draw(g)
#plt.show()
