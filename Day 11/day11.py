visited = []
INPUT = []
### Part 1
with open("Day 11/day11input.txt") as file:
    for line in file:
        INPUT.append(line)

from collections import defaultdict

def parseInput(lines):
    graph = defaultdict(list)
    for line in lines:
        name, outputs = line.strip().split(":")
        if outputs.strip():
            for target in outputs.strip().split():
               graph[name].append(target)
    
    return graph
    
def allPaths(graph, start, end):
    paths = []

    def dfs(node, path):
        if node == end:
            paths.append(path[:])
            return
        
        for next in graph[node]:
            dfs(next, path + [next])

    dfs(start, [start])
    return paths


graph = parseInput(INPUT)
paths = allPaths(graph, "you", "out")

print(len(paths))

### part 2 ###
from collections import defaultdict

### Part 2 ###
from functools import lru_cache
from math import prod

FILENAME = "Day 11/day11input.txt"


def parse_input(filename):
    with open(filename, "r") as input_file:
        return {
            line[:3]: line[5:].split(" ") for line in input_file.read().splitlines()
        }


def count_paths(graph, start, end):
    @lru_cache(None)
    def dfs(node):
        if end == node:
            return 1
        return sum(dfs(neighbor) for neighbor in graph[node])
    return dfs(start)


def part_two(graph, paths):
    return max(
        prod(count_paths(graph, start, end) for start, end in zip(path, path[1:]))
        for path in paths
    )



data = parse_input(FILENAME)
data["out"] = []
print(part_two(data, [["svr", "fft", "dac", "out"], ["svr", "dac", "fft", "out"]]))