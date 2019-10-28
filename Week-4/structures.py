#'''
#structures.py

#Simple functions performing operations on basic Python data structures.  
#'''

# Lists
import string
# write a function that returns a list containig the first and the last element
# of "the_list". 

def first_and_last(the_list):
    '''Returns a list with the first and last elements of the input list.'''
    new_list = [the_list[0], the_list[-1]]
    return new_list


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any og the indices is out of the
# list, raise a "ValueError" exception. 

def part_reverse(the_list, beginning, end):
    '''Slices the first list variable between the second and third variables, then returns the reverse.'''
    if beginning > end or end > len(the_list) or beginning > len(the_list):
        raise ValueError
    if beginning != int or end >= int:
        raise TypeError
    new = the_list[beginning, end]
    new.reverse()
    return new

# hint this is incomplete

# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 

def repeat_at_index(the_list, index):
    '''Repeat the element of the input list at the imputted index 3 times in a new list.'''
    if index != int:
        raise TypeError
    new = the_list[0, index] + the_list[index]*3 + the_list[index+1, -1]
    return new


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards

def palindrome_word(word):
    '''Checks if a word is a palindrome.'''
    if word == word [::-1]:
       return True 
    else:
        return False

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 

def palindrome_sentence(sentence):
    '''Checks if a sentence without punctuation is a palindrome.'''
    sentence.lower()
    sentence = sentence.replace(' ', '')
    sentence = sentence.join(e for e in string if e.isalnum())
    if sentence == sentence [::-1]:
        return True 
    else:
        return False
   

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 

def concatenate_sentences(sentence1, sentence2):
    '''Concatenates two imput sentences if they start with a capital and end with a full stop, etc.'''
    if sentence1[0].isupper and sentence1[-1] == '.' or sentence1[-1] == '?' or sentence1[-1] == '!':
        pass
    if sentence2[0].isupper and sentence2[-1] == '.' or sentence2[-1] == '?' or sentence2[-1] == '!':
        pass
    else:
        return False
    sentence1.strip()
    sentence2.strip()
    return sentence1 + ' ' + sentence2


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    '''Checks if a key exists in a dictionary.'''
    if key in dictionary:
        return True
    else:
        return False

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    '''Checks if a value exists in a dictionary.'''
    if value in dictionary.values():
        True
    else:
        False

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    '''Merges two dictionaries.'''
    return dictionary1.update(dictionary2)
