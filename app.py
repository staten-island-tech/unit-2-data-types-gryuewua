number = int(input("give me a number"))
x = 0
factor = [1-number]

for i in factor:
    if number%(factor[x]) == 0:
        print(factor[x])
        x+1
        i+1
    else:
        x+1
        i+1