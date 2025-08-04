# def delchar(word, leter):
#     for i in word:
#         if i != leter:
#             print(i, end="")

# delchar("banana","an")


def power(a,n):
    ans=1
    for i in range(0, n):
        ans = ans * a
    return ans
# print(power(2,5))


def primeproduct(n):
    factorList = []
    for i in range(1,n+1):
        if n%i == 0:
            factorList.append(i)
    return factorList
def isPrime(n):
    return primeproduct(n) == [1,n]

print(isPrime(202))

