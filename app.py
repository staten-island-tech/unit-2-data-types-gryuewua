#BILL

'''bill = int(input("Pay"))
service = (input("How was service?"))

if service == "bad":
    print(bill*1)
if service == "okay":
    print(bill*1.15)
if service == "good":
    print(bill*1.2)
if service == "great":
    print(bill*1.25)'''

#DISCOUNT

'''def discount(age,isResident,isMember):
    if (age < 12 or age >= 65) or ((isResident == True) or (isMember == True)):
        print("Discount")
    else:
        print("No discount")

print(discount(12,False,False))'''

#GCF

x = int(input("input number"))

y = int(input("input another number"))

factors = []

for p in range(1,x+1):
    if x%p == 0:
        for i in range(1,y+1):
            if y%i == 0:
                if i == p :
                    factors.append(i)
                    
print(f"GCF is {max(factors)}")