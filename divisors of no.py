number = 28
divisors = []
for i in range(1, int(number**0.5) + 1):
    if number % i == 0:
        divisors.append(i)
        if number // i != i:
            divisors.append(number // i)

divisors.remove(number)
divisors.sort()
print(divisors)
