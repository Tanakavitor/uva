def bfs(G, start, ttl):
    marked = {node: False for node in G.keys()}
    distance = {node: float('inf') for node in G.keys()}
    
    queue = [start]
    marked[start] = True
    distance[start] = 0
    
    while queue:
        v = queue.pop(0)
        for w in G[v]:
            if not marked[w]:
                marked[w] = True
                distance[w] = distance[v] + 1
                if distance[w] <= ttl:
                    queue.append(w)
    
    unreachable_count = sum(1 for dist in distance.values() if dist > ttl)
    return unreachable_count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    case_number = 1
    
    while idx < len(data):
        connections = int(data[idx])
        idx += 1
        
        if connections == 0:
            break
        
        G = {}
        
        for _ in range(connections):
            u, v = int(data[idx]), int(data[idx+1])
            idx += 2
            if u not in G:
                G[u] = []
            if v not in G:
                G[v] = []
            G[u].append(v)
            G[v].append(u)
        
        while True:
            start, ttl = int(data[idx]), int(data[idx+1])
            idx += 2
            
            if start == 0 and ttl == 0:
                break
            
            if start not in G:
                unreachable_count = len(G)
            else:
                unreachable_count = bfs(G, start, ttl)
            
            print(f"Case {case_number}: {unreachable_count} nodes not reachable from node {start} with TTL = {ttl}.")
            case_number += 1

if __name__ == "__main__":
    main()
