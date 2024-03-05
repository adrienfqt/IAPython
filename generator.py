import json, random

with open("ressources/liste_probabilites_fr.json", 'r', encoding='utf-8') as fichier:
    letters_proba = json.load(fichier)

def testChar(test_char, word):
    if test_char == "_" and len(word) < 2:
        #Si le mot fait moins de 2 caractères on relance
        return False
    
    if len(word) > 2 and (test_char == word[-1] == word[-2]):
        #Si on a 3 fois le même caractère on relance
        return False
    
    if len(word) == 1 and (test_char == word[0]):
        #Si les deux premiers caractères sont identiques on relance
        return False

    return True


def generer_mot(probabilities_list):
    word = ""
    current_char = "#"
    while current_char != "_":
        next_chars_list = probabilities_list[current_char]
        if next_chars_list:
            next_chars = next_chars_list.keys()
            probas = next_chars_list.values()
        else:
            next_chars, probas = ['_'], [1]
        

        test_char = random.choices(list(next_chars), weights=list(probas))[0]

        test_status = testChar(test_char, word)

        if not test_status:
            continue

        current_char = test_char
        
        if current_char != "_":
            word += current_char
        
    return word

for i in range(100):
    print(generer_mot(letters_proba))

