library(igraph)
graph.input <- read.csv("data/konisburg.csv", header=TRUE, sep=",")
reference.graph <- graph.data.frame(graph.input,directed=TRUE)
gs.node <- data.frame(node = unlist(list(V(reference.graph)$name))
                       ,In = unlist(list(degree(reference.graph,mode="in")))
                       ,Out = unlist(list(degree(reference.graph,mode="out")))
                       ,Degree = unlist(list(degree(reference.graph,mode="total")))
                       ,WeightedDegree = unlist(list(graph.strength(reference.graph)))
                       ,EigenCentrality = unlist(list(evcent(reference.graph,weight=rep(1,length(E(reference.graph))))$vector))
                       ,Betweenness = unlist(list(betweenness(reference.graph)))
                       ,PageRank = unlist(list(page.rank(reference.graph)$vector))
)
gs.node
