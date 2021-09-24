import time as t
import datetime
import getpass
import os
import random as ran

answer="notext"
halign="notext"
link="https://drive.google.com/open?id=16AcLcgRRLlM7chKUi4eHgT-NOfBCnArM"
text="schreib den text:"
truehex = { 'a': '61',    'A': '41', 'b': '62',    'B': '42',
            'c': '63',    'C': '43', 'd': '64',    'D': '44',
            'e': '65',    'E': '45', 'f': '66',    'F': '46',
            'g': '67',    'G': '47', 'h': '68',    'H': '48',
            'i': '69',    'I': '49', 'j': '6A',    'J': '4A',
            'k': '6B',    'K': '4B', 'l': '6C',    'L': '4C',
            'm': '6D',    'M': '4D', 'n': '6E',    'N': '4E',
            'o': '6F',    'O': '4F', 'p': '70',    'P': '50',
            'q': '71',    'Q': '51', 'r': '72',    'R': '52',
            's': '73',    'S': '53', 't': '74',    'T': '54',
            'u': '75',    'U': '55', 'v': '76',    'V': '56',
            'w': '77',    'W': '57', 'x': '78',    'X': '58',
            'y': '79',    'Y': '59', 'z': '7A',    'Z': '5A',
            '0': '30',    '1': '31', '2': '32',    '3': '33',
            '4': '34',    '5': '35', '6': '36',    '7': '37',
            '8': '38',    '9': '39', ' ': '20',    '!': '21',
            ':': '3A',    '.': '2E', ',': '2C',    '@': '40',
            '[': '5B',    ']': '5D', '-': '2D',    '+': '2B',
            '(': '28',    ')': '29', '=': '3D',    '_': '5F',
            '&': '26',    '^': '5E', '%': '25',    '$': '24',
            '£': 'A3',    '"': '22', "'": '27',    '<': '3C',
            '>': '3E',    '|': '7C', '\\': '5C',    '/': '2F',
            '#': '23',    '~': '7E', '`': '60',    '*': '2A',
            '{': '7B',    '}': '7D', '?': '3F',    'ö': 'F6',
            'Ö': 'D6',    'ü': 'FC', 'Ü': 'DC',    'ä': 'E4',
            'Ä': 'C4',    '°': 'B0', '§': 'A7',    'ß': 'DF'}
            
hexlist = { 'a': '01',    'A': '02', 'b': '03',    'B': '04',
            'c': '05',    'C': '06', 'd': '07',    'D': '08',
            'e': '09',    'E': '0A', 'f': '0B',    'F': '0C',
            'g': '0D',    'G': '0E', 'h': '0F',    'H': '11',
            'i': '12',    'I': '13', 'j': '14',    'J': '15',
            'k': '16',    'K': '17', 'l': '18',    'L': '19',
            'm': '1A',    'M': '1B', 'n': '1C',    'N': '1D',
            'o': '1E',    'O': '1F', 'p': '20',    'P': '21',
            'q': '22',    'Q': '23', 'r': '24',    'R': '25',
            's': '26',    'S': '27', 't': '28',    'T': '29',
            'u': '2A',    'U': '2B', 'v': '2C',    'V': '2D',
            'w': '2E',    'W': '2F', 'x': '30',    'X': '31',
            'y': '32',    'Y': '33', 'z': '34',    'Z': '35',
            '1': '36',    '6': '37', '2': '38',    '7': '39',
            '3': '3A',    '8': '3B', '4': '3C',    '9': '3D',
            '5': '3E',    '0': '3F', ' ': '40',    '!': '41',
            ':': '42',    '.': '43', ',': '44',    '@': '45',
            '[': '46',    ']': '47', '-': '48',    '+': '49',
            ')': '4A',    '(': '4B', '=': '4C',    '_': '4D',
            '&': '4E',    '^': '4F', '%': '50',    '$': '51',
            '£': '52',    '"': '53', "'": '54',    '<': '55',
            '>': '56',    '|': '57', '\\': '58',   '/': '59',
            '#': '5A',    '~': '5B', '`': '5C',    '*': '5D',
            '{': '5E',    '}': '5F', '?': '60',    'ö': '61',
            'Ö': '62',    'ü': '63', 'Ü': '64',    'ä': '65',
            'Ä': '66',    '°': '67', '§': '68',    'ß': '70'}

binary = { 'a': '00000001',    'A': '00000010', 'b': '00000011',    'B': '00000100',
           'c': '00000101',    'C': '00000110', 'd': '00000111',    'D': '00001000',
           'e': '00001001',    'E': '00001010', 'f': '00001011',    'F': '00001100',
           'g': '00001101',    'G': '00001110', 'h': '00001111',    'H': '00010000',
           'i': '00010001',    'I': '00010010', 'j': '00010011',    'J': '00010100',
           'k': '00010100',    'K': '00010101', 'l': '00010110',    'L': '00010111',
           'm': '00010111',    'M': '00011000', 'n': '00011001',    'N': '00011010',
           'o': '00011011',    'O': '00011100', 'p': '00011101',    'P': '00011110',
           'q': '00011111',    'Q': '00100000', 'r': '00100001',    'R': '00100010',
           's': '00100011',    'S': '00100100', 't': '00100101',    'T': '00100110',
           'u': '00100111',    'U': '00101000', 'v': '00101001',    'V': '00101010',
           'w': '00101011',    'W': '00101100', 'x': '00101101',    'X': '00101110',
           'y': '00101111',    'Y': '00110000', 'z': '00110001',    'Z': '00110010',
           '1': '00110011',    '6': '00110100', '2': '00110101',    '7': '00110110',
           '3': '00110111',    '8': '00111000', '4': '00111001',    '9': '00111010',
           '5': '00111011',    '0': '00111100', ' ': '00111101',    '!': '00111110',
           ',': '00111111',    '@': '01000000', '[': '01000001',    ']': '01000010',
           '-': '01000011',    '+': '01000100', ')': '01000101',    '(': '01000110',
           '=': '01000111',    '_': '01001000', '&': '01001001',    '^': '01001010',
           '%': '01001011',    '$': '01001100', '£': '01001101',    '"': '01001110',
           "'": '01001111',    '<': '01010000', '>': '01010001',    '|': '01010010',
           '\\':'01010011',    '/': '01010100', '#': '01010101',    '~': '01010110',
           '`': '01010111',    '*': '01011000', '{': '01011001',    '}': '01011010',
           '?': '01011011',    'ö': '01011100', 'Ö': '01011101',    'ü': '01011110',
           'Ü': '01011111',    'ä': '01100000', 'Ä': '01100001',    '°': '01100010',
           '§': '01100011',    'ß': '01100101'}

print("Willkommen zu meinem Selbstgemachten text Converter.")
print("Um die ''Hilfeseite'' zu bekommen kann man Help schreiben.")
print("Jetzt gibt es Mehrere wege text zu convertieren.")
print(f"schreib help um die hilfeseite zu bekommen.\n")
def main():
    global answer
    while True:
        try:
            try:
                name = getpass.getuser()
                answer = input("{}@DESKTOP:~$ ".format(name))
                os.system('cls')

                if answer.lower() == 'phex':
                    hexstyle()

                elif answer.lower() == 'pbinary':
                    binstyle()

                elif answer.lower() == "thex":
                    truehex1()

                elif answer.lower() == "google":
                    print(f"\n11 01 18 18 1E 44 40 13 05 0F 40 03 12 1C 26 43 40 0E 1E 1E 0D 18 09 43 \n")

                elif answer.lower() == "phildev":
                    print(f"\n11 01 18 18 1E 44 40 12 05 0F 40 04 12 1C 40 21 0F 12 18 08 09 2C 44 40 2A 1C 07 40 12 05 0F 40 03 12 1C 40 0D 09 24 01 07 09 40 1C 1E 05 0F 40 01 1A 40 01 24 03 09 12 28 09 1C 40 2C 1E 1C 40 07 09 1A 40 27 20 12 09 18 40 0E 24 01 20 26 0F 1E 28 43 40 08 01 26 40 24 09 18 09 01 26 09 40 07 01 28 2A 1A 40 12 26 28 40 38 3F 40 14 2A 1C 12 43\n\nTip: nutz phex zum decodieren. ;)\n")

                elif answer.lower() == "bumblebee bee":
                    print(f"\n27 28 12 05 0F 40 2E 12 09 40 09 12 1C 09 40 04 12 09 1C 09 43 \n")

                elif answer.lower() == "update":
                    os.system('cls')
                    print("Hier. ↓")
                    print(f"{link}")
                    print(f"2. Link bald da.\n")

                elif answer.lower() == "test":
                    os.system('cls')
                    print(f"\nyay, Es funktioniert.\n")

                elif answer.lower() == "close test":
                    close()

                elif answer.lower() == 'help':
                    print(f"Hier sind die komandos:")
                    print(f"der Command phex Bringt dich zum Pseudo Hex converter.")
                    print(f"der Command pbinary Bringt dich zum Pseudo Binary converter.")
                    print(f"der Command thex Brinigt dich zum Hex converter.")
                    print(f"Zum Update link update schreiben.")
                    print(f"Und es gibt seecrets. ;)")
                    print(f"Binary wird Evtl. bald hinugefügt. Kontaktiier mich bitte")
                    print(f"wenn du willst das Binary hinzugefügt Wird oder neue text caracter hinzugefügt werden.\n")

                elif answer.lower() == 'email':
                    print(f"\nHier: Volkswagenfelge@gmail.com")
                    print(f"Bitte gib ein feedback ab. ;)\n")

                elif answer.lower()=="time":
                    time()

                elif answer.lower()=="halt":
                    print("that person that can see that is a Pro.")
                    exit()

                elif answer.lower() == "exit":
                    closing()

                elif answer == "":        
                    print(f"Hahaha, Du hast nichts eingegeben. :(\n\nversuch es mit help.\n")

                else:
                    os.system('cls')
                    wrongtxt()
                
            except KeyboardInterrupt:
                close()

        except TypeError:
            print(f"\nWut?\n")

def hexstyle():
    global halign
    global answer
    while True:
        try:
            try:
                hanswer = input("Von oder Zu Pseudo Hex? ")
                if hanswer.lower() == 'decode':
                    print(f"\n", text, "\n")
                    encode_s = input(' >> ')
                    print()
                    print(''.join(list(hexlist.keys())[list(hexlist.values()).index(c)] for c in encode_s.split()))
                    print()
                    reconvert()

                elif hanswer.lower() == 'encode':
                    print()
                    print(text)
                    print()
                    decode_s = input(' >> ')
                    print()
                    print(' '.join(hexlist[c] for c in decode_s))
                    print()
                    reconvert()

                elif hanswer.lower() == 'help':
                    os.system('cls')
                    align="PH"
                    helpsite()

                elif hanswer.lower() == "exit":
                    os.system('cls')
                    main()

                elif hanswer.lower() == "":
                    os.system('cls')
                    print(f"-_-\n")

                else:
                    os.system('cls')
                    wrongtxt()
            except KeyboardInterrupt:
                close()

        except ValueError:
            print("Wut?")
            

def truehex1():
    global halign
    global answer
    while True:
        try:
            try:
                hanswer = input("von oder zu True Hex? ")
                if hanswer.lower() == 'decode':
                    print(text)
                    print()
                    encode_s = input(' >> ')
                    print(''.join(list(truehex.keys())[list(truehex.values()).index(c)] for c in encode_s.split()))
                    print()
                    reconvert()

                elif hanswer.lower() == 'encode':    
                    print(text)
                    decode_s = input(' >> ')
                    print(' '.join(truehex[c] for c in decode_s))
                    print()
                    reconvert()

                elif hanswer.lower() == 'help':
                    os.system('cls')
                    halign="TH"
                    helpsite()
                    
                elif hanswer.lower() == "exit":
                    os.system('cls')
                    main()

                elif hanswer.lower() == "":
                    os.system('cls')
                    print(f"-_-\n")
                    
                else:
                    os.system('cls')
                    wrongtxt()

            except KeyboardInterrupt:
                close()

        except ValueError:
            print(f"Wut?\n")

def binstyle():
    global halign
    global answer
    while True:
        try:
            try:
                banswer = input("zu oder von Pseudo Binary? ")
                if banswer.lower() == 'decode':
                    print(text)
                    encode_s = input(' >> ')
                    print(''.join(list(binary.keys())[list(binary.values()).index(c)] for c in encode_s.split()))
                    print()
                    reconvert()

                elif banswer.lower() == 'encode':
                    os.system('cls')
                    print(text)
                    decode_s = input(' >> ')
                    print(' '.join(binary[c] for c in decode_s))
                    print()
                    reconvert()

                elif banswer.lower() == 'help':
                    os.system('cls')
                    halign="PB"
                    helpsite()

                elif banswer.lower() == "exit":
                    os.system('cls')
                    return
                    
                else:
                    os.system('cls')
                    wrongtxt()
                
            except KeyboardInterrupt:
                close()
        
        except ValueError:
            print(f"Wut?\n")

def reconvert():
    while True:
        question = input("wieder convertieren? ")
        os.system('cls')

        if question.lower() == 'ja':
            os.system('cls')
            return

        elif question.lower() == 'nein':
            os.system('cls')
            main()

        else:
            print(f"Wut?\n")

def wrongtxt():
    global answer
    number=ran.randint(1, 5)
    if number == 1:
        print(f"Was? das itst kein Command! bitte gib help nicht {answer} ein.\n")

    if number == 2:
        print(f"oh. Schreib einfach help. nicht {answer}.\n")

    if number == 3:
        print(f"Nope, {answer} ist nicht hier Drinnen. nutz help.\n")

    if number == 4:
        print(f"Nein nein nein! nicht {answer}. Bitte nutz help\n")

    if number == 5:
        print(f"Schreib help. {answer} ist kein command.\n")
    
    return

def helpsite():
    global halign
    os.system('cls')
    if halign == "PB":
        text="pseudo binary"

    if halign == "PH":
        text="pseudo hex"

    if halign == "TH":
        text="true hex"

    print(f"Hier sind ein paar commands:\n")
    print(f"encode Convertiert text zu {text}.")
    print(f"decode Convertiert {text} zu text.")
    print(f"Exit bringt dich zum hauptmenü.\n")
    return

def time():
    try:
        now=datetime.datetime.now()
        print(f"Die zeit ist: ", now.strftime("%d/%m/%Y, %H:%M:%S"), "\n")
        return

    except:
        print(f"Wir haben die Zeit zerstört. :(\n")
        main()

def close():
    os.system('cls')
    while True:
        print(f"willst du das program Schließen?\n")
        leave=input("Ja oder Nein? ")
        print()
        if leave.lower() == "ja":
            closing()

        elif leave.lower() == "nein":
            os.system('cls')
            return
        else:
            print(f"Was? Bitte sag ja oder nein. nicht {leave}.\n")

def closing():
    os.system('cls')
    Christmas = 12
    now = datetime.datetime.now()

    if now.month == Christmas:
        print("Es ist die weihnachtszeit")
        print("und das heißt das datenräuber")
        print("eure daten nicht stehlen")
        print("dürfen. (das convertier")
        print("nur Text. aber schon so")
        print("das keiner es lesen kann)")
        print("unhd das heißt das alle")
        print("textnachrichten in")
        print("pseudo-hex convertier")
        print("sind. Ich wünsche allen ein")
        print(f"Frohes fest. Hohoho. :D")
        t.sleep(10)
        exit()
        
    else:
        print("Vielen dank für die nutzung")
        print("von meinem eigenen text Convertierer.")
        print("ich versuche features hinzuzufügen und")
        print("versuche den Code zu reparieren  wenn ")
        print("etwas ist. mich würde es Freuen wenn du")
        print(f"feedback geben würdest. Email adresse: volkswagenfelge@gmail.com\n")
        t.sleep(10)
        exit()

main()
