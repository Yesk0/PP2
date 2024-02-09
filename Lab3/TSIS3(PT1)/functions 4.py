import math

def filter_prime(x):
    max1 = max(x)
    primes = []

    for i in x:
        isp = True
        
        if i == 2:
            primes.append(i)
        elif i == 1:
            continue
        else:
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    isp = False
                    break

            if isp:
                primes.append(i)
    
    print(*primes)

x = [1, 2, 4, 5, 3, 9, 12, 13, 17, 19]

filter_prime(x)

    