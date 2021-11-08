import graph_tool.all as gt

filename = "rgN50000000E100000000.txt"
file = open(filename,'rb')

G = gt.Graph()

G.add_vertex(50000000)
print G.num_vertices()

count = 0
for k in file:
    edge = [int(p) for p in k[:len(k)-1].split()]
    # print edge
    if count % 100000 == 0: print (G.num_vertices(), G.num_edges())
    G.add_edge(G.vertex(edge[0]-1),G.vertex(edge[1]-1))
    count += 1
    
file.close()
