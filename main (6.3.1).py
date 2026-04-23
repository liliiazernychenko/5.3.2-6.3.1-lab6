import math


class Rational:
    def __init__(self, num, den=1):
        g = math.gcd(num, den)
        num //= g
        den //= g
        if den < 0:
            num *= -1
            den *= -1

        self.num = num
        self.den = den

    def __str__(self):
        return f"{self.num}/{self.den}" if self.den != 1 else str(self.num)


class RationalList:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def __iter__(self):
        return iter(self.data)

    def __add__(self, other):
        result = RationalList()
        result.data = self.data + other.data
        return result

    def sort(self):
        self.data.sort(key=lambda x: (x.den, x.num))


def parse_token(t):
    if '/' in t:
        n, d = t.split('/')
        return Rational(int(n), int(d))
    return Rational(int(t))


def read_file(filename):
    rlist = RationalList()

    with open(filename, "r") as f:
        for line in f:
            for t in line.strip().split():
                rlist.append(parse_token(t))

    return rlist


def main():
    l1 = read_file("input01.txt")
    l2 = read_file("input02.txt")
    l3 = read_file("input03.txt")

    combined = l1 + l2 + l3
    combined.sort()
    with open("output.txt", "w") as f:
        for x in combined:
            f.write(str(x) + " ")

    print("Записано у output.txt")


if __name__ == "__main__":
    main()
