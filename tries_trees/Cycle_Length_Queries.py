'''
You are given an integer n. There is a complete binary tree with 2n - 1 nodes. The root of that tree is the node with the value 1, 
and every node with a value val in the range [1, 2n - 1 - 1] has two children where:
The left node has the value 2 * val, and
The right node has the value 2 * val + 1.
You are also given a 2D integer array queries of length m, where queries[i] = [ai, bi]. For each query, solve the following problem:
Add an edge between the nodes with values ai and bi.
Find the length of the cycle in the graph.
Remove the added edge between nodes with values ai and bi.
''' #tagged hard one of the easiest problem.
#idea : for each query we lca of a,b (length/steps) and ans=steps+1
def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
  #ggiven left, right=2*val,2*val+1
  #parent will be val/2
  #for each query we use lca of a,b ans=1+no.of steps
  res=[]
  for a,b in queries:
      steps=1  #
      while(a!=b):
          if(a>b):
              a//=2
          else:
              b//=2
          steps+=1
      res.append(steps)
  return res
