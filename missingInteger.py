def missing(arr):
    arr = [x for x in arr if x >= 0]
    arr.sort()
    missingInt = arr[len(arr) - 1] + 1
    for i in range(0, len(arr) - 1):
        if arr[i + 1] - arr[i] != 1:
            missingInt = arr[i] + 1
            break
    return missingInt


print(missing([3, 4, -1, 1]))
