
primes = []
twin_primes = []

for num in range(1, 101):
    count = False
    for i in range(2, (num // 2 + 1)):
        if (num % i == 0):
            count = True
            break

    if (count == False and num != 1):
        primes.append(num)


for i in range(0, len(primes)-1):
    if primes[i] + 2 == primes[i+1]:
        twin_primes.append((primes[i], primes[i+1]))

print("Prime Numbers (1 to 100):", primes)
print("Twin Prime Numbers:", twin_primes)
