def faboncii(n):
    if n<=1:
        return 1
    return faboncii(n-1)+faboncii(n-2) 
print(faboncii(5))