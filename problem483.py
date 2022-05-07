def execute_prisoners(n, k):
    prisoners = [x for x in range(1, n+1)]
    order = []
    i = 0
    for x in range(1, n):
        i += k
        i = i % n
        order.append(i)
        prisoners.remove(i)
    print(prisoners[0])
    print(order)

execute_prisoners(5, 2)