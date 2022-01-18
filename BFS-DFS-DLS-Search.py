
graph = {1: set([2, 3]),
         2: set([ 1, 4, 5]),
         3: set([1, 6]),
         4: set([2]),
         5: set([2, 6]),
         6: set([3, 5])}
#Binary three


# A function to perform a Depth-Limited search
def DLS(src,target,maxDepth):
  
    if src == target : 
        return True 
    if maxDepth <= 0 : 
        return False
    for i in graph[src]:
            if(DLS(i,target,maxDepth-1)):
                return True
    return False
  
# A function to perform a Iterative Deepening Search
def IDDFS(src, target, maxDepth):
    for i in range(maxDepth):
        if (DLS(src, target, i)):
            return True
    return False

# A function to perform a Depth-First Search
def dfs(graph, start, visited=[]): 
    visited.append(start)
    for next in graph[start] - set(visited): 
        dfs(graph, next, visited)
    return visited

# A function to perform a Breadth-first Search
def bfs(graph, start):
    visited, queue = [], [start] 
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex] - set(visited)) 
    return visited


print("Which search algorith do you want to use? ")
print("Choose one: \n 1- Breadth-first Search \n 2- Depth-First Search  \n 3- Depth-limited Search \n 4- Iterative Deepening Search")
value = int(input())

if value == 1:
    print(bfs(graph, 'A'))
elif value == 2 :
    print(dfs(graph, 'A'))
elif value == 3: 
    print(" Give me target value: ")
    target = int(input())
    print("Give me maxDepth: ")
    maxDepth = int(input())
    print("Give me start point: ")
    src = int(input())
    print(DLS(src,target,maxDepth))
elif value == 4:
    print(" Give me target value: ")
    target = int(input())
    print("Give me maxDepth: ")
    maxDepth = int(input())
    print("Give me start point: ")
    src = int(input())
    print(IDDFS(src, target, maxDepth)) 



