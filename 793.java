import java.util.Scanner;

public class Main {
    static class UnionFind {
        private int[] parent;
        private int[] rank;

        public UnionFind(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                rank[i] = 0;
            }
        }

        public int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]); // Path compression
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
            int n = Integer.parseInt(scanner.nextLine().trim());
            UnionFind uf = new UnionFind(n + 1);
            int successful = 0, unsuccessful = 0;

            while (scanner.hasNextLine()) {
                String line = scanner.nextLine().trim();
                if (line.isEmpty()) break; 

                String[] parts = line.split(" ");
                if (parts.length != 3) continue;

                char command = parts[0].charAt(0);
                int computer1 = Integer.parseInt(parts[1]);
                int computer2 = Integer.parseInt(parts[2]);

                if (command == 'c') {
                    uf.union(computer1, computer2);
                } else if (command == 'q') {
                    if (uf.find(computer1) == uf.find(computer2)) {
                        successful++;
                    } else {
                        unsuccessful++;
                    }
                }
            }

            System.out.println(successful + "," + unsuccessful);
            if (testCases > 0) System.out.println(); // Print blank line between outputs
        }
        scanner.close();
    }
}
