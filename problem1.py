arr = [10, 15, 3, 7]
k = 17


def equals_k(arr, k):
    for a in range(len(arr)):
        for b in range(a+1, len(arr)):
            if arr[a] + arr[b] == k:
                return True
    return False


print(equals_k(arr, k))
