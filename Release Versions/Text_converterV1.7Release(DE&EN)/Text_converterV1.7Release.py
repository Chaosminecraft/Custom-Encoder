import tkinter as tk
import time as t
from datetime import datetime
import getpass
import os
import random as ran
import webbrowser as web
import locale as loc
from timeread import *
from calc import *

startup="FALSE"
confirm="NULL"
converted="NULL"
lang="NULL"
recon="no"
content="notext"
answer="notext"
halign="notext"
mail="chaosminecraftmail@gmail.com"
link="https://drive.google.com/open?id=16AcLcgRRLlM7chKUi4eHgT-NOfBCnArM"
link2="https://github.com/Chaosminecraft/Custom-Encoder"
phex = { 'a': '01',    'A': '02', 'b': '03',    'B': '04', 'c': '05',    'C': '06', 'd': '07',    'D': '08',
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

pbinary = { 'a': '00000001',    'A': '00000010', 'b': '00000011',    'B': '00000100', 'c': '00000101',    'C': '00000110', 'd': '00000111',    'D': '00001000',
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

def init(): #for the reset command. not much.
    while True:
        main()

def main(): #Loading lang.txt and reading it
    global lang
    while True:
        try:
            content = open("lang.txt", "r")
            f = content.read()
            if startup=="FALSE":
                if f == "de":
                    print(f"\nWillkommen zu meinem Selbstgemachten text Converter.")
                    print("Um die ''Hilfeseite'' zu bekommen kann man Help schreiben.")
                    print("Jetzt gibt es Mehrere wege text zu convertieren.")
                    print("schreib help um die hilfeseite zu bekommen.")
                    print("[INFO] Google drive bekommt keine updates im moment")
                    print(f"und ist Endlich bei GitHub verfügbar.\n")
                    lang="de"
                    content.close()
                    main_thread()
                    return
                if f == "en":
                    print(f"\nHello, and welcome to my Custom Text converter.")
                    print("To get the ''helpsite'' you can write help.")
                    print("There are now multiple ways to Convert text.")
                    print("[INFO] The Google drive is not getting updates")
                    print(f"anymore. and finaly the project is now on  github too\n")
                    lang="en"
                    content.close()
                    main_thread()
                    return
                else:
                    savelang()
            else:
                content.close()
                main_thread()

        except FileNotFoundError:
            savelang()

def savelang(): #for detecting the lagnuage (Windows machine expected.)
    lang2 = loc.getdefaultlocale()[:1]
    deflang = str(lang2)
    if startup=="FALSE":
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
            print("Other then Windows enviroment detected. Please write en if you're English.")
            print("Andere umgebung als Windows erkannt. Bitte schreib de wenn du Deutsch bist.")
            inp=input("de/en ")
            inp.lower()
            with open("lang.txt", "w") as f:
                f.write(inp)
                return
    else:
        main_thread()

def main_thread(): #main thread that is running
    global answer
    global lang
    global startup
    startup="ok"
    while True:
        try:
            try:
                try:
                    name = getpass.getuser()
                    answer = input("{}@DESKTOP:~$ ".format(name))
                    if answer.lower()=="phex" or answer.lower()=="pbin" or answer.lower()=="thex" or answer.lower()=="tbin":
                        converter()

                    if answer.lower() == "phildev": # Secret ;)
                        if lang == "en":
                            print(f"\n11 09 18 18 1E 44 40 12 54 1A 40 21 0F 12 18 08 09 2C 44 40 01 1C 07 40 12 54 1A 40 24 09 18 09 01 26 12 1C 0D 40 28 0F 09 40 0E 01 1A 09 40 0E 24 01 20 26 0F 1E 28 40 26 1E 1E 1C 43 40 4B 20 18 01 1C 1C 09 07 40 24 09 18 09 01 26 09 40 07 01 28 09 40 38 3F 40 15 2A 1C 12 4A \n\nTip: Use phex to decode the text. ;)\n")
                        if lang == "de":
                            print(f"\n11 01 18 18 1E 44 40 12 05 0F 40 04 12 1C 40 21 0F 12 18 08 09 2C 44 40 2A 1C 07 40 12 05 0F 40 03 12 1C 40 0D 09 24 01 07 09 40 1C 1E 05 0F 40 01 1A 40 01 24 03 09 12 28 09 1C 40 2C 1E 1C 40 07 09 1A 40 27 20 12 09 18 40 0E 24 01 20 26 0F 1E 28 43 40 08 01 26 40 24 09 18 09 01 26 09 40 07 01 28 2A 1A 40 12 26 28 40 38 3F 40 14 2A 1C 12 43\n\nTip: nutz phex zum decodieren. ;)\n")

                    if answer.lower() == "update":#update link 
                        if lang == "en":
                            print("Here. ↓")
                            print(f"{link}\n")
                            print(f"{link2}\n")
                        if lang == "de":
                            print("Hier. ↓")
                            print(f"{link}\n")
                            print(f"{link2}\n")

                    if answer.lower() == "test": #just for format testing
                        if lang == "en":
                            print(f"\nyay, it worked..\n")
                        if lang == "de":
                            print(f"\nNice, es Funktioniert. :)\n")

                    if answer.lower() == "reset":#for just resetting to startup condition (may or May not work. it is not proven that it works)
                        os.system("cls")
                        return

                    if answer.lower()=="my ringtone":#literally my Ringtone
                        web.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

                    if answer.lower() == "errorhandler":#to test the errorhandler
                        errorhandle()

                    if answer.lower()=="clear language":#to delete the lang.txt file.
                        os.remove("lang.txt")
                        if lang == "en":
                            print("Language Resetted.")
                        if lang == "de":
                            print("Sprache Zurückgesetzt.")

                    if answer.lower() == "set language":#to set a available language
                        if lang == "en":
                            print("There is en and de as languages. some may get added later.")
                            inp=input(f"\nWhat Language? ")
                        if lang == "de":
                            print("Da sind aktuell nur die sprachen de und en. es werden eventuell weitere Sprachen hinzugefügt.")
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
                                
                    if answer.lower() == "check language":#to just say the language currently used.
                        print(lang)
                    
                    if answer.lower() == "close test":#to test the Close question
                        close()

                    if answer.lower() == "clear screen":#to clear the console screen. (not for Emulator)
                        os.system("cls")

                    if answer.lower() == 'help':#just a Boring o'l help command.
                        if lang == "en":
                            print(f"\nHere is the Help site:\n")
                            print("The command phex Brings you to the Pseudo Hex converter.")
                            print("The command pbinary Brings you to the Pseudo Binary converter.")
                            print("The command thex Brings you to the Hex converter.")
                            print("The command tbin Brings you to the Binary Converter")
                            print("The commend calc opens an yet basic Calculator.")
                            print("The command Clear Language deletes the file lang.txt")
                            print(f"The command Set Language Creates the lang.txt file and resetting the code to the language {lang}")
                            print("The Command My Ringtone Shows what ringtone the initial programmer has")
                            print("to get the only working link, write update.")
                            print("and there are secrets. ;)")
                            print(f"Binary could get added\n")
                        if lang == "de":
                            print(f"\nHier sind die komandos:\n")
                            print("Der command phex Bringt dich zum Pseudo Hex converter.")
                            print("Der command pbinary Bringt dich zum Pseudo Binary converter.")
                            print("Der command thex Bringt dich zum Hex converter.")
                            print("Der command tbin Bringt dich zum Binary converter")
                            print("Der command calc öffnet einen einfachen Rechner.")
                            print("Der Command Clear Language Löscht die Datei lang.txt")
                            print(f"Der Command Set Language Macht die Datei lang.txt und startet das Program neu in {lang}")
                            print("Zum Update link update schreiben.")
                            print(f"Und es gibt secrets. ;)\n")
                            

                    if answer.lower() == 'email':#to get the mail adress to ask for help/adding feature.
                        if lang == "en":
                            print(f"\nHere: {mail}")
                            print(f"Please give feedback to me. ;)\n")
                        if lang == "de":
                            print(f"\nHier: {mail}")
                            print(f"Bitte gib ein feedback ab. ;)\n")

                    if answer.lower()=="time":#to see the time.
                        timereader()

                    if answer.lower()=="secret":
                        print(f"\nWelp, the Secret isn't done yet. look again in a newer version my boi.")

                    if answer.lower()=="calc":#to have a Custom file that is named like that or have a basic Calculator.
                        try:
                            calc()
                        except FileNotFoundError:
                            calcer()

                    if answer.lower()=="clear last message":#to clear the last converted message.
                        converted="NULL"
                        if lang=="en":
                            print(f"\nDone\n")
                        if lang=="de":
                            print(f"\nFertig\n")

                    if answer.lower()=="last message":#to see the last converted message.
                        if converted=="NULL":
                            if lang=="en":
                                print("No message last converted.")
                            if lang=="de":
                                print("Kein text wurde zuletzt convertiert.")
                        else:
                            print(converted)

                    if answer.lower()=="halt":#Developer way to close that madness
                        print("that person that can see that is a Pro.")
                        t.sleep(0.05)
                        exit()

                    if answer.lower() == "exit":#to close that in a Normal manner
                        closing()

                    if answer == "":#Yay, that is just in case nothing is written in there.
                        notext()

                except FileNotFoundError:#if the File is not found with an check if an external function failed.
                    if lang=="en":
                        print("I'm sorry Dave, I'm afraid I can't do that")
                        return
                    if lang=="de":
                        print("Die datei ist schon tot. du kannst sie nicht nochmal töten.")
                        return
                    else:
                        print("woops")
                
            except KeyboardInterrupt:#if STRG and C are pressed togoether it asks to close it.
                close()

        except ValueError:
            if confirm=="false":
                if lang == "en":
                    print(f"\nA typing error occured.\n")
                if lang == "de":
                    print(f"\nEin Schreibfehler ist aufgetaucht.\n")
            else:
                placeholder="Hello, world!" #needed line to somehow not go in to an error

def converter():#the Main usage that is expected of that code, because why wouldn't it be the Second longest function?
    global converted
    global answer
    global halign
    global recon
    global startup
    startup="ok"
    if answer.lower()=="phex":
        text=phex

    if answer.lower()=="pbin":
        text=pbinary
        
    if answer.lower()=="thex":
        text="truehex"

    if answer.lower()=="tbin":
        text="truebinary"
    content=answer

    while True:
        try:
            try:
                if lang == "en":
                    answer = input("Encode or Decode? ")
                if lang == "de":
                    answer = input("Enoder oder Decode? ")
                if answer.lower() == 'decode':
                    if text=="truehex":
                        decode_s=input(">> ")
                        print(f"\n", bytes.fromhex(decode_s), "\n")
                        data=bytes.fromhex(decode_s)
                        converted = decode_s, data

                    if text=="truebinary":
                        a_binary_string = input(">> ")
                        binary_values = a_binary_string.split()
                        ascii_string = ""
                        for binary_value in binary_values:
                            an_integer = int(binary_value, 2)
                            ascii_character = chr(an_integer)
                            ascii_string += ascii_character
                        print(ascii_string)

                    else:
                        decode_s = input(">> ")
                        print(f"\n", ''.join(list(text.keys())[list(text.values()).index(c)] for c in decode_s.split()), "\n")

                elif answer.lower() == 'encode':
                    if text=="truehex":
                        encode_s=input(">> ")
                        print(f"\n{text}:", encode_s.encode("utf-8").hex(), "\n")
                        data=encode_s.encode("utf-8").hex()
                        converted=encode_s, data

                    if text=="truebinary":
                        a = input(">> ")
                        a_bytes = bytes(a, "ascii")
                        print(" ".join(["{0:b}".format(x) for x in a_bytes]))

                    else:
                        encode_s = input(">> ")
                        print(f"\n{content}:", ' '.join(text[c] for c in encode_s), "\n")
                        c=" "
                        data=c.join(text[c] for c in encode_s)
                        converted=encode_s, data

                elif answer.lower() == 'help':#help site of converter. (converter function help)
                    halign=content.lower()
                    helpsite()

                elif answer.lower() == "exit":#to return to the main console.
                    #os.system('cls')
                    main()

                elif answer.lower()=="clear last message":#to clea the last converted message.
                    converted="NULL"
                    if lang=="en":
                        print(f"\nDone\n")
                    if lang=="de":
                        print(f"\nFertig\n")

                elif answer.lower()=="last message":#to view the last converted message
                    if converted=="NULL":
                        if lang=="en":
                            print("no text last converted.")
                        if lang=="de":
                            print("kein text zuletzt convertiert.")
                    else:
                        print(converted)

                elif answer.lower() == "":#The thing that shows text because you didn't input anything..
                    notext()

                else:
                    wrongtxt()
            except KeyboardInterrupt:
                close()

        except ValueError:
            print("Wut?")

def calcer():
    print(f"\nthe first module for the Text converter.")
    print("a Calculator. There is '+' '-' 'x' '/' there.")
    print(f"write help for help.\n")
    while True:
        op=input("What oparation? ")
        print()
        if op.lower()=="+":
            num1=int(input("Number 1: "))
            num2=int(input("Number 2: "))
            num1+=num2
            print(num1)
        if op.lower()=="-":
            num1=int(input("Number 1: "))
            num2=int(input("Number 2: "))
            num1-=num2
            print(num1)
        if op.lower()=="*" or op.lower()=="x":
            num1=int(input("Number 1: "))
            num2=int(input("Number 2: "))
            num1*=num2
            print(num1)
        if op.lower()=="/" or op.lower()=="÷":
            num1=int(input("Number 1: "))
            num2=int(input("Number 2: "))
            calc=num1/num2
            print(num1)
        if op.lower()=="exit":
            return

def notext():#if no text has been given that is used.
    num=ran.randint(1, 3)
    if lang=="de":
        if num==1:
            print("Ups, Vielleicht etwas mehr text... nicht nur nichts")
        if num==2:
            print("hmmm. etwas ist mit UPS oder du hast nichts eingegeben...")
        if num=="3":
            print("DHL hat keine post gegeben, oder hast du nichts gesendet?")
        return
    if lang=="en":
        if num==1:
            print(f"\n-_-\n")
        if num==2:
            print(f"\nHahaha, you typed nothing. :(\n\ntry it with help.\n")
        if num==3:
            print(f"\nA wild NULL appeared\n")
        return

def wrongtxt():#if there is something written wrong.
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

def helpsite():#the helpsite for the converter.
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
        print("last message gives you the last converted message.")
        print("clear last message clears the last converted message")
        print(f"Exit brings you to the Main menu.\n")
        return
    if lang == "de":
        print(f"Hier sind ein paar commands:\n")
        print(f"encode Convertiert text zu {text1}.")
        print(f"decode Convertiert {text1} zu text.")
        print("last message gibt dir die zuletzt convertierte nachricht")
        print("clear last message löscht die zuletzt convertierte nachricht.")
        print(f"Exit bringt dich zum hauptmenü.\n")
    else:
        print(f"\nno language supplied. :(\n")
        return

def close():#to ask if you wanna close that code/program
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

def closing():#jsut for closing. idfk why i done that that way.
    os.system('cls')
    fun=4
    fun1=1
    now = datetime.now()

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
