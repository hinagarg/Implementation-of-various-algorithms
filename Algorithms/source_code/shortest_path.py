import matplotlib.pyplot as plt
from collections import defaultdict
from prioritydict import priorityDictionary
import datetime
import networkx as nx
import random
import time
#% matplotlib inline

def dijkstra_algorithm(graph,start,target=None):
	start_time = datetime.datetime.now()
	final_dist_dict = {} # a dictionary to  maintain final distances
	dict_predecessor = {} # a dictionary to maintain predessor of nodes  
	PD = priorityDictionary() # a priority dictionary using binary heaps
	PD[start] = 0 # initialize 0 to the start vertex

	for u in PD:
		final_dist_dict[u] = PD[u]
		if u == target: break
		for v in graph[u]:
			uvLength = final_dist_dict[u] + graph[u][v]['weight']
			if v in final_dist_dict:
				if uvLength < final_dist_dict[v]: # raise an error if a shorter path exist for an already finalized node
					raise ValueError 
			elif v not in PD or uvLength < PD[v]:
				PD[v] = uvLength
				dict_predecessor[v] = u
	end_time = datetime.datetime.now()
	t = (end_time - start_time)
	print "Time taken by dijkstra_algorithm in seconds is", t.total_seconds()
	return (final_dist_dict,dict_predecessor)



def bellman_ford_algorithm(graph, start, target = None):
	start_time = datetime.datetime.now()
	destination_dict = {} # destination dictionary to store final distances
	predecessor_dict = {} # predessor dictionary to store the predessor of a node
	for node in graph:
		destination_dict[node] = float('Inf')
        predecessor_dict[node] = None
	destination_dict[start] = 0 
    
	for i in range(len(graph)-1):  # iterate until graph converges
		for u in graph:
			for v in graph[u]: 
				if destination_dict[v] > destination_dict[u] + graph[u][v]['weight']:
					destination_dict[v]  = destination_dict[u] + graph[u][v]['weight']
					predecessor_dict[v] = u
	# check for negative-weight edge cycle and trigger an error if there exist one
	for u in graph:
		for v in graph[u]:
			assert destination_dict[v] <= destination_dict[u] + graph[u][v]['weight']
	end_time = datetime.datetime.now()
	t = (end_time - start_time)
	print "Time taken by bellman_ford_algorithm in seconds is", t.total_seconds()
	return destination_dict, predecessor_dict


def floydwarshall_algorithm(graph, start, target= None):
	start_time = datetime.datetime.now()
	final_distance_dict = {} # final destination dictionary storing the final distance values
	pred_dict = {}

	# initialization
	for u in graph:
		final_distance_dict[u] = defaultdict(dict)  
		pred_dict[u] = {}
		for v in graph:
			final_distance_dict[u][v]['weight'] = 1000
			pred_dict[u][v] = -1
		final_distance_dict[u][u]['weight'] = 0
		for child_node in graph[u]:
			final_distance_dict[u][child_node]['weight'] = graph[u][child_node]['weight']
			pred_dict[u][child_node] = u

	# compare the distances and evaluate shortest path
	for i in graph:
		for u in graph:
			for v in graph:
				updatedist = final_distance_dict[u][i]['weight'] + final_distance_dict[i][v]['weight']
				if updatedist < final_distance_dict[u][v]['weight']:
					final_distance_dict[u][v]['weight'] = updatedist
					pred_dict[u][v] = pred_dict[i][v] 
	end_time = datetime.datetime.now()
	t = (end_time - start_time)
	print "Time taken by floydwarshall_algorithm in seconds is", t.total_seconds()
	return final_distance_dict[start] , pred_dict[start]


def shortestPath(G,start,target,algo_name):
    """
    This function finds a single shortest path from the given start vertex to the given target vertex.
    Returns a list of the vertices in order along the shortest path.
    """
    if(algo_name == "dijkstra_algorithm"):
        final_dist_dict, dict_predecessor  = dijkstra_algorithm(G,start,target)
    elif(algo_name == "bellman_ford_algorithm"):
        final_dist_dict, dict_predecessor = bellman_ford_algorithm(G,start,target)
    else:
        final_dist_dict, dict_predecessor = floydwarshall_algorithm(G,start,target)
    route = []
    while target != start:
        route.append(target)
        target = dict_predecessor[target]
    route.append(start)
    route.reverse()
    return route

# Vary number of nodes , draw graphs and call different algorithms for shortest path computation 
nnodes = 1000
bg = nx.complete_graph(nnodes)
nedges = bg.edges()
print "number of nodes are" , nnodes
print "number of edges are" , len(nedges)

bg.add_node(xrange(nnodes))
lnode = nnodes-1

for edge in nedges:
    bg.add_edge(edge[0], edge[1], {'weight':random.randrange(nnodes)})

pos=nx.spring_layout(bg) # positions for all nodes

plt.figure(figsize=(32,32))
nx.draw_networkx(bg,pos,font_size=20,font_family='sans-serif',alpha=.6, width=2.0,
                     node_size=900)

plt.axis('off')
plt.show() 
graph = nx.to_dict_of_dicts(bg, nodelist=None, edge_data=None)

path1 = shortestPath(graph,0,lnode, "dijkstra_algorithm")
print ("Shortest path by dijkstra_algorithm is: " + str(path1))
path2 = shortestPath(graph,0,lnode,"bellman_ford_algorithm")
print ("Shortest path by bellman_ford_algorithm is: " + str(path2))
path3 = shortestPath(graph,0,lnode,"floydwarshall_algorithm")
print ("Shortest path by floydwarshall_algorithm is: " + str(path3))
