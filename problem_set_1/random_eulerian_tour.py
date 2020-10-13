
    # We should take our list of nodes and start with 8 nodes
    vertices = []
    # pick two random nodes and connect them
    first_random_node = random.randrange(0, len(nodes))
    stored = nodes[first_random_node]
    del nodes[first_random_node] # deleting part of the list
    # choose a random node among the nodes that are connected
    # connect them and repeat this process until all the nodes are connected.
    while len(nodes) >= 1:
        second_random_node = random.randrange(0, len(nodes))
        secondNode = nodes[second_random_node]
        del nodes[second_random_node]
        edge = (stored, secondNode)
        vertices.append(edge)
        stored = secondNode
        # classify all the nodes as being odd or even.
    
    # then pick a node in the set of nodes with odd degree
    lastEdge = (vertices[len(vertices) - 1][1], vertices[0][0])
    # connect it with another node that has odd degree
    vertices.append(lastEdge)
    # These both now have even degree
    return vertices