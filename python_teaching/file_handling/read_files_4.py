with open("python_teaching/file_handling/file_1.txt") as f:
    y = 1
    for x in f:
        print(y,".", x)
        y+=1
        
