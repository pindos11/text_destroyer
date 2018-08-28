def change_sym( char ):
    letters = {
        1040:'A',
        1041:'6',
        1042:'B',
        1043:'I`',
        1044:'D',
        1045:'E',
        1025:'E',
        1046:'>|<',
        1047:'3',
        1048:'U',
        1049:'U',
        1050:'K',
        1051:'JI',
        1052:'M',
        1053:'H',
        1054:'O',
        1055:'II',
        1056:'P',
        1057:'C',
        1058:'T',
        1059:'y',
        1060:'F',
        1061:'X',
        1062:'II,',
        1063:'4',
        1064:'III',
        1065:'III,',
        1066:'`b',
        1067:'bl',
        1068:'b',
        1069:'E',
        1070:'I-O',
        1071:'9I'
        }
    try:
        s = letters[char]
    except:
        s = char
    return s

def change_text(text):
    otext = ''
    for i in text:
        t = i.upper()
        f = change_sym(ord(t))
        try:
            f = chr(f)
        except:
            f = f
        otext+=f
    return otext

while(1):
    it = input('Text: ')
    it = change_text(it)
    print(it)
    print()
            
