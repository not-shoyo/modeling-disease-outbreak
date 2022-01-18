'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
inp = input().split()
n, m = int(inp[0]), int(inp[1])
edgesAndWeights = []

for i in range(m):
    val = input().split()
    a, b, w = int(val[0])-1, int(val[1])-1, int(val[2])
    edgesAndWeights.append([a,b,w])


def myFunc(e):
    return e[2]
edgesAndWeights.sort(key=myFunc)

unionList, height = [i for i in range(m)], [1 for i in range(m)]

def root(a: int):
    x = unionList[a]
    while x != unionList[x]:
        unionList[x] = unionList[unionList[x]]
        x = unionList[x]
    return x

def union(a: int, b: int):
    rootA, rootB = root(a), root(b)
    heightA, heightB = height[rootA], height[rootB]
    if heightA > heightB:
        unionList[rootB] = rootA
        heightA += heightB
    else:
        unionList[rootA] = rootB
        heightB += heightA

cost = 0
for edge in edgesAndWeights:
    if root(edge[0]) == root(edge[1]):
        continue
    union(edge[0], edge[1])
    cost += edge[2]

print(cost)










