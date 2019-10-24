'''
keywords.py

Create functions that use keyword arguments
with default values.
'''

# Create a function called welcome_message():
# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>

def welcome_message(user_name = '', place = ''):
    if user_name == '' and place == '':
        greeting = 'Hello and welcome'
    elif user_name != '' and place == '':
        greeting = 'Hello, ' + user_name + ', and welcome'
    elif user_name == '' and place != '':
        greeting = 'Hello and welcome to ' + place
    elif user_name != '' and place != '':
        greeting = 'Hello, ' + user_name + ', and welcome to ' + place
    return greeting 

# Create a function called list_average()
# without using any libraries to do the maths for you 
# (the point of this exercise is to practice interacting 
# with lists)
# the first argument is a list of numbers
# the second optional keyword arguemt is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list 
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list
def list_average(numbers = [1,2,3,4,4,5,6], avg_type = ''):
    if len(numbers) == 0:
        num = 0
    if numbers == []:
        num = 0
    elif avg_type == '' or avg_type == 'mean':
        num = sum(numbers) / len(numbers)
    elif avg_type == 'mode':
        counter = 0
        num = numbers[0] 
        for i in numbers: 
            frequency = numbers.count(i) 
            if(frequency > counter): 
                counter = frequency 
                num = i 
    elif avg_type == 'median':
        numbers.sort()
        num = numbers[int(len(numbers)/2)]
    return num
