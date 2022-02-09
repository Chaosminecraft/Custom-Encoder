import requests
import os

cversion="1.9"

def main():
    return

def update():
    try:
        content = open("lang.txt", "r")
        lang = content.read()
        content.close()
        try:
            url = 'https://www.dropbox.com/s/h9cwtlx43bkbro2/version.txt?dl=1'

            r = requests.get(url, allow_redirects=True)

            open('version.txt', 'wb').write(r.content)
            loadf=open("version.txt", "r")

            version=loadf.read()

            loadf.close()
            
            if version>cversion:
                if lang.lower() == "en":
                    print(f"There is an new version: {version}\n")
                    return

                if lang.lower() == "de":
                    print(f"Da ist eine neue Version: {version}\n")
                    return

                else:
                    print(f"There is an new version: {version}\n")
                    return

            if version==cversion:
                if lang.lower() == "en":
                    print(f"The version is the latest version at the moment.\n")
                    return

                if lang.lower() == "de":
                    print(f"Die version ist die neuste im moment.\n")
                    return
                else:
                    print(f"Hol up: your version is in the Future...  the latest release version is: {version}\n")
                    return
            else:
                return
                
            #os.remove("version.txt") #deactivated to make helping on code probably better...
            return

        except:
            if lang.lower() == "en":
                print(f"updater is unable to Fetch Version list.\n")
                return

            if lang.lower() == "de":
                print(f"Update konnte nicht zum server verbinden.\n")
                return

            else:
                print(f"updater is unable to Fetch Version list.\n")
                return

    except FileNotFoundError:
        if lang.lower() == "en":
            print("Error 404: some file is missing. Please restart the program.")
            return

        if lang.lower() == "de":
            print("Felher 404: eine datei fehlt. Bitte starte das Program neu.")
            return

        else:
            print("Error 404: some file is missing. Please restart the program.")
            return

main()
