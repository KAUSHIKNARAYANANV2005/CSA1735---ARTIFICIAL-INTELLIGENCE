
import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

h = {'A': 4, 'B': 3, 'C': 1, 'D': 0}

def astar(start, goal):
    queue = [(h[start], 0, start, [start])]
    best = {start: 0}

    while queue:
        f, g, node, path = heapq.heappop(queue)

        if node == goal:
            print("Path:", path)
            print("Cost:", g)
            return

        if g > best[node]:
            continue

        for neighbor, weight in graph[node]:
            new_g = g + weight

            if new_g < best.get(neighbor, float('inf')):
                best[neighbor] = new_g
                new_f = new_g + h[neighbor]
                heapq.heappush(
                    queue,
                    (new_f, new_g, neighbor,
                     path + [neighbor])
                )

astar('A', 'D')
