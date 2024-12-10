def validEq(vals, target, useOr=False):
    if len(vals) == 1:
        return vals[0] == target
    if vals[0] > target:
        return False
    return validEq([vals[0] + vals[1]] + vals[2:], target, useOr) \
        or validEq([vals[0] * vals[1]] + vals[2:], target, useOr) \
        or useOr and validEq([int(str(vals[0]) + str(vals[1]))] + vals[2:], target, useOr)


def part1and2(part2=False):
    with open('./input/day7.txt') as f:
        lines = f.read().splitlines()
        total = 0
        for line in lines:
            res, vals = line.split(': ')
            res = int(res)
            vals = list(map(int, vals.split(' ')))
            # useOr = True for part 2
            if validEq(vals, res, useOr=part2):
                total += res
        print(total)


part1and2(part2=True)
