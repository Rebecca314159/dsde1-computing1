#First Part
message = 'If this has printed, you have run the code successfully.'
print(message)

#Second Part - the input function
this = input('What is your message?')
print(this)

#Third Part - Guessing a random number 
import random
number = random.randint(1,10)
#print(number)
user = int(input('Guess a number between 1 and 10:'))
print(bool(number==user))