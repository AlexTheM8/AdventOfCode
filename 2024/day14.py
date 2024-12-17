import numpy as np

with open('./input/day14.txt') as f:
    lines = f.read().splitlines()
# Format (x, y), (vx, vy)
robots = set()
for line in lines:
    p, v = line.split()
    x, y = list(map(int, p.replace('p=', '').split(',')))
    vx, vy = list(map(int, v.replace('v=', '').split(',')))
    robots.add(((x, y), (vx, vy)))

w, h = 101, 103
wMid = w // 2
hMid = h // 2


def part1():
    q0, q1, q2, q3 = 0, 0, 0, 0
    for (x, y), (vx, vy) in robots:
        x += vx * 100
        y += vy * 100
        # but first, we need to talk about
        # Parallel Universes
        x = x % w
        y = y % h
        if x < wMid and y < hMid:
            q0 += 1
        elif x < wMid and y > hMid:
            q1 += 1
        elif x > wMid and y < hMid:
            q2 += 1
        elif x > wMid and y > hMid:
            q3 += 1
    print(q0*q1*q2*q3)


def part2():
    for i in range(1000000):
        arr = np.full((h, w), '.')
        check = True
        for (x, y), (vx, vy) in robots:
            x += vx * i
            y += vy * i
            x = x % w
            y = y % h
            if arr[y, x] == '#':
                check = False
                break
            arr[y, x] = '#'
        if check and any(['#'*10 in ''.join(row) for row in arr]):
            with open('./output/day14Out.txt', 'w') as write:
                for row in arr:
                    write.write(''.join(row) + '\n')
                print(i)
                exit(1)
    print('Not found')


part2()
