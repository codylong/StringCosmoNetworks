import graph_tool.all as gt
import pickle

# G = gt.Graph()
# G.add_vertex(41873645)

# edgesets = []

# numex = [5,32,144,563,2003,6585,20174,57728,154068,382205,876185,1839391,3485171,5820059,8272333,9449159,7844747,3663073]
# numex = [c + 1 for c in numex]
# print "sum of numex", sum(numex)+2 # idx from 0, so + len numex, + 1-cone, 3-cone

# # LATER: get 1-cone and 3-cone stuff in here

# shiftlow, shifthigh = 0, 6
# for i in range(5,38,2):
#     print shiftlow, shifthigh
#     print "Graph V and E", G.num_vertices(), G.num_edges()
    
#     filename = "../landscape_data/c" + str(i) + "-" + str(i+2) + ".lnd.edg.dat"
#     print filename
#     file, thisedgeset = open(filename,'rb'), []
#     for k in file:
#         cur = [int(p) for p in k[:len(k)-1].split()]
#         cur[0] += shiftlow
#         cur[1] += shifthigh
#         G.add_edge(G.vertex(cur[0]),G.vertex(cur[1]))

#     shiftlow += numex[range(5,38,2).index(i)]
#     shifthigh += numex[range(5,38,2).index(i+2)]

#     file.flush()
#     file.close() 

if 'G' not in vars():
    #print 'Loading Graph'
    G = gt.load_graph('tree_network.xml.gz')

if 'prk' not in vars():
    print "Loading Pagerank"
    prk = pickle.load(open("prk.pickle","r"))


################
# Plots are cool
################
    

####
# Degree Distribution

deg = G.get_out_degrees(G.get_vertices()) # uses C to loop, is fast
deg = np.asarray(deg)
fig, ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')
pandas.Series(deg).hist(ax=ax,bins=10,bottom=0.1)
print "Degree distribution log-log"
plt.show()

####
# Pagerank distribution

prk = np.asarray(prk)
fig, ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')
pandas.Series(prk).hist(ax=ax,bins=100,bottom=0.1)
print "Pagerank distribution log-log"
plt.show()
