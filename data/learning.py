print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

height = height ** 2

if height > 120:
    print(f"you can ride! {height}")
else:
    print(f"no fun for you {height}")