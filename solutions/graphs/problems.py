"""
Graphs — Interview Problems
=============================
BFS, DFS, Union-Find, topological sort, shortest paths.
"""
from typing import List, Optional
from collections import deque, defaultdict


# ─────────────────────────────────────────────────────────────────────────────
# 1. Number of Islands
# Count connected components of '1's in a grid.
# Time: O(m*n)  Space: O(m*n)
# ─────────────────────────────────────────────────────────────────────────────
def num_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'  # mark visited
        dfs(r + 1, c); dfs(r - 1, c); dfs(r, c + 1); dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    return count


# ─────────────────────────────────────────────────────────────────────────────
# 2. Clone Graph
# Deep copy of undirected graph.
# Time: O(V+E)  Space: O(V)
# ─────────────────────────────────────────────────────────────────────────────
class GraphNode:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors or []


def clone_graph(node: Optional[GraphNode]) -> Optional[GraphNode]:
    if not node:
        return None
    clones = {}

    def dfs(n):
        if n in clones:
            return clones[n]
        clone = GraphNode(n.val)
        clones[n] = clone
        for neighbor in n.neighbors:
            clone.neighbors.append(dfs(neighbor))
        return clone

    return dfs(node)


# ─────────────────────────────────────────────────────────────────────────────
# 3. Course Schedule (Cycle Detection)
# Can you finish all courses given prerequisites? (Topological sort / cycle detect)
# Time: O(V+E)  Space: O(V+E)
# ─────────────────────────────────────────────────────────────────────────────
def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    # 0 = unvisited, 1 = visiting, 2 = visited
    state = [0] * num_courses

    def dfs(course):
        if state[course] == 1:
            return False  # cycle
        if state[course] == 2:
            return True
        state[course] = 1
        for prereq in graph[course]:
            if not dfs(prereq):
                return False
        state[course] = 2
        return True

    return all(dfs(c) for c in range(num_courses))


# ─────────────────────────────────────────────────────────────────────────────
# 4. Walls and Gates (Multi-source BFS)
# Fill each empty room with distance to nearest gate.
# -1 = wall, 0 = gate, INF = empty room
# Time: O(m*n)  Space: O(m*n)
# ─────────────────────────────────────────────────────────────────────────────
def walls_and_gates(rooms: List[List[int]]) -> None:
    INF = float('inf')
    rows, cols = len(rooms), len(rooms[0])
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))


# ─────────────────────────────────────────────────────────────────────────────
# 5. Dijkstra's Shortest Path
# Time: O((V+E) log V)  Space: O(V)
# ─────────────────────────────────────────────────────────────────────────────
import heapq

def dijkstra(graph: dict, start: int, end: int) -> int:
    """
    graph = {node: [(cost, neighbor), ...]}
    Returns shortest distance from start to end, or -1 if unreachable.
    """
    dist = {start: 0}
    heap = [(0, start)]
    while heap:
        cost, node = heapq.heappop(heap)
        if node == end:
            return cost
        if cost > dist.get(node, float('inf')):
            continue
        for edge_cost, neighbor in graph.get(node, []):
            new_cost = cost + edge_cost
            if new_cost < dist.get(neighbor, float('inf')):
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    return -1


# ─────────────────────────────────────────────────────────────────────────────
# 6. Union-Find (Disjoint Set Union)
# Efficient union and find with path compression + rank.
# ─────────────────────────────────────────────────────────────────────────────
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1
        return True


# ─────────────────────────────────────────────────────────────────────────────
# 7. Word Ladder (BFS shortest transformation)
# Time: O(M² * N) M = word length, N = wordList size
# ─────────────────────────────────────────────────────────────────────────────
def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    word_set = set(word_list)
    if end_word not in word_set:
        return 0
    queue = deque([(begin_word, 1)])
    visited = {begin_word}
    while queue:
        word, steps = queue.popleft()
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i + 1:]
                if new_word == end_word:
                    return steps + 1
                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, steps + 1))
    return 0
