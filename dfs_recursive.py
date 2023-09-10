graph = {
  'A':['B','C','D'],
  'B':['E'],
  'C':['D','E'],
  'D':[],
  'E':[]
}
visited = set()

def dfs(visited,graph,root):
  if root not in visited:
    print(root)
    visited.add(root)
    for neighbor in graph[root]:
      dfs(visited,graph,neighbor)
