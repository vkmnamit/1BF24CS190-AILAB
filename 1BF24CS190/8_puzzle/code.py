
import heapq

def valid_state(state):
    return len(state) == 9 and sorted(state) == list(range(9))


def inversions(state):
    nums = [x for x in state if x != 0]
    count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                count += 1

    return count


def manhattan(state, goal):
    distance = 0

    for i, tile in enumerate(state):
        if tile != 0:
            j = goal.index(tile)
            r1, c1 = divmod(i, 3)
            r2, c2 = divmod(j, 3)
            distance += abs(r1 - r2) + abs(c1 - c2)

    return distance


def print_puzzle(state):
    for i in range(0, 9, 3):
        print(" ".join("_" if x == 0 else str(x)
                       for x in state[i:i + 3]))


def a_star(start, goal):
    start = tuple(start)
    goal = tuple(goal)

    pq = [(manhattan(start, goal), 0, start)]
    best_cost = {start: 0}
    parent = {start: None}

    moves = [
        (-1, 0), # Up
        (1, 0), # Down
        (0, -1), # Left
        (0, 1) # Right
    ]

    while pq:
        f, g, state = heapq.heappop(pq)

        if g != best_cost.get(state):
            continue

        if state == goal:
            path = []
            current = state

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("\nSOLUTION STEPS\n")

            for step, board in enumerate(path):
                if step == 0:
                    print("Initial State:")
                else:
                    print("Step", step, ":")

                print_puzzle(board)
                print()

            print("Goal reached!")
            print("Total moves:", len(path) - 1)
            return

        zero = state.index(0)
        r, c = divmod(zero, 3)

        for dr, dc in moves:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                pos = nr * 3 + nc
                new_state = list(state)

                new_state[zero], new_state[pos] = (
                    new_state[pos], new_state[zero]
                )

                new_state = tuple(new_state)
                new_g = g + 1

                if new_g < best_cost.get(
                    new_state, float("inf")
                ):
                    best_cost[new_state] = new_g
                    parent[new_state] = state

                    new_f = new_g + manhattan(new_state, goal)
                    heapq.heappush(
                        pq, (new_f, new_g, new_state)
                    )

    print("No solution found")


start = list(map(int, input(
    "Enter start state (9 numbers, use 0 for blank): "
).split()))

goal = list(map(int, input(
    "Enter goal state (9 numbers, use 0 for blank): "
).split()))

if not valid_state(start) or not valid_state(goal):
    print("Invalid input")
elif inversions(start) % 2 != inversions(goal) % 2:
    print("Puzzle is not solvable")
else:
    a_star(start, goal)
