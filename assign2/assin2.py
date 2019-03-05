class L:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def fibPow(n):
    x = L(0, 1)
    y = Pow(x, n)

    return y.b


def Pow(k, n):
    for i in range(n):
        sum = k.a + k.b
        k.a = k.b
        k.b = sum
    return k

def main():
    for i in range(0,1000):
        print(fibPow(i))


if __name__ == '__main__':
    main()
