for n in range(1, 101):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            break
    else:
        print(n, end="\t")