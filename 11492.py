import heapq
import sys

def dijkstras_algorithm(graph, start, end):
    pq = []  
    heapq.heappush(pq, (0, start, "")) 
    visited = set()  

    while pq:
        total_distance, current_vertex, last_word = heapq.heappop(pq)
        
        if current_vertex == end:
            return total_distance
        
        if (current_vertex, last_word[:1]) in visited:
            continue
        visited.add((current_vertex, last_word[:1]))

        for neighbor, word in graph.get(current_vertex, []):
            if word[0] != last_word[:1]:  
                next_distance = total_distance + len(word)
                heapq.heappush(pq, (next_distance, neighbor, word))


def main():
    data = sys.stdin.read().splitlines()
    index = 0
    while True:
        n = int(data[index])
        index += 1
        if n == 0:
            break
        
        graph = {}
        start_language, end_language = data[index].split()
        index += 1
        
        for _ in range(n):
            language1, language2, word = data[index].split()
            index += 1
            
            graph.setdefault(language1, []).append((language2, word))
            graph.setdefault(language2, []).append((language1, word))
        
        result = dijkstras_algorithm(graph, start_language, end_language)
        print("impossivel" if result == -1 else result)

if __name__ == "__main__":
    main()