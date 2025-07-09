# SIMPLE EXAMPLE
def gcd(m,n):
    fm=[]
    for i in range(1,m+1):
        if m%i == 0:
            fm.append(i)
    fn=[]
    for j in range(1,n+1):
        if n%j == 0:
            fn.append(j)
    fc=[]
    for f in fm:
        if f in fn:
            fc.append(f)
    return (fc[-1])
print("Optimized GCD:",gcd(14,63))


# OPTIMIZED EXAMPLE
def opt_gcd(m,n):
    fc=[]
    for f in range(1,min(m,n)+1):
        if m%f == 0 and n%f == 0:
            fc.append(f)
    return fc
print("Optimized GCD:",opt_gcd(14,63))

# NO LIST
def no_list_gcd(m,n):
    for f in range(1, min(m,n)+1):
        if m%f ==0 and n%f == 0:
            mrfc = f
    return mrfc
print("No list GCD:", no_list_gcd(14, 63))

# NO LIST WHILE LOOP
def no_list_while_gcd(m,n):
    i = min(m,n)
    while i > 0:
        if m%i ==0 and n%i ==0:
            return(i)
        else:
            i = i-1
print("While loop no list:", no_list_while_gcd(14,63))


def GCD_Theory(a,b):
    while b != 0:
        a,b = b, a % b
    return a
print("Based on the theory:", GCD_Theory(14,63))