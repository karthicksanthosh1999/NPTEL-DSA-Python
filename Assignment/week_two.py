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
print(power(2,5))

