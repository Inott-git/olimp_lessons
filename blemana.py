class Graph:
    def __init__(self, verticals):
        self.V = verticals
        self.graph = []

    def addEage(self, start, finish, weight):
        self.graph.append([start, finish, weight])

    def printGraph(self, graph):
        for start, finish, weight in graph:
            print(f'From {start} to {finish}, weight = {weight}')

    def blemanAlgorithm(self, start):
        dict = float('Inf') * self.V
        dict[start] = 0
        for i in range(self.V - 1):
            for s, f, w in self.graph:
                if dict[s] != float('Inf') and dict[s] + w < dict[f]:
                    dict[f] = dict[s] + w
        for s, f, w in self.graph:
                if dict[s] != float('Inf') and dict[s] + w < dict[f]:
                    print('Negetive while')
                    return

        self.printGraph(dict)

verticals = int(input())
rebrs = int(input())
graph = Graph(verticals)
for i in range(rebrs):
    start, finish, weight = map(int, input(f'{i} - Start, Finish, Weight:').split())
    graph.addEage(start, finish, weight)

