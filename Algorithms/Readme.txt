#### Given program computes the shortest path between a source and a target node in an auto-generated graph ####

Notes:
1. To increase/decrease the number of nodes set the new value in the variable "nnodes" defined in "shortest_path.py".
2. By default source node has been set to 0 and target to be the last node.
3. To change different input graphs set a variable "bg" in "shortest_path.py" as follows:

Random graph:
nx.gnp_random_graph(nnodes,0.5)

Complete graph:
nx.complete_graph(nnodes)

Star graph:
nx.star_graph(nnodes)

path graph:
nx.path_graph(nnodes)

cycle graph:
nx.cycle_graph(nnodes)

----------------------------------------------------------------------------
Run the program:
--- Make sure to keep prioritydict.py in the same folder as shortest_path.py
--- python shortest_path.py

-----------------------------------------------------------------------------

Folder description:

graphs: contains generated graphs while doing experiments
source_code: contains code for the project
report: detailed project report
