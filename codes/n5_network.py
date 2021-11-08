import snap as snap
import pickle

#/opt/local/bin/python2.7

G = snap.TUNGraph.New()
for i in range(4231):
	G.AddNode(i)



    
filename = "/codes/height5.txt"
file, thisedgeset = open(filename,'rb'), []
for k in file:
	cur = [int(p) for p in k[:len(k)-1].split()]
	G.AddEdge(cur[0],cur[1])		
file.flush()
file.close() 


################
# Configurations
################

#configs = pickle.load(open('all_configs.pickle','r'))


################
# Plots are cool
################


import numpy as np
import matplotlib.pyplot as plt
import pandas

#degree centrality
degcen = []
for NI in G.Nodes():
    degcen.append(snap.GetDegreeCentr(G, NI.GetId()))
degcenlist = np.asarray(degcen)
fig, ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')
pandas.Series(degcenlist).hist(ax=ax,bins=50,bottom=10^(-4))
print "Degree centrality log-log"
plt.show()
fig.savefig('DegreesCentralityLogLog.pdf')

#eigenvector centrality
eigencen = []
NIdEigenH = snap.TIntFltH()
snap.GetEigenVectorCentr(G, NIdEigenH)
for item in NIdEigenH:
    eigencen.append(NIdEigenH[item])
eigenlist = np.asarray(eigencen)
fig, ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')
pandas.Series(eigenlist).hist(ax=ax,bins=50,bottom=10^(-6))
print "Eigenvector centrality log-log"
plt.show()
fig.savefig('n5EigenvectorCentralityLogLog.pdf')


#Katz centrality
PRankH = snap.TIntFltH()
snap.GetPageRank(G, PRankH)
pranks = []
for item in PRankH:
    pranks.append(PRankH[item])
prlist = np.asarray(pranks)
fig, ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')
pandas.Series(prlist).hist(ax=ax,bins=50,bottom=10^(-5))
print "Page rank log-log"
plt.show()
fig.savefig('n5pagerankLogLog.pdf')

#Eigenvector
EigvV =  snap.TFltV()
snap.GetEigVec(G, EigvV)
evec = []
for Val in EigvV:
    evec.append(Val)

eveclist = np.asarray(evec)
eveclistcum = np.cumsum(eveclist)
fig, ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')
pandas.Series(eveclist).hist(ax=ax,bins=50,bottom=0)
print "Page rank log-log"
plt.show()



#page rank
PRankH = snap.TIntFltH()
snap.GetPageRank(G, PRankH)
pranks = []
for item in PRankH:
    pranks.append(PRankH[item])

pranks.index(max(pranks))
#8389995
prlist = np.asarray(pranks)
fig, ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('log')
pandas.Series(prlist).hist(ax=ax,bins=50,bottom=9*10^(-9))
print "Page rank log-log"
plt.show()


fig.savefig('page_rank_log_log.pdf')

OutDegV = snap.TIntPrV()
snap.GetNodeOutDegV(G, OutDegV)
outdegrees = []
for item in OutDegV:
	outdegrees.append(item.GetVal2())
outdeglist = np.asarray(outdegrees)
max(outdeglist)
min(outdeglist)

degrees = outdeglist

fig, ax = plt.subplots()
ax.set_yscale('linear')
ax.set_xscale('linear')
pandas.Series(outdeglist).hist(ax=ax,bins=15,bottom=0)
print "Degrees"
plt.show()
fig.savefig('n5Degrees.pdf')

#clustering is zero for our network
#NIdCCfH = snap.TIntFltH()
#snap.GetNodeClustCf(G, NIdCCfH)
#clustering = []
#for item in NIdCCfH:
#    clustering.append(NIdCCfH[item])
#clusterlist = np.asarray(clustering)
#fig, ax = plt.subplots()
#ax.set_yscale('log')
#ax.set_xscale('log')
#pandas.Series(clusterlist).hist(ax=ax,bins=50,bottom=10^(-10))
#print "Clustering log-log"
#plt.show()

#page rank versus degree
degrk = []
for i in range(len(outdeglist)):
	degrk.append([outdeglist[i],pranks[i]])

fig, ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('linear')
df = pandas.DataFrame(degrk,columns = ['a','b'])
df.plot.scatter(x = 'a',y = 'b', ax=ax)
print "Page rank (log) versus degree"
plt.show()
fig.savefig('n5page_rank_versus_degree_log_linear.pdf')


#degree distribution for random graphs
degrees = []

for ii in range(100):
	G2 = snap.GenRndGnm(snap.PUNGraph, 41873645, 99546132)
	OutDegV = snap.TIntPrV()
	snap.GetNodeOutDegV(G2, OutDegV)
	for item in OutDegV:
		degrees.append(item.GetVal2())
	ii
	max(outdeglist)
	min(outdeglist)

fig, ax = plt.subplots()
ax.set_yscale('linear')
ax.set_xscale('linear')
pandas.Series(outdeglist).hist(ax=ax,bins=15,bottom=0)
print "Degrees"
plt.show()
fig.savefig('Degrees2.pdf')


    
