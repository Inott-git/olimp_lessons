import sys


graf = {
    '1':set(['2','4']),
    '2':set(['1','5','3']),
    '3':set(['2','5']),
    '4':set(['1']),
    '5':set(['2','3'])
}
def dfs(graf, start, visited={}):
        visited[start]=True
        for i in graf[start]:
            if i not in visited.keys():
                dfs(graf, i, visited)
        return visited

print(dfs(graf, '1'))

