import numpy as np

coords = []

with open("Day 8/day8input.txt") as file:
    lines = file.readlines()

for line in lines:
    x, y, z = map(int, line.strip().split(","))
    coords.append((x, y, z))

#GAMEPLAN
'''
1. Read all junction box positions into a list. -- DONE (coords)

2. Compute the straight-line (Euclidean) distance between every possible pair
   of boxes and store:
       (distance, boxA_index, boxB_index) -- DONE (list titled eucDist)

3. Sort this list of all pairs by distance from smallest to largest.

4. Create a Union-Find (disjoint-set) structure so each box starts
   as its own circuit. -- DONE

5. Move through the sorted list of pairs one by one:
      - Union them (connect the circuits), even if already connected
      - Each pair counts as 1 attempt

6. Stop when we've PROCESSED the 1000 closest pairs (attempts = 1000)

7. Count circuit sizes, sort, multiply the largest three.
'''

#Euclidean distance calc between every possible pair
eucDist = []
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        a = np.array(coords[i])
        b = np.array(coords[j])
        d = np.linalg.norm(a - b)
        eucDist.append((d, i, j))

#sorting the list from smallest to largest distance
eucDist.sort(key=lambda x: x[0])

n = len(coords)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False

        if self.size[rootA] < self.size[rootB]:
            rootA, rootB = rootB, rootA

        self.parent[rootB] = rootA
        self.size[rootA] += self.size[rootB]
        return True

    def get_sizes(self):
        roots = {}
        for i in range(len(self.parent)):
            r = self.find(i)
            roots[r] = roots.get(r, 0) + 1
        return list(roots.values())


# --- PROCESS THE 1000 CLOSEST PAIRS ---
uf = UnionFind(n)
attempts = 0

for dist, a, b in eucDist:
    uf.union(a, b)  # try to connect them
    attempts += 1   # this pair has been processed

    if attempts == 1000:
        break


# --- GET CIRCUIT SIZES ---
sizes = uf.get_sizes()
sizes.sort(reverse=True)

print("Attempts:", attempts)
print("Circuit sizes:", sizes)
print("Largest three:", sizes[:3])
print("Product:", sizes[0] * sizes[1] * sizes[2])

# --- PART 2: Keep merging until only one circuit remains ---

uf = UnionFind(n)
num_sets = n
last_pair_product = None

for dist, a, b in eucDist:

    # Attempt union
    if uf.union(a, b):
        num_sets -= 1   # One fewer circuit now

        # If this union merges everything into 1 set, stop.
        if num_sets == 1:
            x1 = coords[a][0]
            x2 = coords[b][0]
            last_pair_product = x1 * x2
            break

print("Final X-coordinate product:", last_pair_product)