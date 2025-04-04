def process_log_file(filename,word):

    t=0
    with open(filename) as file:
    
        for i in file:
            if i!=word:
                t=t+1
        print(f"{word} appear in {t} lines")
                    

process_log_file("file.txt","error")        
