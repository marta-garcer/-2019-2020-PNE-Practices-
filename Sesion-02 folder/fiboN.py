#Exercise 2

def fibon(n):
    a = 0
    m = 1
    for i in range (0, n-1) :
        sum = a + m
        a = m
        m = sum
    return m

print("5th fibonacci term:",fibon(5))
print("10th fibonacci term :", fibon(10))
print("15th fibonacci term: ", fibon(15))