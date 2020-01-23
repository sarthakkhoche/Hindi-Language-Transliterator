dict = {
'\u0915' : ['\u006b', '\u0061'], #Hindi waala ka
'\u0916' : ['\u006b' , '\u0068' , '\u0061'], #kha
'\u0917' : ['\u0067' , '\u0061'], #ga
'\u0918' : ['\u0067' , '\u0068' , '\u0061'], #gha
'\u0919' : ['\u1e45', '\u0061'], #n(dot)a
'\u091A' : ['\u0063' , '\u0068' , '\u0061'], #cha
'\u091B' : ['\u0063' , '\u0068' , '\u0068' , '\u0061'], #chha
'\u091C' : ['\u006a' , '\u0061'], #ja
'\u091D' : ['\u006a' , '\u0068' , '\u0061'], #jha
'\u091E' : ['\u00f1', '\u0061'], #n(wave)a
'\u091F' : ['\u1d75' , '\u0061'], #Ta
'\u0920' : ['\u1d75' , '\u0068' , '\u0061'], #Tha
'\u0921' : ['\u0111' , '\u0061'], #Da
'\u0922' : ['\u0111' , '\u0068' , '\u0061'], #Dha
'\u0923' : ['\u0146' , '\u0061'], #n(dot below)a
'\u0924' : ['\u0074' , '\u0061'], #ta
'\u0925' : ['\u0074' , '\u0068' , '\u0061'], #tha
'\u0926' : ['\u0064' , '\u0061'], #da
'\u0927' : ['\u0064' , '\u0068' , '\u0061'], #dha
'\u0928' : ['\u006e' , '\u0061'], #na
'\u092A' : ['\u0070' , '\u0061'], #pa
'\u092B' : ['\u0066' , '\u0061'], #fa
'\u092C' : ['\u0062' , '\u0061'], #ba
'\u092D' : ['\u0062' , '\u0068' , '\u0061'], #bha
'\u092E' : ['\u006d' , '\u0061'], #ma
'\u092F' : ['\u0079' , '\u0061'], #ya
'\u0930' : ['\u0072' , '\u0061'], #ra
'\u0932' : ['\u006c' , '\u0061'], #la
'\u0935' : ['\u0076' , '\u0061'], #va
'\u0936' : ['\u0073' , '\u0068' , '\u0061'], #sha
'\u0938' : ['\u0073' , '\u0061'], #sa
'\u0939' : ['\u0068' , '\u0061'], #ha
'\u0906' : ['\u00e3'], #aa
'\u093E' : ['\u00e3'], #aa ki matra
'\u0908' : ['\u0069'], #i
'\u0940' : ['\u0069'], #i ki matra
'\u090E' : ['\u0065'], #e
'\u0947' : ['\u0065'], #e ki matra
'\u0909' : ['\u0075'], #u
'\u0941' : ['\u0075'], #u ki matra
'\u0971' : ['\u006e'], #bindu
'\u094D' : ['\u097D'] #dummy for half matra
}

vowels = ['\u00e3', '\u0069', '\u0065', '\u006f', '\u0075']
half = ['\u097D']

def array_concat(x):
    text = ''
    for i in range(len(x)):
        text += x[i]
    return text

#Sarthak
word1 = ['\u0938', '\u093E', '\u0930', '\u094D', '\u0925', '\u0915']
# print(array_concat(word1))

#Khaana
word2  = ['\u0916', '\u093E', '\u0928', '\u093E']
# print(array_concat(word2))

#Ulta
word3 = ['\u0924', '\u0930', '\u092C', '\u0941', '\u091C']
# print(array_concat(word3))

#Ulta
word4 = ['\u0909', '\u0932', '\u094D', '\u091F', '\u093E']
# print(array_concat(word4))

# Brahma
word5 = ['\u092C', '\u094D', '\u0930', '\u0939', '\u092E', '\u093E']
# print(array_concat(word5))

#Dekhna
word6 = ['\u0926', '\u0947', '\u0916', '\u0928', '\u093E']
# print(array_concat(word6))

#Tarbuj
word7 = ['\u0924', '\u0930', '\u092C', '\u0941', '\u091C']
# print(array_concat(word7))

#Gandharv
word8 = ['\u0917', '\u0971', '\u0927', '\u0930', '\u094D', '\u0935']
print(array_concat(word8))


def text_generator(word):
    text = []
    for i in range(len(word)):
        text.append(array_concat(dict[word[i]]))
    return text

def cleanup_maatra(x):
    for i in range(len(x)):
        if x[i] in vowels:
            x[i-1] = x[i-1][:-1]
    return x

final1= []
def cleanup_half(x):
    for i in range(len(x)):
        if x[i] in half:
            x[i-1] = x[i-1][:-1]
    for i in range(len(x)):
        if x[i] not in half:
            final1.append(x[i])
    return final1

def cleanup_a(x):
    if x[-1] not in vowels:
        x[-1] = x[-1][:-1]
    return x

first_clean = cleanup_maatra(text_generator(word8))
second_clean = cleanup_half(first_clean)
third_clean = cleanup_a(second_clean)

# print(first_clean)
# print(second_clean)
# print(third_clean)

print(array_concat(third_clean))
