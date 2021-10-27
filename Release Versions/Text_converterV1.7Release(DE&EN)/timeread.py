from datetime import datetime
import time

lang="NULL"

def main():
    return

def timereader():
    global lang
    content = open("lang.txt", "r")
    lang = content.read()
    content.close()
    try:
        if lang == "en":
            now=datetime.now()
            print(f"\nThe time is:", now.strftime("%m/%d/%Y, %r"), "\n")
            return
        if lang == "de":
            now=datetime.now()
            print(f"\nDie zeit ist:", now.strftime("%d/%m/%Y, %H:%M:%S"), "\n")
            return
    except KeyboardInterrupt:
        if lang=="en":
            print(f"\nWe Destroyed the time. :(\n")
            return
        if lang=="de":
            print(f"\n Wir haben die Zeit zerstört. :(\n")
            return

main()
