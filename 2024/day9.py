from sys import set_int_max_str_digits


def getBlocks(line):
    set_int_max_str_digits(19999)
    diskMap = list(map(int, line))
    fileId = 0
    isFile = True
    blocks = []
    for i, x in enumerate(diskMap):
        blocks.extend(fileId if isFile else '.' for _ in range(x))
        if isFile:
            fileId += 1
        isFile = not isFile
    return blocks


def part1():
    with open('./input/day9.txt') as f:
        blocks = getBlocks(f.read())
        checksum = 0
        for i, b in enumerate(blocks):
            if b == '.':
                file = blocks.pop()
                while file == '.':
                    file = blocks.pop()
                if i >= len(blocks):
                    blocks.append(file)
                    break
                blocks[i] = file
            checksum += i * blocks[i]
        print(checksum)


def findAvailSpace(search, fileSize):
    space = ['.'] * fileSize
    for i in range(len(search) - fileSize + 1):
        if search[i:i + fileSize] == space:
            return i
    return -1


def part2():
    with open('./input/day9.txt') as f:
        blocks = getBlocks(f.read())
        checksum = 0
        for i in reversed(range(blocks[-1])):
            fid = i + 1
            fileSize = blocks.count(fid)
            openIdx = blocks.index('.')
            availSpace = findAvailSpace(blocks[openIdx:blocks.index(fid)], fileSize) + openIdx
            if availSpace >= openIdx:
                fileIdx = blocks.index(fid)
                file = blocks[fileIdx:fileIdx + fileSize]
                # Remove file from place
                blocks[fileIdx:fileIdx + fileSize] = ['.'] * fileSize
                # Place in empty space
                blocks[availSpace:availSpace + fileSize] = file
                # Remove trailing free space
                while blocks and blocks[-1] == '.':
                    blocks.pop()
        for fid, v in enumerate(blocks):
            if v != '.':
                checksum += fid * v
        print(checksum)


part2()
