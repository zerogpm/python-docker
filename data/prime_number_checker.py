# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for each_number in range(2, number):
        if number % each_number == 0:
            is_prime = False
    if is_prime:
        print("IT is a prime number")
    else:
        print("IT is not a prime number")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
