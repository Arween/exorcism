# Bob
# Bob is a lackadaisical teenager. In conversation, his responses are very limited.
# Bob answers 'Sure.' if you ask him a question.
# He answers 'Whoa, chill out!' if you yell at him.
# He says 'Fine. Be that way!' if you address him without actually saying anything.
# He answers 'Whatever.' to anything else.


print("Task 1")
text = input("Your question: ")
flag1 = True
flag2 = True
for word in text:
    if word == '?':
        print('Bob answers: "Sure."')
        flag1 = False
        break
    if word == '!':
        print('Bob answers: "Whoa, chill out!"')
        flag2 = False
        break
if text.isupper() and flag2:
    print('Bob answers: "Whoa, chill out!"')
elif text.isspace() | text.isdigit():
    print('Bob answers: "Fine. Be that way!"')
elif flag1 and flag2:
    print('Whatever."')

# Rna Transcription
# Given a DNA strand, return its RNA complement (per RNA transcription).
# Both DNA and RNA strands are a sequence of nucleotides.

print("Task 2. GCTA -> CGAU")
dna = (input("Value: ")).upper()
# G -> C
# C -> G
# T -> A
# T -> U
rna = ""
if dna.length >= 4:
    for letter in dna:
        if letter != 'G' and letter != 'C' and letter != 'T' and letter != 'T' :
            print('Only : G-C-T-A')
            break
        elif letter == 'G':
            letter = 'C'
        elif letter == 'C':
            letter = 'G'
        elif letter == 'T':
            letter = 'A'
        else:
            letter = 'U'
        rna += letter

    print(rna)


# Word Coun
# Given a phrase, count the occurrences of each word in that phrase
# For example for the input "olly olly in come free


n = 0
words = input("Text: ")
list_words = words.split()
for w in list_words:
    for w2 in list_words:
        if w == w2:
            n += 1
    print(w + ': ' + str(n))
    n = 0

    # n = 0