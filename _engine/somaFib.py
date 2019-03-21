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


termo = sys.argv[1]
tot = fib(termo)
tot = list(str(tot))
for c in range(len(tot)-1, 0, -1):
    if c % 3 == 0:
        tot.insert(c, '.')

soma = ''.join(i for i in tot)

print(f'A soma dos primeiros {termo} números de Fibonacci é {tot}')

