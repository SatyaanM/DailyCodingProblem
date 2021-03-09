def swap_bits(num):
    temp = ""
    for x in range(len(num)):
        if num[x] == '0':
            temp += '1'
        else:
            temp += '0'
    return temp


def one_liner(num):
    return "".join('1' if x == '0' else '0' for x in num)


print(swap_bits(str(10101010)))
print(one_liner(str(10101010)))
