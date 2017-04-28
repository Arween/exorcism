print("Select difficulty level: easy, middle, hard")
text = input("Level: ")
for word in text:
    if word == '?':
        print('Bob answers: "Sure."')
        break
    if word == '!':
        print('Bob answers: "Whoa, chill out!"')
        break
if text.isupper():
    print('Bob answers: "Whoa, chill out!"')
elif text.isspace() | text.isdigit():
    print('Bob answers: "Fine. Be that way!"')
else:
    print('Whatever."')




print("Select difficulty level: easy, middle, hard")
dna = (input("Level: ")).upper()
# G -> C
# C -> G
# T -> A
# A -> U
rna = ""
for letter in dna:
    if letter == 'G':
        letter = 'C'
    elif letter == 'C':
        letter = 'G'
    elif letter == 'T':
        letter = 'A'
    else:
        letter = 'U'
    rna += letter

print(rna)

n = 0
words = input("Level: ")
list_words = words.split()
for w in list_words:
    if words.find(w) != -1:
        n += 1

print(n)