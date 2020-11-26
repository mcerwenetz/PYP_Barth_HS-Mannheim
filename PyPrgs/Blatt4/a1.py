# Geradzahlige Kubikzahlen der Zahlen 1 bis 10
print([i**3 for i in range(1,11) if i%2 == 0])

# oder als lambda
# print(list(filter(lambda x: x %2 == 0, map(lambda x: x**3, range(1,11)))))


# Alle Teiler einer Zahl z außer 1 und z (testen Sie mit 123, 12345, 123456)
zahl = 123
print([i for i in range(2,zahl) if zahl%i == 0])

# primitiv
# print(list(filter(lambda i: zahl%i == 0, range(2,zahl))))


# Alle Primzahlen zwischen 10000 und 10100
def isPrime(x: int):
    for i in range(2, x):
        if(x%i == 0):
            return False
    return True

print([i for i in range(10000, 10100) if isPrime(i)])
# print(list(filter(isPrime, range(10000, 10100))))