num = int(input("Enter a number : "))

iterations = 0

if num % 2 == 0 or num % 3 == 0:
    print("Not Prime...")

else:
    # for...else
    for i in range(5, num // 2, 6):
        iterations += 1
        if num % i == 0 or num % i + 2 == 0:
            print("Number is not prime...")
            break
    else:
        print("Number is prime...")

print("Total Iterations : ",iterations)