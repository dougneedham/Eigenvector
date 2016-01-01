import networkx as nx
import pandas as pd

fh = open('data/konisburg.csv','r')
content = fh.read()
fh.close()
g = nx.Graph()
for line in content.split('\n'):
    if(len(line)>0):
             (source,target) = line.split(',')
             if(source != 'Source'):
                     g.add_edge(source,target)
deg =  g.degree()
ecn =  nx.eigenvector_centrality_numpy(g)
pr = nx.pagerank(g)
bc = nx.betweenness_centrality(g)

columns = ['Node','Degree','EeginCentrality','Betweenness','PageRank']
index = sorted(deg.keys())
df = pd.DataFrame(index=index,columns=columns)

for key in deg.keys():
	df.ix[key]["Node"] = key
	df.ix[key]["Degree"] = deg[key]
	df.ix[key]["EeginCentrality"] = ecn[key]
	df.ix[key]["Betweenness"] = bc[key]
	df.ix[key]["PageRank"] = pr[key]
print df
