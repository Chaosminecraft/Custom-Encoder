import time as t
import datetime
import getpass
import os
import random as ran
import webbrowser as web
import locale as loc

converted="NULL"
lang="NULL"
recon="no"
content="notext"
answer="notext"
halign="notext"
mail="volkswagenfelge@gmail.com"
link="https://drive.google.com/open?id=16AcLcgRRLlM7chKUi4eHgT-NOfBCnArM"
hexlist = { 'a': '01',    'A': '02', 'b': '03',    'B': '04', 'c': '05',    'C': '06', 'd': '07',    'D': '08',
            'e': '09',    'E': '0A', 'f': '0B',    'F': '0C', 'g': '0D',    'G': '0E', 'h': '0F',    'H': '11',
            'i': '12',    'I': '13', 'j': '14',    'J': '15', 'k': '16',    'K': '17', 'l': '18',    'L': '19',
            'm': '1A',    'M': '1B', 'n': '1C',    'N': '1D', 'o': '1E',    'O': '1F', 'p': '20',    'P': '21',
            'q': '22',    'Q': '23', 'r': '24',    'R': '25', 's': '26',    'S': '27', 't': '28',    'T': '29',
            'u': '2A',    'U': '2B', 'v': '2C',    'V': '2D', 'w': '2E',    'W': '2F', 'x': '30',    'X': '31',
            'y': '32',    'Y': '33', 'z': '34',    'Z': '35', '1': '36',    '6': '37', '2': '38',    '7': '39',
            '3': '3A',    '8': '3B', '4': '3C',    '9': '3D', '5': '3E',    '0': '3F', ' ': '40',    '!': '41',
            ':': '42',    '.': '43', ',': '44',    '@': '45', '[': '46',    ']': '47', '-': '48',    '+': '49',
            ')': '4A',    '(': '4B', '=': '4C',    '_': '4D', '&': '4E',    '^': '4F', '%': '50',    '$': '51',
            '£': '52',    '"': '53', "'": '54',    '<': '55', '>': '56',    '|': '57', '\\': '58',   '/': '59',
            '#': '5A',    '~': '5B', '`': '5C',    '*': '5D', '{': '5E',    '}': '5F', '?': '60',    'ö': '61',
            'Ö': '62',    'ü': '63', 'Ü': '64',    'ä': '65', 'Ä': '66',    '°': '67', '§': '68',    'ß': '70'}

binary = { 'a': '00000001',    'A': '00000010', 'b': '00000011',    'B': '00000100', 'c': '00000101',    'C': '00000110', 'd': '00000111',    'D': '00001000',
           'e': '00001001',    'E': '00001010', 'f': '00001011',    'F': '00001100', 'g': '00001101',    'G': '00001110', 'h': '00001111',    'H': '00010000',
           'i': '00010001',    'I': '00010010', 'j': '00010011',    'J': '00010100', 'k': '00010100',    'K': '00010101', 'l': '00010110',    'L': '00010111',
           'm': '00010111',    'M': '00011000', 'n': '00011001',    'N': '00011010', 'o': '00011011',    'O': '00011100', 'p': '00011101',    'P': '00011110',
           'q': '00011111',    'Q': '00100000', 'r': '00100001',    'R': '00100010', 's': '00100011',    'S': '00100100', 't': '00100101',    'T': '00100110',
           'u': '00100111',    'U': '00101000', 'v': '00101001',    'V': '00101010', 'w': '00101011',    'W': '00101100', 'x': '00101101',    'X': '00101110',
           'y': '00101111',    'Y': '00110000', 'z': '00110001',    'Z': '00110010', '1': '00110011',    '6': '00110100', '2': '00110101',    '7': '00110110',
           '3': '00110111',    '8': '00111000', '4': '00111001',    '9': '00111010', '5': '00111011',    '0': '00111100', ' ': '00111101',    '!': '00111110',
           ',': '00111111',    '@': '01000000', '[': '01000001',    ']': '01000010', '-': '01000011',    '+': '01000100', ')': '01000101',    '(': '01000110',
           '=': '01000111',    '_': '01001000', '&': '01001001',    '^': '01001010', '%': '01001011',    '$': '01001100', '£': '01001101',    '"': '01001110',
           "'": '01001111',    '<': '01010000', '>': '01010001',    '|': '01010010', '\\':'01010011',    '/': '01010100', '#': '01010101',    '~': '01010110',
           '`': '01010111',    '*': '01011000', '{': '01011001',    '}': '01011010', '?': '01011011',    'ö': '01011100', 'Ö': '01011101',    'ü': '01011110',
           'Ü': '01011111',    'ä': '01100000', 'Ä': '01100001',    '°': '01100010', '§': '01100011',    'ß': '01100101'}

def init():
    while True:
        main()

def main():
    global lang
    while True:
        try:
            content = open("lang.txt", "r")
            f = content.read()
            if f == "de":
                print(f"\nWillkommen zu meinem Selbstgemachten text Converter.")
                print("Um die ''Hilfeseite'' zu bekommen kann man Help schreiben.")
                print("Jetzt gibt es Mehrere wege text zu convertieren.")
                print(f"schreib help um die hilfeseite zu bekommen.\n")
                lang="de"
                content.close()
                main_thread()
                return
            if f == "en":
                print(f"\nHello, and welcome to my Custom Text converter.")
                print("To get the ''helpsite'' you can write help.")
                print(f"There are now multiple ways to Convert text.\n")
                lang="en"
                content.close()
                main_thread()
                return
            else:
                savelang()

        except FileNotFoundError:
            savelang()

def savelang():
    lang2 = loc.getdefaultlocale()[:1]
    deflang = str(lang2)
    if deflang == "('en_EN',)":
        inp=input("What language? ")
        inp.lower()
        with open("lang.txt", "w") as f:
            f.write(inp)
            return
    if deflang == "('de_DE',)":
        inp=input("Was für eine Sprache? ")
        inp.lower()
        with open("lang.txt", "w") as f:
            f.write(inp)
            return
    else:
        print("Linux enviroment detected. Please write en if you're English.")
        print("Linux umgebung erkannt. Bitte schreib de wenn du Deutsch bist.")
        inp=input("de/en ")
        inp.lower()
        with open("lang.txt", "w") as f:
            f.write(inp)
            return

def main_thread():
    global answer
    global lang
    while True:
        try:
            try:
                name = getpass.getuser()
                answer = input("{}@DESKTOP:~$ ".format(name))
                
                if answer.lower()=="phex" or answer.lower()=="pbin" or answer.lower()=="thex":
                    converter()

                elif answer.lower() == "phildev": # Secret ;)
                    if lang == "en":
                        print(f"\n11 09 18 18 1E 44 40 12 54 1A 40 21 0F 12 18 08 09 2C 44 40 01 1C 07 40 12 54 1A 40 24 09 18 09 01 26 12 1C 0D 40 28 0F 09 40 0E 01 1A 09 40 0E 24 01 20 26 0F 1E 28 40 26 1E 1E 1C 43 40 4B 20 18 01 1C 1C 09 07 40 24 09 18 09 01 26 09 40 07 01 28 09 40 38 3F 40 15 2A 1C 12 4A \n\nTip: Use phex to decode the text. ;)\n")
                    if lang == "de":
                        print(f"\n11 01 18 18 1E 44 40 12 05 0F 40 04 12 1C 40 21 0F 12 18 08 09 2C 44 40 2A 1C 07 40 12 05 0F 40 03 12 1C 40 0D 09 24 01 07 09 40 1C 1E 05 0F 40 01 1A 40 01 24 03 09 12 28 09 1C 40 2C 1E 1C 40 07 09 1A 40 27 20 12 09 18 40 0E 24 01 20 26 0F 1E 28 43 40 08 01 26 40 24 09 18 09 01 26 09 40 07 01 28 2A 1A 40 12 26 28 40 38 3F 40 14 2A 1C 12 43\n\nTip: nutz phex zum decodieren. ;)\n")

                elif answer.lower() == "update":
                    if lang == "en":
                        print("Here. ↓")
                        print(f"{link}")
                        print(f"if someone Could help me to put the Project to GitHub please contact me with the email adress: Volkswagenfelge@gmail.com\n")
                    if lang == "de":
                        print("Hier. ↓")
                        print(f"{link}")
                        print(f"wenn yemand mir helfen kann das dieses Projekt auf GitHub zu machen, schreib mich an mit der adresse: {mail}\n")

                elif answer.lower() == "test":
                    os.system('cls')
                    if lang == "en":
                        print(f"\nyay, it worked..\n")
                    if lang == "de":
                        print(f"\nNice, es Funktioniert. :)\n")

                elif answer.lower() == "reset":
                    return

                elif answer.lower()=="my ringtone":
                    web.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

                elif answer.lower() == "errorhandler":
                    errorhandle()

                elif answer.lower()=="clear language":
                    os.remove("lang.txt")
                    if lang == "en":
                        print("Language Resetted.")
                    if lang == "de":
                        print("Sprache Zurückgesetzt.")

                elif answer.lower() == "set language":
                    if lang == "en":
                        print("There is en and de as languages. some may get added later.")
                        inp=input(f"\nWhat Language? ")
                    if lang == "de":
                        print("Da ist aktuell nur die sprachen de und en. es werden eventuell weitere Sprachen hinzugefügt.")
                        inp=input(f"Was für eine Sprache? ")
                    inp.lower()
                    with open("lang.txt", "w") as f:
                        f.write(inp)
                        lang = inp
                        if lang == "en":
                            print("\nHello, and welcome to my Custom Text converter.")
                            print("To get the ''helpsite'' you can write help.")
                            print(f"There are now multiple ways to Convert text.\n")
                        if lang == "de":
                            print("\nWillkommen zu meinem Selbstgemachten text Converter.")
                            print("Um die ''Hilfeseite'' zu bekommen kann man Help schreiben.")
                            print("Jetzt gibt es Mehrere wege text zu convertieren.")
                            print(f"schreib help um die hilfeseite zu bekommen.\n")
                            
                elif answer.lower() == "check language":
                    print(lang)
                
                elif answer.lower() == "close test":
                    close()

                elif answer.lower() == 'help':
                    if lang == "en":
                        print(f"\nHere is the Help site:\n")
                        print("The command phex Brings you to the Pseudo Hex converter.")
                        print("The command pbinary Brings you to the Pseudo Binary converter.")
                        print("The command thex Brings you to the Hex converter.")
                        print("The command Clear Language deletes the file lang.txt")
                        print(f"The command Set Language Creates the lang.txt file and resetting the code to the language {lang}")
                        print("The Command My Ringtone Shows what ringtone the initial programmer has")
                        print("to get the only working link, write update.")
                        print("and there are secrets. ;)")
                        print(f"Binary could get added\n")
                    if lang == "de":
                        print(f"\nHier sind die komandos:\n")
                        print(f"der Command phex Bringt dich zum Pseudo Hex converter.")
                        print(f"der Command pbinary Bringt dich zum Pseudo Binary converter.")
                        print(f"der Command thex Brinigt dich zum Hex converter.")
                        print("der Command Clear Language Löscht die Datei lang.txt")
                        print(f"der Command Set Language Macht die Datei lang.txt und startet das Program neu in {lang}")
                        print(f"Zum Update link update schreiben.")
                        print(f"Und es gibt seecrets. ;)")
                        print(f"Binary wird Evtl. bald hinugefügt. Kontaktier mich bitte")
                        print(f"wenn du willst das Binary hinzugefügt Wird oder neue text caracter hinzugefügt werden.\n")
                        

                elif answer.lower() == 'email':
                    if lang == "en":
                        print(f"\nHere: {mail}")
                        print(f"Please give feedback to me. ;)\n")
                    if lang == "de":
                        print(f"\nHier: {mail}")
                        print(f"Bitte gib ein feedback ab. ;)\n")

                elif answer.lower()=="time":
                    time()

                elif answer.lower()=="halt":
                    print("that person that can see that is a Pro.")
                    t.sleep(0.01)
                    exit()

                elif answer.lower() == "exit":
                    closing()

                elif answer == "":
                    notext()

                else:
                    os.system('cls')
                    wrongtxt()
                
            except KeyboardInterrupt:
                close()

        except ValueError:
            if lang == "en":
                print(f"\nA typing error occured.\n")
            if lang == "de":
                print(f"\nEin Schreibfehler ist aufgetaucht.\n")

def converter():
    #print("testing Started")
    global converted
    global answer
    global halign
    global recon
    if answer.lower()=="phex":
        text=hexlist

    if answer.lower()=="pbin":
        text=binary
        
    if answer.lower()=="thex":
        text="truehex"
    content=answer

    while True:
        try:
            try:
                answer = input("Encode or Decode? ")
                if answer.lower() == 'decode':
                    if text.lower()=="truehex":
                        decode_s=input(">> ")
                        print(f"\n", bytes.fromhex(decode_s), "\n")
                        data=bytes.fromhex(decode_s)
                        converted= decode_s+data
                        print(converted)
                        reconvert()
                        if recon.lower()=="false":
                            return
                        else:
                            placeholder="i'm pickle rick, look at me go."
                    else:
                        decode_s = input(">> ")
                        print(f"\n", ''.join(list(text.keys())[list(text.values()).index(c)] for c in decode_s.split()), "\n")
                        reconvert()
                        if recon.lower()=="false":
                            return
                        else:
                            placeholder="i'm pickle rick, look at me go."

                elif answer.lower() == 'encode':
                    if text.lower()=="truehex":
                        encode_s=input(">> ")
                        print(f"\n{text}:", encode_s.encode("utf-8").hex(), "\n")
                        reconvert()
                        if recon.lower()=="false":
                            return
                        else:
                            placeholder="i'm pickle rick, look at me go."
                    else:
                        encode_s = input(">> ")
                        print(f"\n{content}:", ' '.join(text[c] for c in encode_s), "\n")
                        reconvert()
                        if recon.lower()=="false":
                            return
                        else:
                            placeholder="ich werde eventuell nie gehen oder gesehen werden."

                elif answer.lower() == 'help':
                    halign=content.lower()
                    helpsite()

                elif answer.lower() == "exit":
                    os.system('cls')
                    main()

                elif answer.lower()=="style":
                    print(text)

                elif answer.lower() == "":
                    notext()

                else:
                    wrongtxt()
            except KeyboardInterrupt:
                close()

        except ValueError:
            print("Wut?")

def reconvert():
    global recon
    while True:
        if lang == "en":
            question = input("Reconvert? ")
            if question.lower() == 'yes':
                return

            elif question.lower() == 'no':
                recon="false"
                return

            else:
                print(f"Wut?\n")

        if lang == "de":
            question = input("Wieder Convertieren? ")
            if question.lower() == "ja":
                return
            if question.lower() == "nein":
                recon="false"
                return
            else:
                print(f"\nWas?\n")
def notext():
    num=ran.randint(1, 3)
    if num==1:
        print(f"\n-_-\n")
    if num==2:
        print(f"\nHahaha, you typed nothing. :(\n\ntry it with help.\n")
    if num==3:
        print(f"\nA wild NULL appeared\n")
    return

def wrongtxt():
    if lang == "en":
        num=ran.randint(1, 5)
        if num==1:
            print(f"\nWhat? please use Help. not {answer}.\n")

        if num==2:
            print(f"\nWoops... please write help. not {answer}.\n")

        if num==3:
            print(f"\nNope, {answer} is not here. Use help.\n")

        if num==4:
            print(f"\nNo no no! not {answer}. Please use help\n")

        if num==5:
            print(f"\nWrite help. {answer} is not a Command.\n")
        
        return

    if lang == "de":
        number=ran.randint(1, 5)
        if number == 1:
            print(f"\nWas? das itst kein Command! bitte gib help nicht {answer} ein.\n")

        if number == 2:
            print(f"\noh. Schreib einfach help. nicht {answer}.\n")

        if number == 3:
            print(f"\nNope, {answer} ist nicht hier Drinnen. nutz help.\n")

        if number == 4:
            print(f"\nNein nein nein! nicht {answer}. Bitte nutz help\n")

        if number == 5:
            print(f"\nSchreib help. {answer} ist kein command.\n")
        
        return

def helpsite():
    os.system('cls')
    if halign == "pbin":
        text1="pseudo binary"

    if halign == "phex":
        text1="pseudo hex"

    if halign== "notext":
        if lang == "en":
            print(f"no text supplied inside the code. :(\n")
            return
        if lang == "de":
            print(f"da ist kein text in halign.")
            return

    if lang == "en":
        print(f"Here is the Help site of the converter:\n")
        print(f"encode Converts text zu {text1}.")
        print(f"decode Converts {text1} zu text.")
        print(f"Exit brings you to the Main menu.\n")
        return
    if lang == "de":
        print(f"Hier sind ein paar commands:\n")
        print(f"encode Convertiert text zu {text1}.")
        print(f"decode Convertiert {text1} zu text.")
        print(f"Exit bringt dich zum hauptmenü.\n")
    else:
        print(f"\nno language supplied. :(\n")
        return

def time():
    try:
        if lang == "en":
            now=datetime.datetime.now()
            print(f"\nThe time is: ", now.strftime("%m/%d/%Y, %H:%M:%S"), "\n")
            return
        if lang == "de":
            now=datetime.datetime.now()
            print(f"\nDie zeit ist: ", now.strftime("%d/%m/%Y, %H:%M:%S"), "\n")
            return

    except:
        print(f"we destroyed the time. :(\n")
        main()

def close():
    while True:
        if lang == "en":
            print(f"Do you want to close the Program?\n")
            leave=input("Yes or No? ")
            print()
            if leave.lower() == "yes":
                closing()

            elif leave.lower() == "no":
                return
            else:
                print(f"What? please write Yes or No, not {leave}.\n")
        if lang == "de":
            while True:
                print(f"willst du das program Schließen?\n")
                leave=input("Ja oder Nein? ")
                print()
                if leave.lower() == "ja":
                    closing()

                elif leave.lower() == "nein":
                    return
                else:
                    print(f"Was? Bitte sag ja oder nein. nicht {leave}.\n")

def closing():
    os.system('cls')
    fun=4
    fun1=1
    now = datetime.datetime.now()

    if now.day == fun1 and  now.month == fun:
        web.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        exit()

    else:
        if lang == "en":
            os.system("cls")
            print(f"\nThanks For using my custom encrypter")
            print("that Project may get support from patreon,")
            print("but that is not promissed to be starting.")
            print("i try to keep the Code up to date and if ")
            print("there are any issues with any particular ")
            print("Linux system, you can ask that i verify or fix")
            print("it. thanks for the Support of the krita Chat")
            print("That made the initial push to get tat going.")
            t.sleep(15)
            exit()
        if lang == "de":
            os.system("cls")
            print(f"\nVielen dank für die nutzung\nvon meinem eigenen text Convertierer.")
            print("ich versuche features hinzuzufügen und versuche den Code zu reparieren")
            print(" es kann sein das ich ein Patreon aufmach um den code einen Kleinen ")
            print("geldsupport zu haben. Es ist aktuell nur ein hobby wo ich habe und aus spaß")
            print("Updates gebe. und danke nochmal an die leute die geholfen haben dieses projekt")
            print("Möglich gemacht.")
            t.sleep(15)
            exit()

init()
