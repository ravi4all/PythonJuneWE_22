# Print all prime numbers in a given interval
min_range = int(input("Enter min range : "))
max_range = int(input("Enter max range : "))

for num in range(min_range, max_range):
    if num % 2 == 0 or num % 3 == 0:
        print(f"{num} is not Prime...")
    else:
        for i in range(5, num // 2, 6):
            if num % i == 0 or num % i + 2 == 0:
                print(f"{num} is not prime...")
                break
        else:
            print(f"{num} is prime...")