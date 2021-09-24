import time as t
import datetime
import getpass
import os
import random as ran

answer="notext"
halign="notext"
link="https://drive.google.com/open?id=16AcLcgRRLlM7chKUi4eHgT-NOfBCnArM"
text="Write your text:"

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

print("Welcome to my Custom Text Converter.")
print("There is a Help site. you can access it With Help.")
print(f"Now there are Multiple Ways to convert text.\n")
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

                elif answer.lower() == 'pbin':
                    binstyle()

                elif answer.lower() == "thex":
                    truehex1()

                elif answer.lower() == "google":
                    print(f"11 12 44 40 12 28 54 26 40 1A 09 43 40 0E 1E 1E 0D 18 09 43 \n")

                elif answer.lower() == "phildev":
                    print(f"\n11 01 18 18 1E 44 40 12 05 0F 40 04 12 1C 40 21 0F 12 18 08 09 2C 44 40 2A 1C 07 40 12 05 0F 40 03 12 1C 40 0D 09 24 01 07 09 40 1C 1E 05 0F 40 01 1A 40 01 24 03 09 12 28 09 1C 40 2C 1E 1C 40 07 09 1A 40 27 20 12 09 18 40 0E 24 01 20 26 0F 1E 28 43 40 08 01 26 40 24 09 18 09 01 26 09 40 07 01 28 2A 1A 40 12 26 28 40 38 3F 40 14 2A 1C 12 43\n\nTip: nutz phex zum decodieren. ;)\n")

                elif answer.lower() == "bumblebee bee":
                    print(f"\n27 28 12 1C 0D 40 18 12 16 09 40 01 40 04 09 09 \n")

                elif answer.lower() == "update":
                    os.system('cls')
                    print("Here. ↓")
                    print(f"{link}")
                    print(f"2. link is soon there.\n")

                elif answer.lower() == "test":
                    os.system('cls')
                    print(f"\nYay, It worked.\n")

                elif answer.lower() == "close test":
                    close()

                elif answer.lower() == 'help':
                    print(f"Herre are the commands:")
                    print(f"The command phex sets the Converting mode to Pseudo Hex.")
                    print(f"The command pbin Sets the Converting mode to Pseudo Binary.")
                    print(f"THe command thex Sets the Converting mode to True Hex.")
                    print(f"to get the link for the Archive and versions, type update")
                    print(f"And there are secrets. ;)")
                    print(f"Normal Binary will be soon added, if you can help me, please contact me.\n")

                elif answer.lower() == 'email':
                    print(f"\nHier: Volkswagenfelge@gmail.com")
                    print(f"Please give feedback. ;)\n")

                elif answer.lower()=="time":
                    time()

                elif answer.lower()=="halt":
                    print("that person that can see that is a Pro.")
                    exit()

                elif answer.lower() == "exit":
                    closing()

                elif answer == "":        
                    print(f"Hahaha, you did not type anything. :(\n\nTry it with help.\n")

                else:
                    os.system('cls')
                    wrongtxt()

            except KeyboardInterrupt:
                close()

        except TypeError:
            print(f"\nWut?\n")

def hexstyle():
    global halign
    global hanswer
    while True:
        try:
            try:
                answer = input("Encode or Decode? ")
                if answer.lower() == 'decode':
                    print(f"\n", text, "\n")
                    encode_s = input(' >> ')
                    print()
                    print(''.join(list(hexlist.keys())[list(hexlist.values()).index(c)] for c in encode_s.split()))
                    print()
                    reconvert()

                elif answer.lower() == 'encode':
                    print()
                    print(text)
                    print()
                    decode_s = input(' >> ')
                    print()
                    print(' '.join(hexlist[c] for c in decode_s))
                    print()
                    reconvert()

                elif answer.lower() == 'help':
                    halign="PH"
                    helpsite()

                elif answer.lower() == "exit":
                    os.system('cls')
                    main()

                elif answer.lower() == "":
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
                answer = input("Encode or Decode? ")
                if answer.lower() == 'decode':
                    print(text)
                    print()
                    encode_s = input(' >> ')
                    print(''.join(list(truehex.keys())[list(truehex.values()).index(c)] for c in encode_s.split()))
                    print()
                    reconvert()

                elif answer.lower() == 'encode':    
                    print(text)
                    decode_s = input(' >> ')
                    print(' '.join(truehex[c] for c in decode_s))
                    print()
                    reconvert()

                elif answer.lower() == 'help':
                    halign="TH"
                    helpsite()

                elif answer.lower() == "exit":
                    os.system('cls')
                    main()

                elif answer.lower() == "":
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
    while True:
        try:
            try:
                answer = input("Encode or Decode? ")
                if answer.lower() == 'decode':
                    print(text)
                    encode_s = input(' >> ')
                    print(''.join(list(binary.keys())[list(binary.values()).index(c)] for c in encode_s.split()))
                    print()
                    reconvert()

                elif answer.lower() == 'encode':
                    os.system('cls')
                    print(text)
                    decode_s = input(' >> ')
                    print(' '.join(binary[c] for c in decode_s))
                    print()
                    reconvert()

                elif answer.lower() == 'help':
                    halign="PB"
                    helpsite()

                elif answer.lower() == "exit":
                    os.system('cls')
                    return
                    
                else:
                    os.system('cls')
                    wrongtxt()
                
            except KeyboardInterrupt:
                close()
        
        except ValueError:
            print(f"Wut?\n")

def wrongtxt():
    global answer
    number=ran.randint(1, 5)
    if number == 1:
        print(f"What? that is not a Command. please write help to Get the help list. not {answer}.\n")

    if number == 2:
        print(f"Ugh, please use help, not {answer}.\n")

    if number == 3:
        print(f"Wrong. it is Just encode or decode. not {answer}.\n")

    if number == 4:
        print(f"No no no! not {answer}. please use help\n")

    if number == 5:
        print(f"Write help to get the help site. {answer} is not an command.\n")
    
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

    print(f"Here are the Commands:\n")
    print(f"encode Converts text to {text}.")
    print(f"decode Converts {text} to text.")
    print(f"Exit brings you to the Main menu.\n")
    return

def reconvert():
    while True:
        question = input("Reconvert? ")
        os.system('cls')

        if question.lower() == 'yes':
            os.system('cls')
            return

        elif question.lower() == 'no':
            os.system('cls')
            main()

        else:
            print(f"Wut?\n")

def time():
    try:
        now=datetime.datetime.now()
        print(f"The time is: ", now.strftime("%m/%d/%Y, %H:%M:%S"), "\n")
        return

    except:
        print(f"We Destroyed time. :(\n")
        main()

def close():
    os.system('cls')
    while True:
        print(f"Do you want to Close that Program?\n")
        leave=input("Yes or No? ")
        print()
        if leave.lower() == "yes":
            closing()

        elif leave.lower() == "no":
            os.system('cls')
            return
        else:
            print(f"What? please say Yes or No. not {leave}.\n")

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
        print("Huge thanks for using my Text converter.")
        print("i try to add features, but some times i have no idea,")
        print("What to put in. if there is a Typo, please say it to me.")
        print("i would really love to hear it something is wrong.")
        print(f"if you Could please give some feedback: volkswagenfelge@gmail.com\n")
        t.sleep(10)
        exit()
main()
