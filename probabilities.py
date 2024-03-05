import json

letters_proba = {}

def checkChars(word):
    formated_word = "##" + word + "_"
    for i in range (len(formated_word) - 2):
        char = formated_word[i]
        next_char = formated_word[i+1];
        next_next_char = formated_word[i+2];
        if letters_proba.get(char) is None:
            letters_proba[char] = {}
        if letters_proba[char].get(next_char) is None:
            letters_proba[char][next_char] = {}
        if letters_proba[char][next_char].get(next_next_char) is None:
            letters_proba[char][next_char][next_next_char] = 0
        letters_proba[char][next_char][next_next_char] += 1
            

file = open('ressources/liste_mots_fr_gutenberg_336k.txt', 'r', encoding='utf-8')
wordlist = file.readlines()

for line in wordlist:
    word = line.strip().lower()
    checkChars(word)

for before_letter_key, before_letter in letters_proba.items():
    for letter_key, letter in before_letter.items():
        total_letter = sum(letter.values())
        for key, next_letter in letter.items():
            letter[key] = next_letter / total_letter

# Convert and write JSON object to file
with open("ressources/liste_probabilites_fr.json", "w", encoding='utf8') as outfile: 
    json.dump(letters_proba, outfile, ensure_ascii=False)
print("Dump done to liste_probabilites_fr.json")