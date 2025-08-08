'''
2360. Longest Cycle in a Graph
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.
The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i].
If there is no outgoing edge from node i, then edges[i] == -1.
Return the length of the longest cycle in the graph. If no cycle exists, return -1.
A cycle is a path that starts and ends at the same node.
'''
#idea is given a node can have atmost one outgoing edge, we can use dfs here
def longestCycle(self, edges: List[int]) -> int:
  #dfs 
  visited=set()
  self.ans=-1  #no cycle yet
  def dfs(i,path,level):
      if(i in visited):
          return
      path[i]=level
      child=edges[i]
      if(child==-1 or child in visited):
          del path[i]
          visited.add(i)
          return
      if(child in path):
          child_level=path[child]
          self.ans=max(self.ans,level-child_level+1)
          del path[i]
          visited.add(i)
          return
      dfs(child,path,level+1)
      visited.add(i)
      del path[i] #to allow dfs after completing dfs 
  for i in range(len(edges)):
      if(i not in visited):
          dfs(i,{},0)
  return self.ans
  #TC: O(n)
  #space:O(n)
