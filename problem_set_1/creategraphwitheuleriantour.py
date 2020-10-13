# Eulerian Tour Ver 1
#
# Write a function, `create_tour` that takes as
# input a list of nodes
# and outputs a list of tuples representing
# edges between nodes that have an Eulerian tour.
#

'''
 In the first step, I pick two random nodes and connect them
00:26
and choose a random node among the nodes that are connected—say this one—
00:29
and connect them and repeat this process until all the nodes are connected.
00:32
Then classify all the nodes as being odd or even.
00:35
All the nodes in orange have odd degree, and the other two are even.
00:38
We then pick a node in the set of nodes with odd degree—say this one—
00:42
and connect it with another node that has odd degree.
00:44
We'll connect it to that one. These both now have even degree.
00:47
We repeat this process—pick this node, connect it with that node.
00:50
Now we have two nodes left that have odd degree.
00:53
Unfortunately, they're already connected.
00:55
What we can do is pick one of the nodes with odd degree
00:57
and then randomly pick another node with even degree
00:59
that it's not already connected to and connect them. So, maybe this one down here.
01:02
Now this new node has odd degree. The one node no longer does.
01:05
Now we have two nodes with odd degree that we can connect. 
'''

import random

def create_tour(nodes):
    # your code here

    starting_node = nodes[0] # get the first one
    number_of_nodes = len(nodes)
    i = 0
    vertices = []
    #  Connect 1st with 2nd, 2nd with 3rd, 3rd with 4th, and last with 1st
    while i < number_of_nodes - 1:
        vertices.append((nodes[i], nodes[i+1]))
        i = i + 1
    vertices.append((nodes[number_of_nodes - 1], starting_node))
    return vertices
#########

def get_degree(tour):
    degree = {}
    for x, y in tour:
        degree[x] = degree.get(x, 0) + 1
        degree[y] = degree.get(y, 0) + 1
    return degree

def check_edge(t, b, nodes):
    """
    t: tuple representing an edge
    b: origin node
    nodes: set of nodes already visited

    if we can get to a new node from `b` following `t`
    then return that node, else return None
    """
    if t[0] == b:
        if t[1] not in nodes:
            return t[1]
    elif t[1] == b:
        if t[0] not in nodes:
            return t[0]
    return None

def connected_nodes(tour):
    """return the set of nodes reachable from
    the first node in `tour`"""
    a = tour[0][0]
    nodes = set([a])
    explore = set([a])
    while len(explore) > 0:
        # see what other nodes we can reach
        b = explore.pop()
        for t in tour:
            node = check_edge(t, b, nodes)
            if node is None:
                continue
            nodes.add(node)
            explore.add(node)
    return nodes

def is_eulerian_tour(nodes, tour):
    # all nodes must be even degree
    # and every node must be in graph
    degree = get_degree(tour)
    for node in nodes:
        try:
            d = degree[node]
            if d % 2 == 1:
                print("Node %s has odd degree" % node)
                return False
        except KeyError:
            print("Node %s was not in your tour" % node)
            return False
    connected = connected_nodes(tour)
    if len(connected) == len(nodes):
        return True
    else:
        print("Your graph wasn't connected")
        return False

def test():
    nodes = [20, 21, 22, 23, 24, 25]
    tour = create_tour(nodes)
    return is_eulerian_tour(nodes, tour)
