def missing_num(num):
    ran=num[-1]
    match=1
    for i in range(0,ran-1):
        if num[i]!=match:
            print(f"missing no. is : {match}")
            break
        match+=1    
           
    
missing_num([1,2,3,5,6])    