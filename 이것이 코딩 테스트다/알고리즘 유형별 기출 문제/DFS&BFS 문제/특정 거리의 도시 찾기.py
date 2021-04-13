import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)

dist = [-1] * (n + 1)
dist[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next in graph[now]:
        if dist[next] == -1:
            dist[next] = dist[now] + 1
            q.append(next)

check = False

for i in range(1, n + 1):
    if dist[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
