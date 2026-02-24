import random

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

play_again = True

while play_again:
    image = [rock, paper, scissors]
	
    value = int(input("Enter 0 for rock, 1 for paper and 2 for scissors: "))
    rand_num = random.randint(0,2)
	
    if 2 < value < 0:
        print("you have entered a invalid number")
    else:
        print(f"Your input:\n{image[value]}")
        print(f"Computer input:\n{image[rand_num]}")

    if 2 < value < 0:
        print("your input is invalid, you lose!")
    elif value == rand_num:
        print("It's draw!")
    elif value == 0 and rand_num == 2:
        print("You win!")
    elif value == 2 and rand_num == 0:
        print("You lose!")
    elif value > rand_num:
        print("You win!")
    elif value < rand_num:
        print("You lose!")
		
    user = input("Do you want to play again? Type 'y' or 'n': ").lower()
	
    if user == "n":
        play_again = False