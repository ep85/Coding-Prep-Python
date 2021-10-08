'''

Depth First Traversal (or Search) for a graph is similar to Depth First Traversal of a tree. 
The only catch here is, unlike trees, graphs may contain cycles, a node may be visited twice. 
To avoid processing a node more than once, use a boolean visited array. 

Summary - 
  Searches all the way down one path before going to the next

'''


# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict
  
# This class represents a directed graph using
# adjacency list representation
  
  
class Graph:
  
    # Constructor
    def __init__(self):
  
        # default dictionary to store graph
        self.graph = defaultdict(list)
  
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
  
    # A function used by DFS
    def DFSUtil(self, v, visited):
  
        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')
  
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
  
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):
  
        # Create a set to store visited vertices
        visited = set()
  
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)
  
# Driver code
  
  
# Create a graph given
# in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
  
print("Following is DFS from (starting from vertex 2)")
g.DFS(2)

# Following is Depth First Traversal (starting from vertex 2)
# 2 0 1 3


'''

https://leetcode.com/problems/course-schedule/

Interview Problem

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visitSet = set()
        def dfs():
            if crs in visitSet:
                return False
            if preMap[crs] == []
                return True
            
            visitSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return false
        return True