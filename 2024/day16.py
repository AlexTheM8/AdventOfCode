from heapq import heappop, heappush
import numpy as np


with open('./input/day16.txt') as f:
    lines = f.read().splitlines()
raceTrack = np.array([[c for c in line] for line in lines])


def movementOptions(score, x, y, dx, dy):
    return (
        (score + 1, x + dx, y + dy, dx, dy),
        (score + 1000, x, y, dy, -dx),
        (score + 1000, x, y, -dy, dx),
    )


def part1and2():
    y, x = np.argwhere(raceTrack == 'S')[0]
    scoresToPos = {(x, y, 1, 0): 0}
    toVisit = [(0, [(x, y)], 1, 0)]
    seats = set()
    bestScore = float('inf')
    while toVisit:
        score, path, dx, dy = heappop(toVisit)
        x, y = path[-1]
        if raceTrack[y, x] == 'E':
            bestScore = score
            seats.update(path)
        elif score < bestScore:
            for score, x, y, dx, dy in movementOptions(score, x, y, dx, dy):
                pos = x, y, dx, dy
                if raceTrack[y, x] != '#' and scoresToPos.get(pos, bestScore) >= score:
                    scoresToPos[pos] = score
                    heappush(toVisit, (score, path + [(x, y)], dx, dy))
    print('Score', bestScore)
    print('Seats', len(seats))


part1and2()
