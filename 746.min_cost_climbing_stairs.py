#746. Min Cost Climbing Stairs
cost = [10, 15, 20]
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
def min_cost(cost):
	n=len(cost)
	dp=[None]*(n)
	if n==1:
		return cost[0]

	dp[0]=cost[0]
	dp[1]=cost[1]

	for i in range(2,n):
		dp[i]=min(dp[i-1],dp[i-2])+cost[i]

	return min(dp[n-1],dp[n-2])
	print (dp)
print (min_cost(cost))
