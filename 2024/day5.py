
def passesRules(update, pairs):
    for (a, b) in pairs:
        if a not in update or b not in update:
            continue
        if update.index(a) > update.index(b):
            return False
    return True


def part1():
    with open('./input/day5.txt') as f:
        lines = f.read().splitlines()
        pairs = []
        readingOrder = True
        total = 0
        # Read in data
        for line in lines:
            if not line:
                readingOrder = False
                continue
            if readingOrder:
                pairs.append(line.split('|'))
            else:
                update = line.split(',')
                if passesRules(update, pairs):
                    total += int(update[(len(update) - 1) // 2])
        print(total)


def fixUpdate(update, pairs):
    failedRules = False
    for i, (a, b) in enumerate(pairs):
        if update.index(a) < update.index(b):
            continue
        failedRules = True
        update.remove(a)
        update.insert(update.index(b), a)
        # Go through old rules again
        update, _ = fixUpdate(update, pairs[:i])
    return update, failedRules


def part2():
    with open('./input/day5.txt') as f:
        lines = f.read().splitlines()
        pairs = []
        readingOrder = True
        total = 0
        # Read in data
        for line in lines:
            if not line:
                readingOrder = False
                continue
            if readingOrder:
                pairs.append(line.split('|'))
            else:
                relevantPairs = []
                update = line.split(',')
                for (a, b) in pairs:
                    if a in update and b in update:
                        relevantPairs.append((a, b))

                fixed, failedRules = fixUpdate(update, relevantPairs)
                if failedRules:
                    total += int(fixed[(len(fixed) - 1) // 2])
        print(total)


part2()
