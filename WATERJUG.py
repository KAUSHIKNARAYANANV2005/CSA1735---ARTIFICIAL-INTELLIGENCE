
from collections import deque

def water_jug():
    capacity1 = 4
    capacity2 = 3
    start = (0, 0)

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()

        if a == 2 or b == 2:
            print("Solution:")
            for state in path:
                print(state)
            return

        amount = min(a, capacity2 - b)
        amount2 = min(b, capacity1 - a)

        states = [
            (capacity1, b),
            (a, capacity2),
            (0, b),
            (a, 0),
            (a - amount, b + amount),
            (a + amount2, b - amount2)
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

water_jug()
