import math
def main(graph, target):
    # make a 2d table of size len(graph)
    memo = [[math.inf for x in range(len(graph))] for y in range(len(graph))]

    #fill in the base case, memo[0][i] = 0 for all i
    for x in range(1,len(graph)):
        memo[0][x] = 0

    #recursive step (or iterative, in this case)


if __name__ == "__main__":
    main()
