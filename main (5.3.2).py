import math


class Rational:
    def __init__(self, num=0, den=1):
        if den == 0:
            raise ValueError("Знаменник не може бути 0")

        self.num = num
        self.den = den
        self._reduce()

    def _reduce(self):
        g = math.gcd(self.num, self.den)
        self.num //= g
        self.den //= g
        if self.den < 0:
            self.num *= -1
            self.den *= -1

    def __add__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return Rational(self.num * other.den + other.num * self.den,
                        self.den * other.den)

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"


class RationalList:
    def __init__(self):
        self.data = []

    def append(self, value):
        if not isinstance(value, Rational):
            raise TypeError("Елемент має бути Rational")
        self.data.append(value)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        if not isinstance(value, Rational):
            raise TypeError("Елемент має бути Rational")
        self.data[index] = value

    def __len__(self):
        return len(self.data)

    def __add__(self, other):
        if not isinstance(other, RationalList):
            raise TypeError("Можна додавати тільки RationalList")

        result = RationalList()
        result.data = self.data + other.data
        return result

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
    with open(input_name, "r") as fin, open(output_name, "w") as fout:
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
