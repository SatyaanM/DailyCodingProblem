def swap_bits(num):
    swap = ""
    for x in range(len(num)):
        if num[x] == '0':
            swap += '1'
        else:
            swap += '0'
    return swap


def one_liner(num):
    return "".join('1' if x == '0' else '0' for x in num)


print(swap_bits(str(10101010)))
print(one_liner(str(10101010)))
