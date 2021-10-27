def main():
    return

def calc():
    content = open("lang.txt", "r")
    f = content.read()
    content.close()
    try:
        if f == "en":
            print(f"\nA File for a custom Calculator\n")
            return

        if f == "de":
            print(f"\nEine Datei für einen custom Rechner\n")
            return

        else:
            print("lang.txt File Probably corrupted!")
            return

    except FileNotFoundError:
        print("Error 404")
        return
main()
