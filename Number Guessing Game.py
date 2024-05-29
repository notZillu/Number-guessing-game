import random

#Introduction to the game
print("This is a nuber guessing game where the computer will choose a number from 1 to 100. You will be give 3 hints and and for each hint you get 2 chances.")

#Setting the range for the computer to choose a number
computer_choice = random.randint(1, 100)

#Setting number of attempts for each hint
attempts = 2

#Using 'for' loop for the correct number of attempts by the player 
for a in range(1, attempts+1):
  
  #Checking if the number the computer chose is between 1 and 50 or 51 and 100 to set one hint
  if computer_choice <= 50:
    print("Hint: The number is between 1 and 50.")
  elif computer_choice > 50:
    print("Hint: The number is between 51 and 100.")

  player_input_1 = int(input("Enter your guess over here: "))

  #Checking if the player guessed the correct number or if the player needss to go higher or lower
  if player_input_1 == computer_choice:
    print("You guessed the correct number!")
    quit()
  elif player_input_1 <= computer_choice:
    print("Go higher.")
  elif player_input_1 >= computer_choice:
    print("Go lower.")

for a in range(1, attempts+1):

  #Checking if the number is even or odd to set another hint
  if computer_choice % 2 == 0:
    print("Hint: The number is even.")
  elif computer_choice % 2 == 1:
    print("Hint: The number is odd.")

  player_input_2 = int(input("Enter your guess over here: "))

  #Checking if the player guessed the correct number or if the player needss to go higher or lower
  if player_input_2 == computer_choice:
    print("You guessed the correct number!")
    quit()
  elif player_input_2 <= computer_choice:
    print("Go higher.")
  elif player_input_2 >= computer_choice:
    print("Go lower.")

for a in range(1, attempts+1):
  
  # Create a list of prime numbers up to 100 using Sieve of Eratosthenes algorithm
  primes = []
  for i in range(2, 101):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
          if i % j == 0:
            is_prime = False
            break
        if is_prime:
            primes.append(i)

    # Check if the chosen number is in the list of primes
  if computer_choice in primes:
    print("Hint: The number is a prime number.")
  else:
    print("Hint: The number is a composite number.")

  player_input_3 = int(input("Enter your guess over here: "))

  # Checking if the player guessed the correct number or if the player needs to go higher or lower
  if player_input_3 == computer_choice:
    print("You guessed the correct number!")
    quit()
  elif player_input_3 < computer_choice:
    print("Go higher.")
  elif player_input_3 > computer_choice:
    print("Go lower.")