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
            # unicode += +

        elif(akshara[0] in it3_to_utf.keys()):
            unicode += it3_to_utf[akshara[0]]
            unicode += '\u0948'

            if((akshara[1:]+'a') in it3_to_utf.keys()):
                unicode += it3_to_utf[(akshara[1:]+'a')]

    if(len(akshara) == 1):
        if((akshara+'a') in it3_to_utf.keys()):
            unicode += it3_to_utf[(akshara+'a')]
            # unicode += '+'

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
                # unicode += '+'
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
    # 'e' : '\u093F',
    'ee': '\u0940',
    'u' : '\u0941',
    'oo': '\u0942',
    'e': '\u0947',
    'ai': '\u0948',
    'o' : '\u094B',
    'ow': '\u094C',
}

first = {
    'a': '\u0905',
    'aa': '\u0906',
    'i': '\u0907',
    'ii': '\u0908',
    'ee': '\u0908',
    'u': '\u0909',
    'uu': '\u090a',
    'oo': '\u090a',
    'e': '\u090f',
    'ai': '\u0910',
    'o': '\u0913',
    'au': '\u0914',
}

it3_to_utf = {
    # 'a': '\u0905',
    # 'aa': '\u0906',
    # 'i': '\u0907',
    # 'ii': '\u0908',
    # 'u': '\u0909',
    # 'uu': '\u090a',
    # 'oo': '\u090a',
    # 'e': '\u090f',
    # 'ai': '\u0910',
    # 'o': '\u0913',
    # 'au': '\u0914',
    'k': '\u0915',
    'kh': '\u0916',
    'g': '\u0917',
    'gh': '\u0918',
    'ch': '\u091a',
    'chh': '\u091b',
    'j': '\u091c',
    'jh': '\u091d',
    'T': '\u091f',
    'Th': '\u0920',
    'D': '\u0921',
    'Dh': '\u0922',
    'N': '\u0923',
    't': '\u0924',
    'th': '\u0925',
    'd': '\u0926',
    'dh': '\u0927',
    'n': '\u0928',
    'p': '\u092a',
    'ph': '\u092b',
    'b': '\u092c',
    'bh': '\u092d',
    'm': '\u092e',
    'y': '\u092f',
    'r': '\u0930',
    'l': '\u0932',
    'v': '\u0935',
    'sh': '\u0936',
    'Sh': '\u0937',
    's': '\u0938',
    'h': '\u0939',
    'ph': '\u095e',
    'ksh': '\u0915'+'\u094d'+'\u0937',
    'tr': '\u0924'+'\u094d'+'\u0930',
    'br': '\u092c'+'\u094d'+'\u0930',
    'z': '\u095b'
}


if __name__ == "__main__":

    hinglish_to_hindi("kaksha")
