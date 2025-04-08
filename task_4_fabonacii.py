def faboncii(n):
    if n<=1:
        return 1
    return faboncii(n-1)+faboncii(n-2) 
n=5
for i in range(5):
    print(faboncii(i),end=" ")
