def mcm(p):
    n = len(p) - 1 #calculate number of matrix
    dp = [[0]*n for _ in range(n)] #creates a 2d table to store the minimum multiplication cost for different group of matrices

    for length in range(2, n+1): #controls the length of the matrix chain being considered
        for i in range(n-length + 1): #determines starting position of matrix chain
            j = i + length - 1 #calculating ending index of current chain

            dp[i][j] = min(dp[i][k] + dp[k+1][j] + p[i]*p[k+1] * p[j+1]
                            for k in range(i, j))

        return dp[0][n-1]
    p = [10, 20, 30, 40]

    print("Minimum cost of multiplications is:", mcm(p))