evencount = 0
oddcount = 0

for x in range(5):
    num = int(input("What is your number? "))
    if num% 2==0:
        evencount=evencount+1
    else:
        oddcount=oddcount+1
print("You have",evencount,"even numbers")
print("You have",oddcount,"odd numbers")

    
