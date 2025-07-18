'''
Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. 
The objective of the game is to end with the most stones.
Alice and Bob take turns, with Alice starting first.
On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). Initially, M = 1.
The game continues until all the stones have been taken.
Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
Example 1:
Input: piles = [2,7,9,4,4]
Output: 10
'''
#max number of stones alice can get
#can we use dp for this? yes dp+dfs
dp={} #(alice,i,M):value for alice
def dfs(alice,i,M):
    if(i==len(piles)):
        return 0
    if((alice,i,M) in dp):
        return dp[(alice,i,M)]
    res=0 if alice else float("inf")
    total=0
    for j in range(i,min(i+2*M,len(piles))):
        total+=piles[j]
        if alice:
            res=max(res,total+dfs(not alice,j+1,max(M,j-i+1))) #X=i-j+1 that picked
        else:
            res=min(res,dfs(not alice,j+1,max(M,j-i+1)))
    dp[(alice,i,M)]=res
    return dp[(alice,i,M)]
return dfs(True,0,1)
# TC=O(n*n*n)=O(n3) and Space=O(n*n)=O(n2)
