from math import ceil


def can_finish_eating(piles, h, k):
    hour_used = 0
    for p in piles:
        hour_used += ceil(float(p) / k)
    return hour_used <= h


print(can_finish_eating([1, 2, 3, 4, 5, 6], 6, 3))
