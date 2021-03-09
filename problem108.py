def check_shift(string1, string2, count):
    shifted = string1[-1] + string1[:-1]
    count += 1
    if count == len(string1):
        print("false")
    elif shifted == string2:
        print("true")
    else:
        check_shift(shifted, string2, count)


print("case 1: ")
check_shift("abcde", "cdeab", 0)
print("case2: ")
check_shift("abc", "acb", 0)
print("case3: ")
check_shift("hello", "llohe", 0)
print("case4: ")
check_shift("goodbye", "byegood", 0)
print("case5: ")
check_shift("python", "cython", 0)