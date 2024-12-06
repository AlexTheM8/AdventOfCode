import math


def part1():
    with open('./input/day2.txt', 'r') as f:
        safeCnt = 0
        lines = f.readlines()
        # count number of safe reports
        for line in lines:
            report = list(map(int, line.split(' ')))  # converts strs to ints
            if sorted(report) != report and sorted(report, reverse=True) != report:
                continue
            isSafe = True
            for i, v in enumerate(report):
                if i == 0:
                    continue
                isSafe = isSafe and 1 <= math.fabs(v - report[i-1]) <= 3
            if isSafe:
                safeCnt += 1
        print(safeCnt)


def checkDiff(report, errCnt):
    if errCnt > 1:
        return errCnt
    negCnt, posCnt = 0, 0
    for i, v in enumerate(report):
        if i == 0:
            continue
        if errCnt > 1:
            break
        diff = v - report[i-1]
        if diff < 0:
            negCnt += 1
        if diff > 0:
            posCnt += 1
        if math.fabs(diff) > 3:
            updatedDiff = math.fabs(report[max(0, i-1)] - report[min(len(report) - 1, i+1)])
            if updatedDiff > 3:
                errCnt += 1
            errCnt += 1
            continue
        if math.fabs(diff) == 0:
            errCnt += 1
    return errCnt + min(negCnt, posCnt)


def part2():
    # same process, but if removing one number makes it safe, it still counts
    with open('./input/day2.txt', 'r') as f:
        safeCnt = 0
        lines = f.readlines()
        # count number of safe reports
        goodPass, badPass = [], []
        for line in lines:
            report = list(map(int, line.split(' ')))  # converts strs to ints
            if len(report) == 1:
                safeCnt += 1
                continue
            reportSet = list(dict.fromkeys(report))
            if len(report) - len(reportSet) > 1:
                continue
            bfErrCnt = []
            for i, _ in enumerate(report):
                errCnt = checkDiff(report[:i] + report[i + 1:], 1)
                bfErrCnt.append(errCnt)
                if errCnt == 1:
                    break
            if min(bfErrCnt) <= 1:
                goodPass.append(report)
                safeCnt += 1
        print(safeCnt)


part2()
