import json, random

with open("ressources/liste_probabilites_fr.json", 'r', encoding='utf-8') as fichier:
    letters_proba = json.load(fichier)

def generer_mot(probabilities_list):
    word = "##"
    current_char = "#"
    while current_char != "_":
        before_char = word[-2]
        next_chars_list = probabilities_list[before_char][current_char]
        if next_chars_list:
            next_chars = next_chars_list.keys()
            probas = next_chars_list.values()
        else:
            next_chars, probas = ['_'], [1]
        

        current_char = random.choices(list(next_chars), weights=list(probas))[0]
        
        if current_char != "_":
            word += current_char
        
    return (word[2:]).capitalize()

for i in range(100):
    print(generer_mot(letters_proba))

