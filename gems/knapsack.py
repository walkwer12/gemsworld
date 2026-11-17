#AIM 1: To implement Dynamic Problem –  KnapSack Problem

def knapsack(w, v, c):

#create empty list for calculating the maximum profit for each capacity from 0 to c
    dp = [0] * (c+1)

    for i in range(len(w)):
        for j in range(c, w[i] - 1, -1): #doing a backward range so that we acoid taking the same value twice
            dp[j] = max(dp[j], v[i] + dp[j - w[i]])
#dp[j] - keeps the existing max profit
 # v[i] is the value of the current item.
# w[i] is the weight of the current item.
# j-w[i] is the remaining capacity after selecting the item.
# dp[j-w[i]] gives the maximum profit possible with that remaining capacity.

    return dp[c]

w = list(map(int, input("Weights: "))).split()
v = list(map(int, input("Values: "))).split()
c = int(input("Maximum capacity: "))    

print("Maximum profit: ", knapsack(w, v, c))