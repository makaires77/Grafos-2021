def fatorial(n):
    """ Retorna o fatorial de n """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fatorial(n - 1) * n

def fatorial_range(n):
    """ Retorna o fatorial de todos os números entre 1 e n """
    next_value = 1
    for i in range(1, n+1):
        yield next_value
        next_value *= i + 1

k = fatorial_range(7)
print(list(k))