import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
    static class UnionFind {
        private int[] parent;
        private int[] rank;

        public UnionFind(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
        }

        public int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        public void union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX != rootY) {
                if (rank[rootX] < rank[rootY]) {
                    parent[rootX] = rootY;
                } else if (rank[rootX] > rank[rootY]) {
                    parent[rootY] = rootX;
                } else {
                    parent[rootY] = rootX;
                    rank[rootX]++;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int testCases = Integer.parseInt(scanner.nextLine().trim());
        scanner.nextLine(); // Skip blank line

        while (testCases-- > 0) {
            char largestNode = scanner.nextLine().trim().charAt(0);
            int size = largestNode - 'A' + 1;
            UnionFind uf = new UnionFind(size);

            while (scanner.hasNextLine()) {
                String edge = scanner.nextLine().trim();
                if (edge.isEmpty()) break; // Handle multiple blank lines
                int node1 = edge.charAt(0) - 'A';
                int node2 = edge.charAt(1) - 'A';
                uf.union(node1, node2);
            }

            Set<Integer> uniqueRoots = new HashSet<>();
            for (int i = 0; i < size; i++) {
                uniqueRoots.add(uf.find(i));
            }

            System.out.println(uniqueRoots.size());
            if (testCases > 0) System.out.println(); // Print blank line between outputs
        }
    }
}
