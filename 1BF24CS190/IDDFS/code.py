def dls(graph, node, goal, depth, path):
    if node == goal:
        return path

    if depth == 0:
        return None

    for neighbor in graph[node]:
        if neighbor not in path:
            result = dls(
                graph, neighbor, goal,
                depth - 1, path + [neighbor]
            )

            if result:
                return result

    return None


def main():
    graph = {}

    n = int(input("Enter number of edges: "))

    for i in range(n):
        u, v = input("Enter edge (u v): ").split()

        graph.setdefault(u, []).append(v)
        graph.setdefault(v, [])

    start = input("Enter start node: ")
    goal = input("Enter goal node: ")
    max_depth = int(input("Enter maximum depth: "))

    for depth in range(max_depth + 1):
        result = dls(graph, start, goal, depth, [start])

        if result:
            print("Path:", " -> ".join(result))
            print("Depth:", len(result) - 1)
            return

    print("Goal not found")


if __name__ == "__main__":
    main()
