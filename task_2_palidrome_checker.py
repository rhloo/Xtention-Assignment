def palidrome_checker(s):
    s=s.lower().replace(" ","")
    a=s[::-1]
    if s==a:
        print(f"{s} is polidrome")
    else:
        print (f"{s} is not polidrome")   
        
palidrome_checker("rahul")
palidrome_checker("A man a plan a canal Panama")
palidrome_checker("level")
