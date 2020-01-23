from nltk.tokenize import word_tokenize

vowels = ['a','i','o','e','u']

global_flag = False

def tokenize(text):
    return word_tokenize(text)

def convert_to_unicode(word):
    unicode = ''
    matra = word[-2:]

    akshara = word[:-2]
    if(len(akshara) == 2):
        if((akshara+'a') in it3_to_utf.keys()):
            unicode += it3_to_utf[(akshara+'a')]
            unicode += '+'

        elif(akshara[0] in it3_to_utf.keys()):
            unicode += it3_to_utf[akshara[0]]
            unicode += '+\u0948+'

            if((akshara[1:]+'a') in it3_to_utf.keys()):
                unicode += it3_to_utf[(akshara[1:]+'a')]

    if(len(akshara) == 1):
        if((akshara+'a') in it3_to_utf.keys()):
            unicode += it3_to_utf[(akshara+'a')]
            unicode += '+'

    #MATRA CHECK

    if(matra in matras.keys()):
        global_flag = True
        unicode += matras[matra]
    
    elif(matra[0] in matras.keys()):
        unicode += matras[matra[0]]

    
    return unicode
    


def hinglish_to_hindi(text):
    words = tokenize(text)

    global_flag = False
    final_sentence_unicode = ''
    for i in words:
        word = ""
        unicode = ''
        flag = False
        j=0
        while (j <len(i)):
            if(i[j] in vowels):
                word += i[j]
                if(j+1 < len(i)):
                    word += i[j+1]
                print(word)
                unicode += convert_to_unicode(word)
                unicode += '+'
                word = ""
                if(global_flag == True):
                    j +=1
                    global_flag=False
            else:
                flag = True
                word += i[j]
            j+=1
        final_sentence_unicode += unicode[:-1]
        final_sentence_unicode += " "
    print(final_sentence_unicode)
    
matras = {
    'aa': '\u093E',
    'i' : '\u093F',
    'e' : '\u093F',
    'ee': '\u0940',
    'u' : '\u0941',
    'oo': '\u0942',
    'ae': '\u0947',
    'ai': '\u0948',
    'o' : '\u094B',
    'ow': '\u094C',
}

it3_to_utf = {
    'a': '\u0905',
    'aa': '\u0906',
    'i': '\u0907',
    'ii': '\u0908',
    'u': '\u0909',
    'uu': '\u090a',
    'e': '\u090f',
    'ai': '\u0910',
    'o': '\u0913',
    'au': '\u0914',
    'ka': '\u0915',
    'kha': '\u0916',
    'ga': '\u0917',
    'gha': '\u0918',
    'cha': '\u091a',
    'chha': '\u091b',
    'ja': '\u091c',
    'jha': '\u091d',
    'Ta': '\u091f',
    'Tha': '\u0920',
    'Da': '\u0921',
    'Dha': '\u0922',
    'Na': '\u0923',
    'ta': '\u0924',
    'tha': '\u0925',
    'da': '\u0926',
    'dha': '\u0927',
    'na': '\u0928',
    'pa': '\u092a',
    'pha': '\u092b',
    'ba': '\u092c',
    'bha': '\u092d',
    'ma': '\u092e',
    'ya': '\u092f',
    'ra': '\u0930',
    'la': '\u0932',
    'va': '\u0935',
    'sha': '\u0936',
    'Sha': '\u0937',
    'sa': '\u0938',
    'ha': '\u0939',
    'pha': '\u095e'
}


if __name__ == "__main__":

    hinglish_to_hindi("naanaa")
