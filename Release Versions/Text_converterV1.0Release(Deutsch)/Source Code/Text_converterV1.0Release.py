import datetime
import time
import getpass
link="https://drive.google.com/open?id=16AcLcgRRLlM7chKUi4eHgT-NOfBCnArM"
text_decode = 'Enter string to Decode...'
text_encode = 'Type string to Encode...'
numbers = { 'a': '01',    'A': '02',
            'b': '03',    'B': '04',
            'c': '05',    'C': '06',
            'd': '07',    'D': '08',
            'e': '09',    'E': '0A',
            'f': '0B',    'F': '0C',
            'g': '0D',    'G': '0E',
            'h': '0F',    'H': '11',
            'i': '12',    'I': '13',
            'j': '14',    'J': '15',
            'k': '16',    'K': '17',
            'l': '18',    'L': '19',
            'm': '1A',    'M': '1B',
            'n': '1C',    'N': '1D',
            'o': '1E',    'O': '1F',
            'p': '20',    'P': '21',
            'q': '22',    'Q': '23',
            'r': '24',    'R': '25',
            's': '26',    'S': '27',
            't': '28',    'T': '29',
            'u': '2A',    'U': '2B',
            'v': '2C',    'V': '2D',
            'w': '2E',    'W': '2F',
            'x': '30',    'X': '31',
            'y': '32',    'Y': '33',
            'z': '34',    'Z': '35',
            '1': '36',    '6': '37',
            '2': '38',    '7': '39',
            '3': '3A',    '8': '3B',
            '4': '3C',    '9': '3D',
            '5': '3E',    '0': '3F',
            ' ': '40',    '!': '41',
            ':': '42',    '.': '43',
            ',': '44',    '@': '45',
            '[': '46',    ']': '47',
            '-': '48',    '+': '49',
            ')': '4A',    '(': '4B',
            '=': '4C',    '_': '4D',
            '&': '4E',    '^': '4F',
            '%': '50',    '$': '51',
            '£': '52',    '"': '53',
            "'": '54',    '<': '55',
            '>': '56',    '|': '57',
            '\\': '58',   '/': '59',
            '#': '5A',    '~': '5B',
            '`': '5C',    '*': '5D',
            '{': '5E',    '}': '5F',
            '?': '60',    'ö': '61',
            'Ö': '62',    'ü': '63',
            'Ü': '64',    'ä': '65',
            'Ä': '66',    '°': '67',
            '§': '68',    '!': '69',
            'ß': '70'}
print("Willkommen zu meinem Selbstgemachten text Converter.")
print()
print("Um die ''Hilfeseite'' zu bekommen kann man Help schreiben.")
print()
def main():
    try:
        name = getpass.getuser()
        answer = input("{}@DESKTOP:~$ ".format(name))
        print()
        if answer.lower() == 'decode':
            print(text_decode)
            encode_s = input(' >> ')
            print(''.join(list(numbers.keys())[list(numbers.values()).index(c)] for c in encode_s.split()))
            print()
            main()
        elif answer.lower() == 'encode':
            print(text_encode)
            decode_s = input(' >> ')
            print(' '.join(numbers[c] for c in decode_s))
            print()
            main()
        elif answer.lower() == "google":
            print("11 01 18 18 1E 44 40 13 05 0F 40 03 12 1C 26 43 40 0E 1E 1E 0D 18 09 43 ")
            print()
            main()
        elif answer.lower() == "philcodes":
            print(" 11 01 18 18 1E 44 40 13 05 0F 40 1A 01 05 0F 09 40 0D 09 24 01 07 09 40 09 12 1C 40 26 20 12 09 18 40 07 01 26 40 11 09 12 70 28 42 40 13 1C 40 29 0F 09 40 1B 12 1C 07 43 40 08 01 26 40 27 20 12 09 18 40 2E 12 24 07 40 03 01 18 07 40 2D 09 24 61 0B 0B 09 1C 28 18 12 05 0F 28 44 40 02 03 09 24 40 12 05 0F 40 2E 09 12 70 40 1C 1E 05 0F 40 16 09 12 1C 40 2D 09 24 61 0B 0B 09 1C 28 18 12 05 0F 2A 1C 0D 26 40 08 01 28 2A 1A 43 40 02 03 09 24 40 12 05 0F 40 2E 09 12 70 40 08 01 26 40 09 26 40 06 1E 1E 18 40 26 09 12 1C 40 2E 12 24 07 43 40 42 08 ")
            print()
            main()
        elif answer.lower() == "bumblebee bee":
            print("27 28 12 05 0F 40 2E 12 09 40 09 12 1C 09 40 04 12 09 1C 09 43 ")
            print()
            main()
        elif answer.lower() == "get.update":
            print("Hier. ↓")
            print("https://drive.google.com/open?id=16AcLcgRRLlM7chKUi4eHgT-NOfBCnArM")
            print("2. Link bald da.")
            print()
            main()
        elif answer.lower() == "test":
            print("yay, Es funktioniert.")
            print()
            main()
        elif answer.lower() == 'help':
            print("Hier sind die komandos:")
            print("Zum verschlüsseln encode schreiben.")
            print("Zum entschlüsseln decode schreiben.")
            print("Zum Update link get.update schreiben.")
            print()
            print("Und es gibt seecrets. ;)")
            print("Wenn du mein script bewwerten willst, schreib mir mit der Maiil adresse:")
            print("volkswagenfelge@gmail.com")
            print()
            main()
        elif answer.lower() == 'email':
            print("Hier: Volkswagenfelge@gmail.com")
            print("Bitte gib ein feedback ab. ;)")
            print()
            main()
        elif answer.lower()=="time":
            ctime()
        elif answer.lower()=="devstop":
            exit()
        elif answer.lower() == "exit":
            bd_day = 16
            bd_month = 3
            now = datetime.datetime.now()
            if now.day == bd_day and now.month == bd_month:
                print("")
                print("Es ist die weihnachtszeit")
                print("und das heißt das datenräuber")
                print("eure daten nicht stehlen")
                print("dürfen. (das verschlüsselt")
                print("nur Text. aber schon so")
                print("das keiner es lesen kann)")
                print("unhd das heißt das alle")
                print("textnachrichten in")
                print("pseudo-hex verschlüsselt")
                print("sind. Ich wünsche allen ein")
                print("Frohes fest. Hohoho. :D")
                time.sleep(10)
                exit()
            else:
                print("")
                print("Vielen dank für die nutzung")
                print("Von dem selbst geschriebenen")
                print("Verschlüssler und entschlüssler.")
                print("Und wenn updates oder was anderes")
                print("los ist, bitte get.update schreiben")
                print("und den link  eingeben. Das")
                print("Projekt ist open source und")
                print("das bearbeiten ist Erlaubt.")
                print("das ist einfach ein projekt")
                print("das einfach nur aus spaß entschtanden.")
                print("Es würde mich sehr freuen wenn ihr")
                print("ein feedback abgibgt, das")
                print("Verbessert dann auch das script.")
                print("Die email adresse ist bei get.email")
                time.sleep(15)
                exit()
        elif answer == "":
            print("Hahaha, Du hast nichts eingegeben. <:(")
            main()
        else:
            print("Du kannst nur encode  oder decode verwenden! und nicht {}!".format(answer))
            print()
            main()
    except TypeError:
        crash()
def ctime():
    print("Die zeit ist: ", datetime.datetime.now(), ".")
    print()
    main()
def crash():
    print()
    print("ups, etwas ist schief gelaufen.")
    print("sende Bitte eine email zu Volkswagenfelge@gmail.com")
    print("Bitte sende die Details:")
    print("Wie ist es Passiert?")
    print("kann man es Reproduzieren?")
    print("Einen großen dank wenn du die details senden würdest.")
    crashed=input("Willst du das programm weiter nutzen? ")
    print()
    if crashed.lower()=="nein":
        exit()
    elif crashed.lower()=="ja":
        print("ok, ich hoffe das es Bald wieder repariert ist.")
        print()
        main()
    else:
        print("Ja oder Nein?")
        print()
        crash()
main()
