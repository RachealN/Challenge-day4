def power(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    else:
        return a*power(a, b-1)


if __name__ == '__main__':
    print(power(2, 3))
