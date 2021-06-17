import functools


@functools.lru_cache()
def is_prime(n):
    if n == 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


# Выводит массив из пар различных простых чисел, произведенеие которые даст n
@functools.lru_cache()
def get_two_primes(n):
    results = []
    d = 2
    while d * d < n:
        if n % d == 0 and is_prime(d) and is_prime(n//d):
            results.append([d, n//d])
        d += 1
    return results


minn = None
count = 0

for n in range(158928, 345293+1):
    d = 2
    while d * d < n:
        skip = False

        if n % d == 0:
            if is_prime(d):
                prime1 = d
                primes2 = get_two_primes(n//d)
                if prime1 is not None and primes2 != []:
                    for pair in primes2:
                        if prime1 not in pair:
                            if minn is None:
                                minn = n
                            count += 1
                            skip = True
                            break
            if skip:
                break

            if is_prime(n//d):
                prime1 = n//d
                primes2 = get_two_primes(d)
                if prime1 is not None and primes2 != []:
                    for pair in primes2:
                        if prime1 not in pair:
                            if minn is None:
                                minn = n
                            count += 1
                            skip = True
                            break
            if skip:
                break
        d += 1

print(count, minn)