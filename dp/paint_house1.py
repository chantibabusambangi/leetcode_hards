'''
There is a row of N houses, each house can be painted with one of the three colors: 
red, blue or green. The cost of painting each house with a certain color is different. 
You have to paint all the houses such that no two adjacent houses have the same color. Find the minimum cost to paint all houses.
The cost of painting each house in red, blue or green colour is given in the array r[], g[] and b[] respectively.
Example 1:
Input:
N = 3
r[] = {1, 1, 1}
g[] = {2, 2, 2}
b[] = {3, 3, 3}
'''
#idea is easy dp keep track of R,G,B values
if(N==0):
  return 0
R,G,B=r[0],g[0],b[0]
for i in range(1,N):
  new_R=r[i]+min(G,B)
  new_B=b[i]+min(R,G)
  new_G=g[i]+min(R,B)
  R,G,B=new_R,new_G,new_B
return min((R,G,B))
