from itertools import islice

def isPrime(n):
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k+=1
    return True

def gen_abwechselnd(prim, pprim):
    while True:
        yield next(prim)
        yield next(pprim)

def prim():
    n=1
    while True:
        while not isPrime(n):
            n+=1
        yield n
        n+=1    

def pprim():
   prime_gen = prim()
   last_prime=1
   new_prime=1
   while True:
        new_prime = next(prime_gen)
        if new_prime - last_prime == 2:
           yield (new_prime, last_prime)
        last_prime=new_prime


def main():
    # prime_generator=prim()
    prime_pairs_generator = pprim()
    prime_gen = prim()
    prime_gen_abwechselnd  = gen_abwechselnd(prime_gen,prime_pairs_generator)

    for _ in range(10):
        print(next(prime_gen_abwechselnd))


if __name__ == "__main__":
    main()