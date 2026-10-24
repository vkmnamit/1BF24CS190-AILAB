import heapq

def astar(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while pq:
        f, g, node = heapq.heappop(pq)

        # Ignore outdated queue entries
        if g != cost.get(node):
            continue

        if node == goal:
            path = []
            current = goal

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path, g

        for neighbor, edge_cost in graph.get(node, []):
            new_cost = g + edge_cost

            if new_cost < cost.get(neighbor, float("inf")):
                cost[neighbor] = new_cost
                parent[neighbor] = node

                new_f = new_cost + heuristic[neighbor]
                heapq.heappush(
                    pq, (new_f, new_cost, neighbor)
                )

    return None, None


def main():
    graph = {}
    heuristic = {}

    n = int(input("Enter number of nodes: "))

    for i in range(n):
        node, h = input(
            "Enter node and heuristic (e.g. A 3): "
        ).split()

        heuristic[node] = int(h)
        graph[node] = []

    m = int(input("Enter number of edges: "))

    for i in range(m):
        u, v, w = input(
            "Enter edge (from to cost): "
        ).split()

        graph[u].append((v, int(w)))

    start = input("Enter start node: ")
    goal = input("Enter goal node: ")

    if start not in graph or goal not in graph:
        print("Invalid start or goal node.")
        return

    path, total_cost = astar(
        graph, heuristic, start, goal
    )

    if path:
        print("Path:", " -> ".join(path))
        print("Total cost:", total_cost)
    else:
        print("No path found.")


main()