from nltk.tokenize import word_tokenize

vowels = ['a','i','o','e','u']

def tokenize(text):
    return word_tokenize(text)

def ascii_to_hindi(text):
    words = tokenize(text)

    for i in words:
        word = ""
        for j in range(0,len(i)):
            
            if(i[j] in vowels):
                word += i[j]
                print(word)
                word = ""

            else:
                word += i[j]

if __name__ == "__main__":
    ascii_to_hindi("Zyaada")