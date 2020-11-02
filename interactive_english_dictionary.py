import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

def translate(word):
    with open(r'C:\Users\nsett\Desktop\Python\Curso mega python\data.json') as json_file:
        data = json.load(json_file)
        word = word.lower()
        if word in data:
            return  data[word]
        elif get_close_matches(word, data.keys(), n=1, cutoff=0.7):        
            best_match = get_close_matches(word, data.keys(), n=1, cutoff=0.7)
            input_confirmation = input(("Did you mean {}? Type 'Y' or 'N' ").format(best_match[0]))
            if input_confirmation.upper() == 'Y':
                return data[best_match[0]]
            else:
                return 'Thanks for using the translator'
        else:
            return 'Sorry, that word is not available in the translator'

input_user = input('Enter word: ')

output = translate(input_user)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
    

