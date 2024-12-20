import math

import numpy as np
from heapq import heappush, heappop


with open('./input/day18.txt') as f:
    lines = f.read().splitlines()
bytePos = [tuple(map(int, line.split(','))) for line in lines]

w, h = 71, 71
endPos = (w-1, h-1)


def findPath(byteMap):
    visited = set()
    toVisit = []
    heappush(toVisit, (0, [(0, 0)]))
    costs = {(0, 0): 0}
    while toVisit:
        cost, path = heappop(toVisit)
        pos = path[-1]
        visited.add(pos)
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = nextPos = pos[0] + dx, pos[1] + dy
            if not (0 <= nx < w and 0 <= ny < h) or nextPos in visited or byteMap[nextPos] == '#':
                continue
            if nextPos == endPos:
                return path + [endPos]
            cost += 1 + math.dist(nextPos, endPos)
            if cost < costs.get(nextPos, float('inf')):
                costs[nextPos] = cost
                heappush(toVisit, (cost, path + [nextPos]))
    return []


def part1():
    byteMap = np.full((w, h), '.')
    for i in range(1024):
        byteMap[bytePos[i]] = '#'
    print(len(findPath(byteMap)) - 1)


def part2():
    byteMap = np.full((w, h), '.')
    solvedPath = []
    for i in range(len(bytePos)):
        pos = bytePos[i]
        byteMap[pos] = '#'
        if i == 1024:
            solvedPath = findPath(byteMap)
        elif pos in solvedPath:
            solvedPath = findPath(byteMap)
            if len(solvedPath) == 0:
                print(i, pos)
                break


part2()
