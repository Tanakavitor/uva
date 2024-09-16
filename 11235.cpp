#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <limits.h>
#define INVALID INT_MIN

using namespace std;
typedef vector<int> vi;

class SegmentTree {
  private:
    vi tree;
    int *frequencyArray, *originalArray, arraySize;
    int treeSize;

    void buildTree(int node, int start, int end) {
      if (start == end) {
        tree[node] = frequencyArray[start];
      } else {
        int mid = (start + end) / 2;
        int leftChild = 2 * node;
        int rightChild = 2 * node + 1;
        buildTree(leftChild, start, mid);
        buildTree(rightChild, mid + 1, end);
        tree[node] = max(tree[leftChild], tree[rightChild]);
      }
    }

    int queryTree(int node, int start, int end, int i, int j) {
      if (i > end || j < start) return INVALID;
      if (start >= i && end <= j) return tree[node];
      int mid = (start + end) / 2;
      int leftResult = queryTree(2 * node, start, mid, i, j);
      int rightResult = queryTree(2 * node + 1, mid + 1, end, i, j);
      return max(leftResult, rightResult);
    }

  public:
    SegmentTree(int original[], int frequency[], int size) {
      arraySize = size;
      treeSize = 2 * pow(2.0, floor(log2(size)) + 1);
      tree.resize(treeSize, 0);
      frequencyArray = frequency;
      originalArray = original;
      buildTree(1, 0, size - 1);
    }

    int getMaxFrequency(int i, int j) {
      int leftCount = 0, rightCount = 0;
      while (i > 0 && i <= j && originalArray[i] == originalArray[i - 1]) i++, leftCount++;
      while (j >= i && j < arraySize - 1 && originalArray[j] == originalArray[j + 1]) j--, rightCount++;
      return (j < i) ? max(leftCount, rightCount) : max(max(queryTree(1, 0, arraySize - 1, i, j), leftCount), rightCount);
    }
};

int main() {
  int n, q;
  while (cin >> n) {
    if (n == 0) break;
    cin >> q;
    int originalArray[100000];
    int frequencyArray[100000];
    map<int, int> frequencyCount;

    for (int i = 0; i < n; i++) {
      int value;
      cin >> value;
      frequencyCount[value]++;
      originalArray[i] = value;
    }

    for (int i = 0; i < n; i++) {
      frequencyArray[i] = frequencyCount[originalArray[i]];
    }

    SegmentTree segmentTree(originalArray, frequencyArray, n);

    // Process each query
    for (int i = 0; i < q; i++) {
      int start, end;
      cin >> start >> end;
      cout << segmentTree.getMaxFrequency(start - 1, end - 1) << endl;
    }
  }
  return 0;
}