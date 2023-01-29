from collections import deque

def dfs(st):
    tree = []
    visited = [False for _ in range(N+1)]
    # 木の深さ
    tree_depth = 0
    # 最も深い位置
    edge = st
    # From, To, Depth
    stack = [(-1,st,0)]
    while stack:
        prev, cur, depth = stack.pop()
        if visited[cur]: continue
        if prev != -1:
            tree.append((prev,cur))
            if tree_depth < depth:
                tree_depth = depth
                edge = cur
        visited[cur] = True
        for next in p[cur]:
            if not visited[next]: # not visited
                stack.append((cur, next, depth+1))
    return tree,tree_depth,edge


def bfs(st):
    tree = []
    visited = [False for _ in range(N+1)]
    queue = deque([st])
    visited[st] = True
    while queue:
        cur = queue.popleft()
        for next in p[cur]:
            if not visited[next]: # not visited
                visited[next] = True
                tree.append((cur, next))
                queue.append(next)
    return tree

N,M = [int(x) for x in input().split()]
p = [set() for _ in range(N+1)]
for _ in range(M):
    u,v = [int(x) for x in input().split()]
    p[u].add(v)
    p[v].add(u)


t1,d1,e1 = dfs(1)
t2 = bfs(1)

for path in t1:
    print(*path)

for path in t2:
    print(*path)
