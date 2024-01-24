import colorama
from colorama import Fore
from colorama import Style
import os
import subprocess


# Es gibt die farben BLACK, RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN und WHITE
# Es gibt die Zusatzparameter DIM, NORMAL und BRIGHT

# ------------------------ DEFINIEREN ANFANG --------------------------------------------

def auswahl():
    print(Fore.RED + "Choose a Program that you want to install (type his name with the right sspelling)" + Style.RESET_ALL)

# def Auswahl():
    # print("Choose an Program that you want to Install or Uninstall:")
    # install = input()

install = "Standard"

def gparted():
    if install == "GParted":
        print("Currently installing this Programm (because im are a good Programm *_* )")
        # Name der .sh-Datei
        sh_file_name = "gparted.sh"
        # Ermittle den Pfad zum Verzeichnis, in dem sich das Python-Programm befindet
        python_script_dir = os.path.dirname(os.path.abspath(__file__))
        # Erstelle den Pfad zum "Games"-Unterordner
        games_dir = os.path.join(python_script_dir, "System_Tools")
        # Erstelle den absoluten Pfad zur .sh-Datei
        sh_file_path = os.path.join(games_dir, sh_file_name)
        # Führe das Skript im Hintergrund aus
        subprocess.Popen(["bash", sh_file_path])

def minetest():
    if install == "Minetest":
        print("Currently installing this Programm (because im are a good Programm *_* )")
        # Name der .sh-Datei
        sh_file_name = "minetest.sh"
        # Ermittle den Pfad zum Verzeichnis, in dem sich das Python-Programm befindet
        python_script_dir = os.path.dirname(os.path.abspath(__file__))
        # Erstelle den Pfad zum "Games"-Unterordner
        games_dir = os.path.join(python_script_dir, "Games")
        # Erstelle den absoluten Pfad zur .sh-Datei
        sh_file_path = os.path.join(games_dir, sh_file_name)
        # Führe das Skript im Hintergrund aus
        subprocess.Popen(["bash", sh_file_path])
    else:
        chromium_bsu()

def chromium_bsu():
    if install == "Chromium BSU":
        print("Currently installing this Programm (because im are a good Programm *_* )")
        # Name der .sh-Datei
        sh_file_name = "chromium-bsu.sh"
        # Ermittle den Pfad zum Verzeichnis, in dem sich das Python-Programm befindet
        python_script_dir = os.path.dirname(os.path.abspath(__file__))
        # Erstelle den Pfad zum "Games"-Unterordner
        games_dir = os.path.join(python_script_dir, "Games")
        # Erstelle den absoluten Pfad zur .sh-Datei
        sh_file_path = os.path.join(games_dir, sh_file_name)
        # Führe das Skript im Hintergrund aus
        subprocess.Popen(["bash", sh_file_path])

def claws_mail():
    if install == "Claws Mail":
        print("Currently installing this Programm (because im are a good Programm *_* )")
        # Name der .sh-Datei
        sh_file_name = "claws-mail.sh"
        # Ermittle den Pfad zum Verzeichnis, in dem sich das Python-Programm befindet
        python_script_dir = os.path.dirname(os.path.abspath(__file__))
        # Erstelle den Pfad zum "Games"-Unterordner
        games_dir = os.path.join(python_script_dir, "Internet")
        # Erstelle den absoluten Pfad zur .sh-Datei
        sh_file_path = os.path.join(games_dir, sh_file_name)
        # Führe das Skript im Hintergrund aus
        subprocess.Popen(["bash", sh_file_path])
    else: 
        firefox()
def List_games():
    print(Fore.CYAN + "Minetest" + Style.RESET_ALL + "      "   "An Open-Source Free Minecraft Clone")
    print(Fore.CYAN + "Chromium BSU" + Style.RESET_ALL + "      "   " Fast-paced open-source spaceship shoot'em-up game")

def List_office():
    print(Fore.CYAN + "Libre Office" + Style.RESET_ALL + "      "   "An Open Source Microsoft Word, Excel and powerpoint clone")

def libreoffice():
    if install == "Libre Office":
        print("Currently installing this Programm (because im are a good Programm *_* )")
        # Name der .sh-Datei
        sh_file_name = "libreoffice.sh"
        # Ermittle den Pfad zum Verzeichnis, in dem sich das Python-Programm befindet
        python_script_dir = os.path.dirname(os.path.abspath(__file__))
        # Erstelle den Pfad zum "Games"-Unterordner
        games_dir = os.path.join(python_script_dir, "Office")
        # Erstelle den absoluten Pfad zur .sh-Datei
        sh_file_path = os.path.join(games_dir, sh_file_name)
        # Führe das Skript im Hintergrund aus
        subprocess.Popen(["bash", sh_file_path])

def Gimp():
    install = input()
    if install == "GIMP":
        print("Currently installing this Programm (because im are a good Programm *_* )")
        # Name der .sh-Datei
        sh_file_name = "gimp.sh"
        # Ermittle den Pfad zum Verzeichnis, in dem sich das Python-Programm befindet
        python_script_dir = os.path.dirname(os.path.abspath(__file__))
        # Erstelle den Pfad zum "Games"-Unterordner
        games_dir = os.path.join(python_script_dir, "Graphic")
        # Erstelle den absoluten Pfad zur .sh-Datei
        sh_file_path = os.path.join(games_dir, sh_file_name)
        # Führe das Skript im Hintergrund aus
        subprocess.Popen(["bash", sh_file_path])

def emacs():
    install = input()
    if install == "Emacs":
        print("Currently installing this Programm (because im are a good Programm *_* )")
        # Name der .sh-Datei
        sh_file_name = "emacs.sh"
        # Ermittle den Pfad zum Verzeichnis, in dem sich das Python-Programm befindet
        python_script_dir = os.path.dirname(os.path.abspath(__file__))
        # Erstelle den Pfad zum "Games"-Unterordner
        games_dir = os.path.join(python_script_dir, "Accessory")
        # Erstelle den absoluten Pfad zur .sh-Datei
        sh_file_path = os.path.join(games_dir, sh_file_name)
        # Führe das Skript im Hintergrund aus
        subprocess.Popen(["bash", sh_file_path])
        
def firefox():
    if install == "Firefox":
        print("Currently installing this Programm (because im are a good Programm *_* )")
        # Name der .sh-Datei
        sh_file_name = "firefox.sh"
        # Ermittle den Pfad zum Verzeichnis, in dem sich das Python-Programm befindet
        python_script_dir = os.path.dirname(os.path.abspath(__file__))
        # Erstelle den Pfad zum "Games"-Unterordner
        games_dir = os.path.join(python_script_dir, "Internet")
        # Erstelle den absoluten Pfad zur .sh-Datei
        sh_file_path = os.path.join(games_dir, sh_file_name)
        # Führe das Skript im Hintergrund aus
        subprocess.Popen(["bash", sh_file_path])
def List_System_Tools():
     print(Fore.CYAN + "GParted" + Style.RESET_ALL + "      "   "An Open Source and CPU economical Memory editor")

def List_Internet():
    print(Fore.CYAN + "Claws Mail" + Style.RESET_ALL + "      "   "An Open Source and CPU economical Mail Client")
    print(Fore.CYAN + "Firefox" + Style.RESET_ALL + "      "   "Browser")

def List_Graphic():
    print(Fore.CYAN + "GIMP" + Style.RESET_ALL + "      "   "An Open Source clone of Adobe Photoshop")

def List_Accessory():
    print(Fore.CYAN + "Emacs" + Style.RESET_ALL + "      "   "An Open Source Terminal + GUI Text Editor")


def Leerstelle():
    print("")


colorama.init()

print(Fore.RED + "Program installer for Raspberry pi" + Style.RESET_ALL)
print(Fore.RED + "Copyright by Finn2431" + Style.RESET_ALL)
print(Fore.RED + 'To See the license of The Icon, type "license"' + Style.RESET_ALL)
print("")
print("Choose an category:")
print(Fore.GREEN + "1) Games" + Style.RESET_ALL)
print(Fore.BLUE + "2) Development" + Style.RESET_ALL)
print(Fore.MAGENTA + "3) Office" + Style.RESET_ALL)
print(Fore.RED + "4) Internet" + Style.RESET_ALL)
print(Fore.BLACK + "5) Graphic" + Style.RESET_ALL)
print(Fore.CYAN + "6) System Tools" + Style.RESET_ALL)
print(Fore.YELLOW + "7) Accessory" + Style.RESET_ALL)
print("8) Theme and Display Design")
print("")
category = input("Coose an category (Say The Number):")
if category == "1":  # Games
    Leerstelle()
    List_games()
    print(Fore.RED + "Choose a Program that you want to install (type his name with the right sspelling)" + Style.RESET_ALL)
    install = input()
    minetest()
    chromium_bsu()     #(Überarbeiten, da nicht funktioniert)
    a = input()

if category == "2":  # Development
    print("No program available for this category")
    a = input()

if category == "3":  # Office
    Leerstelle()
    List_office()
    print(Fore.RED + "Choose a Program that you want to install (type his name with the right sspelling)" + Style.RESET_ALL)
    install = input()
    libreoffice()
    a = input()

if category == "4":  # Internet
    Leerstelle()
    List_Internet()
    print(Fore.RED + "Choose a Program that you want to install (type his name with the right sspelling)" + Style.RESET_ALL)
    install = input()
    claws_mail()
    firefox()
    a = input()


if category == "5":  # Graphic
    List_Graphic()
    print(Fore.RED + "Choose a Program that you want to install (type his name with the right sspelling)" + Style.RESET_ALL)
    Gimp()
    a = input()

if category == "6":  # System Tools
    List_System_Tools()
    print(Fore.RED + "Choose a Program that you want to install (type his name with the right sspelling)" + Style.RESET_ALL)
    gparted()
    a = input()
if category == "7":  # Accessory
    List_Accessory()
    print(Fore.RED + "Choose a Program that you want to install (type his name with the right sspelling)" + Style.RESET_ALL)
    emacs()
    a = input()


if category == "8":  # Theme and Display Design
    print("No program available for this category")
    a = input()

if category == "license":  # License
    print(Fore.MAGENTA + "Berry: https://de.vecteezy.com/vektorkunst/34780111-loganbeere-symbol-isoliert-auf-weiss-hintergrund, 2023/12/25" +    Style.RESET_ALL)
    print(Fore.MAGENTA + "Cardboard Box: https://de.vecteezy.com/vektorkunst/18907204-kartons-seitenansicht-vektor-illustration-business-und-cargo-objekt-icon-konzept-lieferfracht-offene-kisten-vektordesign-mit-schatten-leeres-offenes-und-pappkarton-ikonendesign, 2023/12/25" +    Style.RESET_ALL)
    print(Fore.MAGENTA + "combining the two components to form the logo: Finn Droelle" +    Style.RESET_ALL)
    a = input()
    

