Scissor = '''

Scissor
      ________
---'    ______)____
          _________)
           __________)
        (______)
---. ____(____)


'''

Rock = '''

Rock
      ________
---'    ______)_
          ______)
           _____)
        (______)
---. ____(____)

'''

Paper = '''
Paper
      ________
---'    ______)____
          _________)
           _________)
              _____)
---. ____________)
'''
import random
Pictures = [Rock,Paper,Scissor]
a = int(input("What do you want to chose?  \n Type 0 for Rock. \n Type 1 for Paper. \n Type 2 for Scissor.\n"))
print(Pictures[a])
b = random.randint(0,2)
print("computer Choose :\n")
print(Pictures[b])
if(a == 0 and b == 0):
    print("Draw")
elif(a == 0 and b == 1):
    print("Computer Won")
elif(a == 0 and b == 2):
    print("You Won")
if(a == 1 and b == 0):
    print("You Won")
elif(a == 1 and b == 1):
    print("Draw")
elif(a == 1 and b == 2):
    print("Computer Won")
if(a == 2 and b == 0):
    print("Computer Won")
elif(a == 2 and b == 1):
    print("You Won")
elif(a == 2 and b == 2):
    print("Draw")
else:
    print("You chose wrong digit.")



