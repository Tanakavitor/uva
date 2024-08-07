import java.util.*;

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
            int num_guest = Integer.parseInt(scanner.nextLine().trim());
            List<List<Integer>> adjList = new ArrayList<>();
            for (int i = 0; i < num_guest; i++) {
                adjList.add(new ArrayList<>());
            }

            for (int i = 0; i < num_guest; i++) {
                String[] relation = scanner.nextLine().trim().split(" ");
                int p = Integer.parseInt(relation[0]);
                for (int j = 1; j <= p; j++) {
                    int enemy = Integer.parseInt(relation[j]) - 1;
                    if (enemy < num_guest) {
                        adjList.get(i).add(enemy);
                        adjList.get(enemy).add(i);
                    }
                }
            }

            int[] color = new int[num_guest];
            Arrays.fill(color, -1);
            int maxInvited = 0;

            for (int i = 0; i < num_guest; i++) {
                if (color[i] == -1) {
                    Queue<Integer> queue = new LinkedList<>();
                    queue.add(i);
                    color[i] = 0;
                    int[] colorCount = new int[2];
                    colorCount[0]++;

                    boolean isBipartite = true;

                    while (!queue.isEmpty()) {
                        int u = queue.poll();
                        for (int v : adjList.get(u)) {
                            if (color[v] == -1) {
                                color[v] = 1 - color[u];
                                colorCount[color[v]]++;
                                queue.add(v);
                            } else if (color[v] == color[u]) {
                                isBipartite = false;
                            }
                        }
                    }

                    if (isBipartite) {
                        maxInvited += Math.max(colorCount[0], colorCount[1]);
                    }
                }
            }

            System.out.println(maxInvited);
            if (testCases > 0) {
                scanner.nextLine(); // Skip blank line between test cases
            }
        }
    }
}