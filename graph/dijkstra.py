
graph = {}
graph["start"] = {"a": 6, "b": 2}
graph["a"] = {"fin": 1}
graph["b"] = {"a": 3, "fin": 5}
graph["fin"] = {}

infinity = float("inf")
costs = {"a": 6, "b": 2, "fin": infinity}

parents = {"a": "start", "b": "start", "fin": None}

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_node = node
    return lowest_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors:
        new_cost = cost + neighbors[n]
        if n not in costs or new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node

    processed.append(node)
    node = find_lowest_cost_node(costs)



path = []
node = "fin"
while node != "start": 
    path.insert(0, node)
    node = parents[node]
path.insert(0, "start") 

print("Shortest path from start to fin:", path)
