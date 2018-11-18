def main(graph):
    #use parent array and bfs
    # graphs are represented like graph=[[1,2][0,2][0,1]]
    #assume the graph is strongly connected
    q = []
    parent = {}

    #bfs thru the array
    q.append(0)
    parent[0] = 0

    while q:
        node = q.pop(0)
        for child in graph[node]:
            if child in parent:
                return False
            else:
                parent[child] = node
                q.append(child)

    return True


if __name__ == "__main__":
    print(main(graph=[[1,2],[],[]]))
