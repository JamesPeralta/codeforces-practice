from collections import deque, defaultdict
class Solution:
    def bfs(self, adj_list, start):
        # u: z
        dist_map = {start: 0}
        q = deque([start])
        seen = set([start])
        dist = 1
        while len(q):
            for _ in range(len(q)):
                node = q.popleft()
                neighbs = adj_list[node]
                for neighb in neighbs:
                    if neighb in seen:
                        continue
                    q.append(neighb)
                    seen.add(neighb)
                    dist_map[neighb] = dist

            dist += 1
        return dist_map
    
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        
        x_dist = self.bfs(adj_list, x)
        # print(x_dist)
        y_dist = self.bfs(adj_list, y)
        z_dist = self.bfs(adj_list, z)
        result = 0
        for i in range(n):
            tmp = []
            tmp.append(x_dist[i])
            tmp.append(y_dist[i])
            tmp.append(z_dist[i])
            tmp.sort()
            if tmp[0]**2 + tmp[1]**2 == tmp[2]**2:
                # print(i, tmp[0]**2, tmp[1]**2,tmp[2]**2)
                result += 1
        return result

"""
Determine the number of special nodes!!

x, y, z - distance
sort distances

for every u 

a^2 + b^2 = c^2
"""







