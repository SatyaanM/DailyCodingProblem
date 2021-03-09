import math
arr = [1, 2, 3, 4, 5]


def product_except_self1(arr1):  # division
    arr2 = []
    length = len(arr1)

    for x in range(0, length):
        product = math.prod(arr1) / arr1[x]
        arr2.insert(x, math.trunc(product))

    return arr2


def product_except_self2(arr1):  # no division
    arr2 = []
    length = len(arr1)

    for each in range(0, length):
        temp = arr1[:each] + arr1[each + 1:]
        arr2.insert(each, math.prod(temp))
    return arr2


print(f'With Division: {product_except_self1(arr)}')
print(f'Without Division: {product_except_self2(arr)}')
