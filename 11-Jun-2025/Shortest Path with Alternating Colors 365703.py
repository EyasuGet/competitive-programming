# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        RED, BLUE = 0, 1

        graph = [defaultdict(list), defaultdict(list)]
        for u, v in redEdges:
            graph[RED][u].append(v)
        for u, v in blueEdges:
            graph[BLUE][u].append(v)

        res = [-1] * n
        visited = [[False] * n for _ in range(2)]  

        q = deque()
        q.append((0, 0, -1))  

        while q:
            node, dist, prev_color = q.popleft()

            if res[node] == -1:
                res[node] = dist

            for color in [RED, BLUE]:
                if color == prev_color:
                    continue  
                for nei in graph[color][node]:
                    if not visited[color][nei]:
                        visited[color][nei] = True
                        q.append((nei, dist + 1, color))

        return res