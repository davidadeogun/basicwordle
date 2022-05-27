
import random

#created a list of words that can be randomly selected 
random_words = ["duvet", "bed", "pillow","mattress"] 
secret_word = random.choice(random_words)   #This randomly chooses an element from the list "random_words" for the user to guess


guess = ""   #The value of the variable, guess is set to empty, because the user can guess any word.
count = 0    #Starts the count of guesses at zero

print("Welcome to the word guessing game!")
print()
#I gave a clue of the secret word,so that there can be few quesses

while guess != secret_word:
     guess = input("What is your guess? The items can be found in a bedroom: ").lower()
                                        
     print("Your guess was not correct.")
     count = count + 1  #This will count the number of times the user made a guess
else:
     print("Congratulations! You guessed it!")
     print()  
print (f"It took you {count} guesses.")

