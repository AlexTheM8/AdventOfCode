import numpy as np


def part1and2(part2=False):
    with open('./input/day8.txt') as f:
        lines = f.read().splitlines()
        npArr = np.array([[c for c in line] for line in lines])
        signals = set(''.join(lines))
        signals.remove('.')
        antinodes = set()
        w, h = npArr.shape
        for s in signals:
            locs = np.argwhere(npArr == s)
            for i, loc1 in enumerate(locs):
                if part2:
                    x1, y1 = loc1
                    antinodes.add((x1, y1))
                for loc2 in locs[i+1:]:
                    dist = loc1 - loc2
                    n1, n2 = loc1 + dist, loc2 - dist
                    x1, y1 = n1
                    x2, y2 = n2
                    while w > x1 >= 0 and h > y1 >= 0:
                        antinodes.add((x1, y1))
                        if not part2:
                            break
                        n1 += dist
                        x1, y1 = n1
                    while w > x2 >= 0 and h > y2 >= 0:
                        antinodes.add((x2, y2))
                        if not part2:
                            break
                        n2 -= dist
                        x2, y2 = n2
        print(len(antinodes))


part1and2(part2=True)