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

        public boolean union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX == rootY) {
                return false; // Already in the same set
            }
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
            return true;
        }

        public boolean areConnected(int x, int y) {
            return find(x) == find(y);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        UnionFind friends = new UnionFind(n * 2);
        UnionFind enemies = new UnionFind(n * 2);

        while (true) {
            int c = scanner.nextInt();
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            if (c == 0 && x == 0 && y == 0) break;

            int fx = friends.find(x);
            int fy = friends.find(y);
            int ex = friends.find(x + n);
            int ey = friends.find(y + n);

            switch (c) {
                case 1: // setFriends
                    if (fx == ey || fy == ex) {
                        System.out.println("-1");
                    } else {
                        friends.union(fx, fy);
                        friends.union(ex, ey);
                    }
                    break;
                case 2: // setEnemies
                    if (fx == fy) {
                        System.out.println("-1");
                    } else {
                        friends.union(fx, ey);
                        friends.union(fy, ex);
                    }
                    break;
                case 3: // areFriends
                    System.out.println(friends.areConnected(fx, fy) ? "1" : "0");
                    break;
                case 4: // areEnemies
                    System.out.println(friends.areConnected(fx, ey) ? "1" : "0");
                    break;
            }
        }
        scanner.close();
    }
}
