import math


class Rational:
    def __init__(self, num=0, den=1):

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

    def __add__(self, other):

        if isinstance(other, int):
            other = Rational(other)

        if not isinstance(other, Rational):
            return NotImplemented

        return Rational(
            self.num * other.den + other.num * self.den,
            self.den * other.den
        )

    def __str__(self):

        if self.den == 1:
            return str(self.num)

        return f"{self.num}/{self.den}"


class RationalList:

    def __init__(self):
        self.data = []

    def append(self, value):

        if isinstance(value, int):
            value = Rational(value)

        if not isinstance(value, Rational):
            raise TypeError("Елемент має бути Rational або int")

        self.data.append(value)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):

        if isinstance(value, int):
            value = Rational(value)

        if not isinstance(value, Rational):
            raise TypeError("Елемент має бути Rational або int")

        self.data[index] = value

    def __len__(self):
        return len(self.data)

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

    def total(self):

        s = Rational(0, 1)

        for x in self.data:
            s = s + x

        return s


def parse_token(t):

    if '/' in t:

        n, d = t.split('/')

        return Rational(int(n), int(d))

    return Rational(int(t))


def process_file(input_name, output_name):

    with open(input_name, "r") as fin, \
         open(output_name, "w") as fout:

        for line in fin:

            line = line.strip()

            if not line:
                continue

            tokens = line.split()

            rlist = RationalList()

            for t in tokens:
                rlist.append(parse_token(t))

            result = rlist.total()

            fout.write(f"{line} = {result}\n")


def main():

    process_file("input01.txt", "output01.txt")
    process_file("input02.txt", "output02.txt")
    process_file("input03.txt", "output03.txt")


if __name__ == "__main__":
    main()
