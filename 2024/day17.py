import re

with open('./input/day17.txt') as f:
    lines = f.read().splitlines()
A = int(re.findall(r'\d+', lines[0])[0])
B = int(re.findall(r'\d+', lines[1])[0])
C = int(re.findall(r'\d+', lines[2])[0])
program = list(map(int, lines[4].split()[1].split(',')))


def getComboVal(val, regA, regB, regC):
    match val:
        case _ if val in range(4):
            return val
        case 4:
            return regA
        case 5:
            return regB
        case 6:
            return regC
        case _:
            return None


def compute(regA, regB, regC):
    i = 0
    output = []
    while i < len(program):
        opCode, operand = program[i], program[i+1]
        combo = getComboVal(operand, regA, regB, regC)
        match opCode:
            case 0:
                # division: regA = regA / 2^operand--combo
                regA = regA >> combo
            case 1:
                # bitwise XOR: regB XOR operand--literal
                regB = regB ^ operand
            case 2:
                # modulo: operand % 8--combo
                regB = combo % 8
            case 3:
                # if regA not 0, jump to operand--literal
                if regA != 0:
                    i = operand
                    continue
            case 4:
                # bitwise XOR: regB = regB XOR regC
                regB = regB ^ regC
            case 5:
                # output: operand % 8--combo
                output.append(combo % 8)
            case 6:
                # division: regB = regA / 2^operand--combo
                regB = regA >> combo
            case 7:
                # division: regC = regA / 2^operand--combo
                regC = regA >> combo
        i += 2
    return output


def part1():
    print(','.join(list(map(str, compute(A, B, C)))))


def findCopy(prevNum=0, idx=15):
    # Work backwards as earlier indexes are more variable
    if idx == -1:
        return prevNum
    solutions = {float('inf')}
    for i in range(1, 8):
        # 3-bit iterations (8^digit), starting at the previous number's pattern
        regA = 8 ** idx * i + prevNum
        if compute(regA, B, C)[idx] == program[idx]:
            solutions.add(findCopy(regA, idx-1))
    return min(solutions)


def part2():
    print(findCopy())


part2()
