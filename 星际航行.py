import sys
def get_max_item(array: list) -> int:
    max_i = 0
    for i, n in enumerate(array[1:]):
        if n <= array[max_i]:
            continue
        max_i = i + 1
    return max_i

A, B, C, D, N = sys.stdin.readline().split()
A, B, C, D, N = int(A), int(B), int(C), int(D), int(N)
#ks = list(reversed(sorted(enumerate([A, B, C, D]), key=lambda x: x[1])))
ks = list(enumerate([A, B, C, D]))
def range_k(k: int, n: int) -> int:
    return int(n / k)
result: list[tuple[int, int, int, int]] = []

for i in range(range_k(ks[0][1], N)):
    i_N = N - ks[0][1] * i
    if i_N < 0:
        break
    for j in range(range_k(ks[1][1], i_N)):
        j_N = i_N - ks[1][1] * j
        if j_N < 0:
            break
        for k in range(range_k(ks[2][1], j_N)):
            k_N = j_N - ks[2][1] * k
            if k_N < 0:
                break
            aim = k_N / ks[3][1]
            if int(aim) != aim:
                continue
            r = [0, 0, 0, 0]
            r[ks[0][0]] = i
            r[ks[1][0]] = j
            r[ks[2][0]] = k
            r[ks[3][0]] = int(aim)
            result.append((r[0], r[1], r[2], r[3]))
            break

if not len(result):
    print("-1")
else:
    print(f"{result[0][0]} {result[0][1]} {result[0][2]} {result[0][3]}")