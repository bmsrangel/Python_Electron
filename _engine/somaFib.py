# encoding: iso-8859-1
import sys


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
def fib(n):
    if n >= 0:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return 1 + fib(n-1) + fib(n-2)


termo = int(sys.argv[1])
tot = fib(termo)
tot = list(str(tot))
cont = 0
c = len(tot)-1
while c != 0:
    print(c)
    if tot[c].isnumeric():
        cont += 1
        c -= 1
    if cont == 3 or tot[c] == '.':
        tot.insert(c+1, '.')
        cont = 0

soma = ''.join(i for i in tot)

print(f'A soma dos primeiros {termo} números de Fibonacci é {soma}')
