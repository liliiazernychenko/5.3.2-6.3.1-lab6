import math


class Rational:

    def __init__(self, num, den=1):

        if den == 0:
            raise ValueError("Знаменник не може бути 0")

        g = math.gcd(num, den)

        num //= g
        den //= g

        if den < 0:
            num *= -1
            den *= -1

        self.num = num
        self.den = den

    def __str__(self):

        if self.den == 1:
            return str(self.num)

        return f"{self.num}/{self.den}"


class RationalListIterator:

    def __init__(self, data):

        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index >= len(self.data):
            raise StopIteration

        value = self.data[self.index]

        self.index += 1

        return value


class RationalList:

    def __init__(self):
        self.data = []

    def append(self, value):

        if isinstance(value, int):
            value = Rational(value)

        if not isinstance(value, Rational):
            raise TypeError("Елемент має бути Rational або int")

        self.data.append(value)

    def __iter__(self):

        return RationalListIterator(self.data)

    def __add__(self, other):

        result = RationalList()

        result.data = self.data.copy()

        if isinstance(other, RationalList):

            result.data.extend(other.data)

        elif isinstance(other, Rational):

            result.data.append(other)

        elif isinstance(other, int):

            result.data.append(Rational(other))

        else:
            raise TypeError(
                "Можна додавати RationalList, Rational або int"
            )

        return result

    def __iadd__(self, other):

        if isinstance(other, RationalList):

            self.data.extend(other.data)

        elif isinstance(other, Rational):

            self.data.append(other)

        elif isinstance(other, int):

            self.data.append(Rational(other))

        else:
            raise TypeError(
                "Можна додавати RationalList, Rational або int"
            )

        return self

    def sort(self):

        self.data.sort(
            key=lambda x: (x.den, x.num),
            reverse=True
        )


def parse_token(t):

    if '/' in t:

        n, d = t.split('/')

        return Rational(int(n), int(d))

    return Rational(int(t))


def read_file(filename):

    rlist = RationalList()

    with open(filename, "r") as f:

        for line in f:

            tokens = line.strip().split()

            for t in tokens:

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
