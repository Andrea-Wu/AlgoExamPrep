def main(graph):
    #graph is a List(List) and of outbound edges

    #create array to hold topologically sorted elements
    topSorted = []

    #create a Dict(List) of inbound edges
    inbound = {}

    #Dict(List) of outbound edges (basically a dictionary version of graph)
    outbound = {}

    for g in range(len(graph)):
        inbound[g] = []

    for i in range(len(graph)):
        outbound[i] = graph[i]
        for dest in graph[i]:
            inbound[dest].append(i)

    print("inbound dict:")
    print(inbound)

    while outbound:
        #find an array in "inbound" that is empty (aka no incoming edges)
        #add that i to "topsorted"
        for i, vals in inbound.items():
            if len(vals) == 0:
                #add i to "topsorted"
                topSorted.append(i)
                #remove array from inbound
                inbound.pop(i)
                
                #go thru graph[i] to find out which "g" is/was coming out of node i
                #remove those from "inbound"
                for g in outbound[i]:
                    inbound[g].remove(i)
                #pop i from outbound
                outbound.pop(i)
                break

    print(topSorted)

if __name__ == "__main__":
    main([[2],[0,2],[]])
