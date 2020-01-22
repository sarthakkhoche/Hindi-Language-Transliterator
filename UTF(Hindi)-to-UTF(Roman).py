dict = {
'\u0915' : '\u006b' + '\u0061', #Hindi waala ka
'\u0916' : '\u006b' + '\u0068' + '\u0061', #kha
'\u0917' : '\u0067' + '\u0061', #ga
'\u0918' : '\u0067' + '\u0068' + '\u0061', #gha
'\u091A' : '\u0063' + '\u0068' + '\u0061', #cha
'\u091B' : '\u0063' + '\u0068' + '\u0068' + '\u0061', #chha
'\u091C' : '\u006a' + '\u0061', #ja
'\u091D' : '\u006a' + '\u0068' + '\u0061', #jha
'\u091F' : '\u1d75' + '\u0061', #Ta
'\u0920' : '\u1d75' + '\u0068' + '\u0061', #Tha
'\u0921' : '\u0111' + '\u0061', #Da
'\u0922' : '\u0111' + '\u0068' + '\u0061', #Dha
'\u0924' : '\u0074' + '\u0061', #ta
'\u0925' : '\u0074' + '\u0068' + '\u0061', #tha
'\u0926' : '\u0064' + '\u0061', #da
'\u0927' : '\u0064' + '\u0068' + '\u0061', #dha
'\u0928' : '\u006e' + '\u0061', #na
'\u092A' : '\u0070' + '\u0061', #pa
'\u092B' : '\u0066' + '\u0061', #fa
'\u092C' : '\u0062' + '\u0061', #ba
'\u092D' : '\u0062' + '\u0068' + '\u0061', #bha
'\u092E' : '\u006d' + '\u0061', #ma
'\u092F' : '\u0079' + '\u0061', #ya
'\u0930' : '\u0072' + '\u0061', #ra
'\u0932' : '\u006c' + '\u0061', #la
'\u0935' : '\u0076' + '\u0061', #va
'\u0936' : '\u0073' + '\u0068' + '\u0061', #sha
'\u0938' : '\u0073' + '\u0061', #sa
'\u0939' : '\u0068' + '\u0061', #ha
'\u0906' : '\u00e3', #aa ki matra
'\u0908' : '\u0069', #i
'\u0908' : '\u0069', #i ki matra
'\u090e' : '\u0065', #e ki matra
'\u0913' : '\u006f' #e ki matra
'\u0909' : '\u0075', #e ki matra
}

print(dict)

#Ignore last a if char is followed by vowel(Khana)
#Ignore the last a in entire word (Sarthak)
# i will follow the word in case of small i ki matra (Sakina)
#Downward tile will remove the succeding a (Madhya)
