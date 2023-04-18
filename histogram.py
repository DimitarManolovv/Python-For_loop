n = int(input())

p1_cnt = 0
p2_cnt = 0
p3_cnt = 0
p4_cnt = 0
p5_cnt = 0

for i in range(0, n):
    curr_num = int(input())

    if curr_num < 200:
        p1_cnt += 1
    elif curr_num <= 399:
        p2_cnt += 1
    elif curr_num <= 599:
        p3_cnt += 1
    elif curr_num <= 799:
        p4_cnt += 1
    else:
        p5_cnt += 1

r1 = (p1_cnt / n) * 100
r2 = (p2_cnt / n) * 100
r3 = (p3_cnt / n) * 100
r4 = (p4_cnt / n) * 100
r5 = (p5_cnt / n) * 100

print((f'{r1:.2f}%'))
print((f'{r2:.2f}%'))
print((f'{r3:.2f}%'))
print((f'{r4:.2f}%'))
print((f'{r5:.2f}%'))