import sys

def get_input() -> tuple[int, int, int, list[list[float]]]:
    n, m, k = sys.stdin.readline().split()
    n, m, k = int(n), int(m), int(k)
    stock_market: list[list[float]] = []
    for i in range(n):
        data = sys.stdin.readline()
        stock_market.append([float(w) for w in data.split()])
    return n, m, k, stock_market

def get_max_item(array: list[float], delta: list[float]) -> int:
    aaa = [d/a for a, d in zip(array, delta)]
    max_i = 0
    for i, n in enumerate(aaa[1:]):
        if n <= aaa[max_i]:
            continue
        max_i = i + 1
    return max_i

def process(n: int, m: int, k: int, stock_market: list[list[float]]):
    delta:list[list[float]] = []
    for b, a in zip(stock_market[:-1], stock_market[1:]):
        new_item: list[float] = []
        for bi, ai in zip(b, a):
            new_item.append(ai - bi)
        delta.append(new_item)
    money: float = k
    hold_list: list[int] = [-1]
    for i, day in enumerate(delta):
        max_i = get_max_item(stock_market[i], day)
        max = day[max_i]
        if max <= 0:
            hold_list.append(-1)
            continue
        hold_list.append(max_i)
        money *= 1 + max / stock_market[i][max_i]
    hold_list.append(-1)
    
    print("{:.4f}".format(money))
    for l, r in zip(hold_list[:-1], hold_list[1:]):
        print(l, r)


n, m, k, stock_market = get_input()
process(n, m, k, stock_market)