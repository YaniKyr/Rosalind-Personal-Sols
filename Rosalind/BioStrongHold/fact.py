def fact(n,k):
    if n == 1:
        return 1
    else:
        # recursive call to the function
        return ((n-k) * fact(n-1,k-1))

res = fact(21,7)
print(res%1000000)