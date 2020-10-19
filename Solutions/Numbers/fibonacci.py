def fibogenerator():
    first, second = 0, 1
    while True:
        yield first
        first, second = second, first + second
        
fibonacci = fibogenerator()

n = int(input("Please put in what number of the fibonacci sequence you want: "))

for i in range(n + 1):
    nterm = next(fibonacci)

print(nterm)

