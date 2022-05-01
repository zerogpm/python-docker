import random
import pi

# rand = random.randint(1,3)
# randfloat = random.random()
# print(rand)
# print(randfloat)
# print(pi.pi)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choseList = [rock, paper, scissors]

userChoose = int(input("what is your choose?"))

computerChoose = random.randint(0, len(choseList) - 1)

print("user pick " + choseList[userChoose])
print("computer pick " + choseList[computerChoose])

if userChoose == computerChoose:
    print("draw")