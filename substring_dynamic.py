def main(s1, s2):
    #use dynamic programming to find the longest subsequence in two sentences

    arr1 = s1.split()
    arr2 = s2.split()

    len1 = len(arr1)
    len2 = len(arr2)

    #memo[][] will be of size len1 x len2 
    #memo[i][j] will store the longest subsequence between s1[0,i] and s2[0,j]
    #i < len1; j < len2
    #I don't think it would be a problem to init all indices to -1
    memo = [[ -1 for j in range(len2)] for i in range(len1)]

    for i in range(len1):
        if s2[0] == s1[0]:
            memo[i][0] = 1

    for j in range(len2):
        if s1[0] == s2[0]:
            memo[0][j] = 1

    for i in range(1,len1):
        for j in range(1,len2):
            if arr1[i] == arr2[j]:
                print(memo[i-1][j-1])
                memo[i][j] = memo[i-1][j-1] + 1
                print("hello?")
            else:
                memo[i][j] = max(memo[i][j-1], memo[i-1][j])

    return memo[len1-1][len2-1]


if __name__ == "__main__":
    print(main("I really hate algorithms", "I hate algorithms with a burning passion"))
