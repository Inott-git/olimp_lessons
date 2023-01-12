def smezh(v, e):
    #v, e = map(int, input('Вершины и ребра:').split())
    v += 1
    A = [[0]*v for i in range(v)]
    for i in range(e):
        a, b = map(int, input(f'Ребро {i+1}: ').split())
        A[a][b] = 1
        A[b][a] = 1 #не ориентерованный
    for item in A:
        print(item)
    return A
