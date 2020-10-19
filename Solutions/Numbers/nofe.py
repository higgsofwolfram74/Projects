import decimal

#generator object for odd factorials of denominator
def factorial():
    n = 1
    value = 1

    while True:
        yield value
        n += 1
        value *= n
        n += 1
        value *= n


#e is defined as the infinite series (2n + 2)/(2n + 1)! starting at n=0
def compute_e(n):
    decimal.getcontext().prec = n + 1
    factorials = factorial()
    e = 0
    for i in range(n + 2):
        numerator = 2 * i + 2
        denominator = next(factorials)
        e += decimal.Decimal(numerator / denominator)
    return e

#put limit on user input so algrothim isn't unmaintainable
while True:
    n = int(input("Please type number between 0-1000: "))
    if n >= 0 and n <= 1000:
        break


print(str(compute_e(n))[:n + 1])