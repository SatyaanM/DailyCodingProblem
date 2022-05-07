import random;
import time;
random.seed(time.time())


def coins(n, num_rounds):
    num_flips = 0
    num_rounds += 1
    for x in range(n):
        flip = random.randint(0, 1)
        if num_flips == n-1:
            break
        elif flip:
            num_flips += 1
    if num_flips < n-1:
        coins(n - num_flips, num_rounds)
    else:
        return num_rounds


print(coins(10, 0))
