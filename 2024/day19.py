from functools import cache

with open('./input/day19.txt') as f:
    lines = f.read().splitlines()
towels = lines[0].split(', ')


@cache
def countCombos(pattern):
    return sum(countCombos(pattern.removeprefix(t)) for t in towels if pattern.startswith(t)) if pattern else 1


possible, combos = 0, 0
for p in lines[2:]:
    res = countCombos(p)
    possible += 1 if res > 0 else 0
    combos += res
print(possible, combos)

