# Bob
# Bob is a lackadaisical teenager. In conversation, his responses are very limited.
# Bob answers 'Sure.' if you ask him a question.
# He answers 'Whoa, chill out!' if you yell at him.
# He says 'Fine. Be that way!' if you address him without actually saying anything.
# He answers 'Whatever.' to anything else.


print("Task 1")

def answer_Bob():

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

answer_Bob()

# Rna Transcription
# Given a DNA strand, return its RNA complement (per RNA transcription).
# Both DNA and RNA strands are a sequence of nucleotides.

print("Task 2. GCTA -> CGAU")

def gcta_cgau():
    dna = (input("Value: ")).upper()
    # G -> C
    # C -> G
    # T -> A
    # T -> U
    rna = ""
    if len(dna) >= 4:
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
    else: print('Less than 4')
gcta_cgau()


# Word Coun
# Given a phrase, count the occurrences of each word in that phrase
# For example for the input "olly olly in come free


print("Word Count")

def word_count():
    words = input("Text: ")
    my_words = words.lower().split()
    my_dict = {}
    for item in my_words:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1
    print(my_dict)


word_count()