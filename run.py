# Search methods

import search

ab = search.GPSProblem('A', 'U'
                       , search.romania)

node = search.breadth_first_graph_search(ab)
print(node.path())
print(node.path_cost)
node = search.depth_first_graph_search(ab)
print(node.path())
print(node.path_cost)
node = search.Branch_and_Bound(ab)
print(node.path())
print(node.path_cost)

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
