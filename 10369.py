import math

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            if self.rank[xroot] < self.rank[yroot]:
                self.parent[xroot] = yroot
            elif self.rank[xroot] > self.rank[yroot]:
                self.parent[yroot] = xroot
            else:
                self.parent[yroot] = xroot
                self.rank[xroot] += 1

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0

    n = int(data[idx])
    idx += 1

    results = []

    for _ in range(n):
        s = int(data[idx])
        p = int(data[idx + 1])
        idx += 2

        outposts = []
        for _ in range(p):
            x = int(data[idx])
            y = int(data[idx + 1])
            outposts.append((x, y))
            idx += 2

        edges = []
        for i in range(p):
            for j in range(i + 1, p):
                dist = distance(outposts[i], outposts[j])
                edges.append((dist, i, j))
        edges.sort()

        uf = UnionFind(p)
        mst_edges = []
        for edge in edges:
            d, u, v = edge
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                mst_edges.append(d)

        if s >= p:
            results.append("0.00")
        else:
            results.append(f"{mst_edges[p - s - 1]:.2f}")

    print("\n".join(results))

if __name__ == "__main__":
    main()