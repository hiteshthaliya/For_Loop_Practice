# Calculate and print the factorial of every number from 1 to 100.
for num in range(1,11):
    fact = 1
    for i in range(1,num+1):
        fact *=i
    print(f"{num}! = {fact}")    