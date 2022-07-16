num = int(input("Enter a number : "))

prime = True

for i in range(2, num):
    if num % i == 0:
        prime = False
        # print("Not Prime...")
        break
    
if prime:
    print("Number is prime...")
else:
    print("Number is not prime...")
