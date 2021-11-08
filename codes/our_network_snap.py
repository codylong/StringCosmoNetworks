import snap as snap
import pickle

#/opt/local/bin/python2.7

G = snap.TUNGraph.New()
for i in range(41873645):
	G.AddNode(i)


#G.AddNode(41873644)
edgesets = []

numex = [5,32,144,563,2003,6585,20174,57728,154068,382205,876185,1839391,3485171,5820059,8272333,9449159,7844747,3663073]
numex = [c + 1 for c in numex]
print "sum of numex", sum(numex)+2 # idx from 0, so + len numex, + 1-cone, 3-cone


shiftlow, shifthigh = 0, 6
#5
#for i in range(5,38,2):
pairs = []
for i in range(5,10,2):
	print shiftlow, shifthigh
	print("Graph V and E", G.GetNodes(), G.GetEdges())
    
	filename = "./landscape_data/c" + str(i) + "-" + str(i+2) + ".lnd.edg.dat"
	print filename
	file, thisedgeset = open(filename,'rb'), []
	for k in file:
		cur = [int(p) for p in k[:len(k)-1].split()]
		#print cur
		cur[0] += shiftlow
		cur[1] += shifthigh
		pairs.append([cur[0], cur[1]])
		#G.AddEdge(cur[0],cur[1])
		#G.AddEdge(cur[1],cur[0]) 		
	file.flush()
	file.close() 
	shiftlow += numex[range(5,40,2).index(i)]
	shifthigh += numex[range(5,40,2).index(i+2)]
#	shiftlow += numex[range(5,38,2).index(i)]
#	shifthigh += numex[range(5,40,2).index(i+2)]


#get 1-cone and 3-cone stuff in here


G.AddEdge(41873643,0)
G.AddEdge(41873643,1)
G.AddEdge(41873643,2)
G.AddEdge(41873643,3)
G.AddEdge(41873643,4)
G.AddEdge(41873643,5)
G.AddEdge(41873644,41873643)

#G2 = TUNGraph(G)

if 'G' not in vars():
    	print 'Loading Graph'
	FIn = snap.TFIn("network_snap.graph")
	G = snap.TUNGraph.Load(FIn)

#if 'prk' not in vars():
#    print "Loading Pagerank"
#    prk = pickle.load(open("prk.pickle","r"))

#FOut = snap.TFOut("/Users/cody/Desktop/network_snap.graph")
#G.Save(FOut)
#FOut.Flush()

################
# Configurations
################

configs = pickle.load(open('all_configs.pickle','r'))


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
pandas.Series(degcenlist).hist(ax=ax,bins=50,bottom=9*10^(-9))
pandas.Series(dats).hist(ax=ax,bins=50,bottom=9*10^(-9))
print "Degree centrality log-log"
plt.show()
fig.savefig('DegreesCentralityLogLog.pdf')

data2 = [abs(i) for i in data2]
degcenlist = np.asarray(data2)
fig, ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('linear')
pandas.Series(degcenlist).hist(ax=ax,bins=50,bottom=10^(-18))
#pandas.Series(dats).hist(ax=ax,bins=50,bottom=9*10^(-9))
print "Degree centrality log-log"
plt.show()
#fig.savefig('DegreesCentralityLogLog.pdf')

#eigenvector centrality
eigencen = []
NIdEigenH = snap.TIntFltH()
snap.GetEigenVectorCentr(G, NIdEigenH)
for item in NIdEigenH:
    eigencen.append(NIdEigenH[item])
eigenlist = np.asarray(eigencen)
fig, ax = plt.subplots()
ax.set_yscale('log')
ax.set_xscale('linear’)
plt.xlabel('Eigenvector Centrality')
plt.ylabel('Frequency')
pandas.Series(eigenlist).hist(ax=ax,bins=50,bottom=9*10^(-9))
print "Eigenvector centrality log-log"
plt.show()
fig.savefig('EigenvectorCentralityLogLog.pdf')


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
pandas.Series(prlist).hist(ax=ax,bins=50,bottom=9*10^(-9))
print "Page rank log-log"
plt.show()

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
fig.savefig('Degrees.pdf')

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
fig.savefig('page_rank_versus_degree_log_linear.pdf')


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

plt.rcParams.update({'font.size': 15})
plt.gcf().subplots_adjust(bottom=0.15)
bins = np.logspace(-16,-1,30)
widths = (bins[1:] - bins[:-1])/2

# Make the histogram
hist = np.histogram(eigencen, bins=bins)

# Plot it
plt.bar(bins[:-1], hist[0], widths, color = 'steelblue')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Eigenvector Centrality')
plt.ylabel('Frequency')
#plt.show()
plt.savefig('largerfont.pdf')



    
