import math
def main(graph, target):
    #implement Bellman-Ford algorithm
    #wtf is the bellman ford algorithm
    #for each vertex, send a "message" about the shortest path to that node that we know so far
    #the order in which the messages are sent is fixed
    #we must send |V|-1 messages (same as the # of nodes)

    #first we should figure out how to represent this. I will use an "adjacency linked list"
    #this example graph is taken from the emory website
    #as you see, node 0 is connected to node 1 with weight 3
    #           and node 0 is connected to node 3 with weight 2
    #           and node 0 is connected to node 8 with weight 4
    #([[[3,8],[1,4]] , [2,1] , [3,1] , []])

    #for this example I'm going to assume this is a directed graph. 
    #actually i'm wondering if bellman ford has any purpose if the graph is acyclic
    dist = {}

    #init distance to source node = 0
    dist[0] = 0
    #initialize each distance to infinity? maybe not necessary?
    for i in range(1,len(graph)):
        dist[i] = math.inf

    for i in range(len(graph) -1):
        for node in range(len(graph) -1):
            #send a message from each node to it's childs
            for child in graph[node]:
                childNum = child[0]
                childDist = child[1]
                dist[childNum] = min(dist[childNum], dist[node] + childDist )

    return dist[target]

if __name__ == "__main__":
    print(main([[[3,5], [1,4]], [[2,1]], [[3,1]], [[]]], 3))
