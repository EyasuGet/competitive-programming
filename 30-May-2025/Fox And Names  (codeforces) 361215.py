# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import defaultdict, deque

def fox_and_names(names):
    graph = defaultdict(set)
    in_degree = [0] * 26
    used = [False] * 26

    for i in range(len(names) - 1):
        w1, w2 = names[i], names[i+1]
        min_len = min(len(w1), len(w2))
        found_diff = False

        for j in range(min_len):
            c1, c2 = w1[j], w2[j]
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    in_degree[ord(c2) - ord('a')] += 1
                found_diff = True
                break

        if not found_diff and len(w1) > len(w2):
            return "Impossible"

        for ch in w1 + w2:
            used[ord(ch) - ord('a')] = True

    queue = deque()
    for i in range(26):
        if in_degree[i] == 0 and used[i]:
            queue.append(chr(i + ord('a')))

    result = []
    while queue:
        current = queue.popleft()
        result.append(current)
        for neighbor in graph[current]:
            in_degree[ord(neighbor) - ord('a')] -= 1
            if in_degree[ord(neighbor) - ord('a')] == 0:
                queue.append(neighbor)

    if len(result) != sum(used):
        return "Impossible"

    for i in range(26):
        if not used[i]:
            result.append(chr(i + ord('a')))

    return ''.join(result)

n = int(input())
names = [input().strip() for _ in range(n)]
print(fox_and_names(names))
