#!/usr/bin/python

'''
This problem was asked by Google.

In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most frequently-occurring letter along that path.
For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges, return the largest value path of the graph. If the largest value is infinite, then return null.

The graph is represented with a string and an edge list. The i-th character represents the uppercase letter of the i-th node.
Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node. Self-edges are possible, as well as multi-edges.

For example, the following input graph:

ABACA
[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]
Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

The following input graph:

A
[(0, 0)]
Should return null, since we have an infinite loop.
'''

'''
#My solution
#Worked for both the cases
#Check for the solution, it is easy compared to mine
from collections import defaultdict

def getGraph(edges):
    graph = defaultdict(set)

    for origin,destination in edges:
        if origin in graph:
            graph[origin].add(destination)
        else:
            graph[origin] = {destination}

    for origin,destination in edges:
        if destination in graph:
            graph[destination].add(origin)
        else:
            graph[destination] = {origin}
            
    return graph

def getVertices(graph):
    return graph.keys()

pathLen = {}

def dfsPaths(graph,start,goal):
    stack = [(start,[start])]
    while stack:
        (vertex,path) = stack.pop()
        for next in graph[vertex]-set(path):
            if next == goal:
                path = path + [next]
                pathLen[len(path)] = path
            else:
                stack.append((next,path + [next]))

def getPaths(start,goal):
    dfsPaths(graph,start,goal)

def getPathsCombinations(string,vertices):
    for i in range(len(vertices)):
        for j in range(i+1,len(vertices)):
            getPaths(i,j)

    if pathLen:
        largestValuePath = pathLen[sorted(pathLen.keys())[-1]]
    else:
        return None

    dict = {}
    
    if len(string) == len(largestValuePath):
        for i in string:
            if i in dict:
                dict[i]+= 1
            else:
                dict[i] = 1
    else:
        return 0

    largestValue = sorted(dict.values())[-1]
    return largestValue
    #print(list(dict.keys())[list(dict.values()).index(largestValue)])

edges = [(0, 1),
         (0, 2),
         (2, 3),
         (3, 4)]
string = "ABACA"

edges = [(0,0)]
string = "A"

graph = getGraph(edges)
vertices = getVertices(graph)
print(getPathsCombinations(string,vertices))
'''
