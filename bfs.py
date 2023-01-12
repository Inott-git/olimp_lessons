from smezh import smezh
A = [[0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0]]
queue = []
def bfs(graf, start):
    visited = set()
    visited.add(start)
    queue.append(start)
    while queue:
        x = queue.pop()
        print('x = ', x)
        for w in graf[x]:
            if w not in visited:
                visited.add(w)
                queue.append(w)
bfs(A, 1)