import ctypes
import os

lang="en"

def main():
    return

def nolang():
    if lang=="en":
        ctypes.windll.user32.MessageBoxW(0, "No language Defined.", "Language Error", 0)
        return
    if lang=="de":
        ctypes.windll.user32.MessageBoxW(0, "Keine sprache Definiert", "Sprachen Fehler", 0)
        return
    else:
        ctypes.windll.user32.MessageBoxW(0, "No language Defined.", "Language Error", 0)
        return

def nofile():
    if lang=="en":
        ctypes.windll.user32.MessageBoxW(0, "Error 404: File Not Found.", "File Not Found", 0)
        return
    if lang=="de":
        ctypes.windll.user32.MessageBoxW(0, "Fehler 404: Datei nicht Gefunden.", "Datei nicht Gefunden", 0)
        return
    else:
        ctypes.windll.user32.MessageBoxW(0, "Error 404: File Not Found.", "File Not Found", 0)
        return

def noname():
    if lang=="en":
        ctypes.windll.user32.MessageBoxW(0, "No name Defined.", "Name Error", 0)
        return
    if lang=="de":
        ctypes.windll.user32.MessageBoxW(0, "Kein name Definiert.", "Namen Fehler", 0)
        return
    else:
        ctypes.windll.user32.MessageBoxW(0, "No name Defined.", "Name Error", 0)
        return

def generalerr():
    if lang=="en":
        ctypes.windll.user32.MessageBoxW(0, "Generic Error", "Generic Error", 1)
        return
    if lang=="de":
        ctypes.windll.user32.MessageBoxW(0, "Generischer Fehler", "Generischer Fehler", 0)
        return
    else:
        ctypes.windll.user32.MessageBoxW(0, "Generic Error", "Generic Error", 1)
        return

main()
