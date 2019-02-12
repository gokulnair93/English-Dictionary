#  Dictionary  #
#  ----------  #

import json
import difflib
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

#Function for retriving definition
def retrive_definition(word):
    # Converting all letters to lower because out data is in that format
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]   #definition of words that start with a capital letter
    elif word.upper() in data:
        return data[word.upper()]   #definition of acronyms
    elif len(get_close_matches(word, data.keys())) > 0:             #To get a close match

        action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys(), n=1)[0])
        if (action == "y" or "Y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action == "n" or "N"):
            return ("Apologies! The word doesn't exist in our database.")
        elif ((action != "n" or "N") or (action != "y" or "Y")):
            return ("Invalid Entry! Please try again later.")

    else:
        return ("Apologies! The word doesn't exist in our database.")

word_user = input("Enter the word: ")
output = retrive_definition(word_user)

#If a word has more than one definition, print them recursively
if type(output) == list:
    print(str(word_user) + " has multiple meaning in our database. They're as follows: \n")
    for item in output:
        print("•", item)
else:
    print(str(word_user) + " meaning as per our database is: \n")
    print("•", output)
