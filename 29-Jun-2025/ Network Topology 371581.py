# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

n, m = map(int, input().split())
    deg = [0] * (n + 1)

    for _ in range(m):
        u, v = map(int, input().split())
        deg[u] += 1
        deg[v] += 1

    degs = deg[1:] 

    # Check Bus
    if m == n - 1 and degs.count(1) == 2 and degs.count(2) == n - 2:
        print("bus topology")
    # Check Ring
    elif m == n and degs.count(2) == n:
        print("ring topology")
    # Check Star
    elif m == n - 1 and degs.count(1) == n - 1 and degs.count(n - 1) == 1:
        print("star topology")
    else:
        print("unknown topology")
