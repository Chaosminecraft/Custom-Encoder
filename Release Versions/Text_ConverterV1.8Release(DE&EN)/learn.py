import webbrowser as web

startup="FALSE"
lang="undefined"

def main():
    return
def get_game(): #Loading lang.txt and reading it
    global lang
    while True:
        try:
            content = open("lang.txt", "r")
            f = content.read()
            if startup=="FALSE":
                if f == "de":
                    lang="de"
                    content.close()
                    ask_shop()
                    return
                if f == "en":
                    lang="en"
                    content.close()
                    ask_shop()
                    return
                else:
                    savelang()
            else:
                content.close()
                savelan()

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
        print("i'm sorry, that Language can't be found. select en (English) or de (German)")
        return

def ask_shop():
    while True:
        if lang.lower()=="de":
            print("Da sind diese Stores:\n1. steam\n2. epic games store\n3. humble\n4. Google Play\n5. Apple Store\n6. Nintendo\n7. Playstation 4\n8. Galaxy Store\n9. gog\n10. Exit geht zurück zum text converter Projekt.")
            ans=input("Von welchem store möchtest du es: ")
            if ans.lower()=="steam" or ans.lower()=="1":
                web.open("https://store.steampowered.com/app/619150/while_True_learn/")
            if ans.lower()=="epic games store" or ans.lower()=="2":
                web.open("https://www.epicgames.com/store/en-US/p/while-true-learn")
            if ans.lower()=="humble" or ans.lower()=="3":
                  web.open("https://www.humblebundle.com/store/while-true-learn")
            if ans.lower()=="google play" or ans.lower()=="4":
                  web.open("https://play.google.com/store/apps/details?id=com.nival.wtlm")
            if ans.lower()=="apple store" or ans.lower()=="5":
                  web.open("https://itunes.apple.com/app/while-true-learn/id1443569124")
            if ans.lower()=="switch store" or ans.lower()=="6":
                  web.open("https://www.nintendo.com/games/detail/while-true-learn-switch/")
            if ans.lower()=="playstation 4" or ans.lower()=="7":
                  web.open("https://store.playstation.com/en-us/product/UP3390-CUSA20449_00-AAAAAAA000000001")
            if ans.lower()=="galaxy store" or ans.lower()=="8":
                  web.open("http://galaxystore.samsung.com/detail/com.nival.wtlm.gs")
            if ans.lower()=="gog" or ans.lower()=="9":
                  web.open("https://www.gog.com/game/while_true_learn")
            if ans.lower()=="exit" or ans.lower()=="10":
                return
            else:
                print(f"sorry, dieser store hat das spiel in der version von diesem Werbung modul. :(\n")
        if lang.lower()=="en":
            print("there are those stores:\n1. steam\n2. epic games store\n3. humble\n4. Google Play\n5. Apple Store\n6. Nintendo\n7. Playstation 4\n8. Galaxy Store\n9. gog\n10. Exit goes to the Text converter Project.")
            ans=input("from what store do you want it: ")
            if ans.lower()=="steam" or ans.lower()=="1":
                web.open("https://store.steampowered.com/app/619150/while_True_learn/")
            if ans.lower()=="epic games store" or ans.lower()=="2":
                web.open("https://www.epicgames.com/store/en-US/p/while-true-learn")
            if ans.lower()=="humble" or ans.lower()=="3":
                  web.open("https://www.humblebundle.com/store/while-true-learn")
            if ans.lower()=="google play" or ans.lower()=="4":
                  web.open("https://play.google.com/store/apps/details?id=com.nival.wtlm")
            if ans.lower()=="apple store" or ans.lower()=="5":
                  web.open("https://itunes.apple.com/app/while-true-learn/id1443569124")
            if ans.lower()=="switch store" or ans.lower()=="6":
                  web.open("https://www.nintendo.com/games/detail/while-true-learn-switch/")
            if ans.lower()=="playstation 4" or ans.lower()=="7":
                  web.open("https://store.playstation.com/en-us/product/UP3390-CUSA20449_00-AAAAAAA000000001")
            if ans.lower()=="galaxy store" or ans.lower()=="8":
                  web.open("http://galaxystore.samsung.com/detail/com.nival.wtlm.gs")
            if ans.lower()=="gog" or ans.lower()=="9":
                  web.open("https://www.gog.com/game/while_true_learn")
            if ans.lower()=="exit" or ans.lower()=="10":
                return
            else:
                print(f"i'm sorry, that shop has in that module version not the game. :(\n")
main()
