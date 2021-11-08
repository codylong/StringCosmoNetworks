import cPickle as pickle
import datetime
execfile("lib.sage")

def teste8conjecture(heights,alg):
    for i in range(len(alg)):
        h, g = heights[i], alg[i]
        if h == 1 and g != 'E8':
            return False
        if h == 2 and g != 'F4':
            return False
        if h == 3 and g != 'G2':
            return False
        if h == 4 and g != 'A1m':
            return False
        if h == 5 and g != 'N':
            return False
        if h == 6 and g != 0:
            return False    
    return True

#if 'facevertsin' not in vars():
#    facevertsin = pickle.load(open("verticeswsymmetries.pickle",'r'))

#    for v in facevertsin[0]:
#        v.remove((1,0,0))
#        v.remove((0,1,0))
#        v.remove((0,0,1))
#
    facetreeverts = []
#    for i in range(len(facevertsin[0])):
#        for j in range(facevertsin[1][i]):
#            facetreeverts.append(facevertsin[0][i])
#
#    edgetreeverts = pickle.load(open("alledgevertices.pickle",'r'))
#    for v in edgetreeverts:
#        v.remove((1,0))
#        v.remove((0,1))


count = -1
from sage.geometry.polyhedron.palp_database import PALPreader
polys=PALPreader(3)    #read KS 3-folds

import datetime
numsecs = []

#verts = [[-1,-1,-1],[-1,-1,11],[-1,2,-1],[1,-1,-1]]
verts = [[-1,-1,-1],[-1,-1,5],[-1,5,-1],[1,-1,-1]]
p = Polyhedron(verts)
lp = LatticePolytope(verts)
pts = [list(k) for k in p.integral_points()]
pts.remove([0,0,0])
mat = matrix(pts)

if 'tv' not in vars(): 
    tv = triandtoric(pts) 

threecones = tv.fan().cones(3)
twocones = tv.fan().cones(2)

threeconesvs = [[list(k) for k in c.rays()] for c in threecones]
twoconesvs = [[list(k) for k in c.rays()] for c in twocones]

origfpts, origgpts = polypoints([4 for p in pts], pts), polypoints([6 for p in pts], pts)

edgepts = [[list(j) for j in i.points()] for i in lp.edges_lp()]

numsamples = 1
groundalgs, algs, groundmults, commongroundalg = [], [], [], None
e8conj = True
algswe6, vertswe6 = [], []
for i in range(numsamples):
    blpts = pts[0:]
    heights = [1 for p in blpts]
    added = 0
    for c in twoconesvs:
	stopit = True
	for edge in edgepts:
		if c[0] in edge and c[1] in edge:
			stopit = False
	if stopit:
		continue
        treevert = [(1, 0),(4, 1),(3, 1),(2, 1),(1, 1),(1, 2),(1, 3),(1, 4),(0, 1)]
        added += len(treevert)
        for m,n in treevert:
            blpts.append(pl(ti(m,c[0]),ti(n,c[1])))
            heights.append(m+n)

    #m4k, m6k = [4 for p in blpts], [6 for p in blpts]
    #fsecsbl, gsecsbl = sections(m4k,blpts), sections(m6k, blpts)
    nfpts, ngpts = chopfgpts(blpts[len(blpts)-added:],origfpts,origgpts)
    fsecsbl = [[4+dot(v,fpt) for v in blpts] for fpt in nfpts]
    gsecsbl = [[6+dot(v,gpt) for v in blpts] for gpt in ngpts]

    ### 
    # Catalog Algebra Data
    ###
    alg = find_algebra(fsecsbl,gsecsbl)
    if alg not in algs: algs.append(alg)
    if alg[:38] not in groundalgs: 
        groundalgs.append(alg[:38])
        groundmults.append(1)
    else: groundmults[groundalgs.index(alg[:38])] += 1
    if commongroundalg == None:
        commongroundalg = alg[:38]
    for i in range(len(alg[:38])):
        if alg[i] != commongroundalg[i]:
            commongroundalg[i] = "UN"
    print commongroundalg
