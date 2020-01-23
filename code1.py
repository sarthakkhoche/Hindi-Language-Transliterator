from nltk.tokenize import word_tokenize

it3_to_utf = {
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

vowels = ['a','i','o','e','u']

def convert_to_unicode(word):
    unicode = ''
    i = 0
    j = 0
    if (word[:2] in first.keys()):
        unicode += it3_to_utf[word[:2]]
        i = 2
        j = 2
    elif (word[0] in ['a', 'i', 'u', 'e', 'o']):
        unicode += it3_to_utf[word[0]]
        i = 1
        j = 1
    else:
        while (i < len(word)):
            if (word[i] not in vowels):
                i+=1
            else:
                if (word[i:(i+2)] in matras.keys()):
                    unicode += it3_to_utf[word[j:i]] + matras[word[i:(i+2)]]  
                    i += 2
                    j = i
                elif (word[i] in matras.keys()):
                    unicode += it3_to_utf[word[j:i]] + matras[word[i]]
                    i += 1
                    j = i
                elif (word[i] == 'a'):
                    unicode += it3_to_utf[word[j:i]]
                    i += 1
                    j = i
    return unicode

def tokenize(text):
    return word_tokenize(text)

def hinglish_to_hindi(text):
    words = tokenize(text)

    global_flag = False
    final_sentence_unicode = ''
    for i in words:
        unicode = ''
        unicode += convert_to_unicode(i)
        final_sentence_unicode += unicode
        final_sentence_unicode += " "
    print(final_sentence_unicode)

if __name__ == "__main__":    
    hinglish_to_hindi("kakshaa")        