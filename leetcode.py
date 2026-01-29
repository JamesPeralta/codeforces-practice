class UnionFind:
    def __init__(self, n):
        # parent[i] = parent of node i
        # initially, every node is its own parent
        self.parent = list(range(n))
        
        # rank[i] = an upper bound on the height of the tree rooted at i
        self.rank = [0] * n

    def find(self, x):
        """
        Finds the representative (root) of the set containing x.
        Uses path compression to make future queries faster.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        """
        Unites the sets containing x and y.
        Uses union by rank to keep the tree shallow.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # already in the same set

        # attach smaller rank tree under larger rank tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # same rank → choose one root and increase its rank
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

    def connected(self, x, y):
        """
        Checks whether x and y are in the same set.
        """
        return self.find(x) == self.find(y)
