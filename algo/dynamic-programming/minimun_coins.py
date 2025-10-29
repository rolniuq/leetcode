memo = {}


def minimun_coins(m: int, coins: list[int]):
    if m in memo:
        return memo[m]

    if m == 0:
        answer = 0
    else:
        answer = float("inf")
        for coin in coins:
            sub = m - coin
            if sub < 0:
                continue
            answer = min(answer, minimun_coins(sub, coins) + 1)

    memo[m] = answer

    return answer


print("[DEBUG]:", minimun_coins(150, [1, 4, 5]))
