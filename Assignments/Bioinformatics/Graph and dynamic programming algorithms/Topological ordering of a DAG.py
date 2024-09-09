"""
참고 사이트: https://www.algotree.org/algorithms/tree_graph_traversal/lexical_topological_sort_python/
"""


# Find topological ordering of a directed acyclic graph (DAG).
def topological_ordering(textfile):
    """
    >>> topological_ordering('data01.txt')
    (1, 4, 5, 2, 3)
    """

    adjacency = {}  # store the graph in an adjacency list
    nodes = []

    with open(textfile) as txt:
        for line in txt:
            start, end = line.strip().split(' -> ')
            end = end.split(',')
            nodes += start, *end
            adjacency[start] = end

    # calculate the indegree of each node
    indegree = {key: 0 for key in set(nodes)}  # key= node, value= indegree (default=0)
    for end in list(adjacency.values()):
        for node in end:
            indegree[node] += 1    # increase the indegree of ending nodes

    # choose nodes without predecessors (indegree = 0)
    zero_indegree = [start for start, end in list(adjacency.items()) if indegree[start] == 0]

    # repeat until no nodes left
    topo_order = []
    while zero_indegree:
        node = zero_indegree.pop(0)  # remove node with zero indegree
        topo_order.append(node)  # and add it to ordered list

        if node in adjacency:
            for end in adjacency[node]:
                indegree[end] -= 1    # decrease the indegree of its ending nodes
                if indegree[end] == 0:  # add node with zero indegree (newly created)
                    zero_indegree.append(end)

    return tuple(map(int, topo_order))


if __name__ == '__main__':
    import doctest
    doctest.testmod()