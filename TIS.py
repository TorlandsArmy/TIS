#-*- coding: utf-8 -*-
import os

def menu():

    print(""" 
▄▄▄█████▓      ██▓       ██████      
▓  ██▒ ▓▒     ▓██▒     ▒██    ▒      
▒ ▓██░ ▒░     ▒██▒     ░ ▓██▄        
░ ▓██▓ ░      ░██░       ▒   ██▒     
  ▒██▒ ░  ██▓ ░██░ ██▓ ▒██████▒▒ ██▓ 
  ▒ ░░    ▒▓▒ ░▓   ▒▓▒ ▒ ▒▓▒ ▒ ░ ▒▓▒ 
    ░     ░▒   ▒ ░ ░▒  ░ ░▒  ░ ░ ░▒  
  ░       ░    ▒ ░ ░   ░  ░  ░   ░   
           ░   ░    ░        ░    ░  
           ░        ░             ░  
           
           			@Torlands.axelVA
           				2018
========================================
TOOLS INSTALER SCRIPT
----
ONLY FOR TERMUX!
----
==========================================
00. Convierte a tu android en una Hacking Machine.
------------------------------------------
1. Instalar Nmap 
2. Instalar Hydra
3. Instalar SQLMap
4. Instalar Metasploit
5. Instalar ngrok
6. Instalar Kali Nethunter
7. Instalar angryFuzzer
8. Instalar Red_Hawk
9. Instalar Weeman
10.Instalar IPGeoLocation
11.Instalar Cupp
12.Instagram Bruteforcer (instahack)
13.Twitter Bruteforcer   (TwitterSniper)
14.Instalar Ubuntu
15.Instalar Fedora
16.Instalar viSQL
17.Instalar Hash-Buster
18.Instalar D-TECT
19.Instalar routersploit
------------------------------------------
99. Exit
==========================================
""")

loop = True

while loop:
    menu()
    what = input("#: ")
    if what == "00":
        print("================================")
        print("This will install: nmap, hydra, sqlmap, metasploit, ngrok, angryFuzzer, red_hawk, weeman, IPGeoLocation, cupp, instahack, TwitterSniper, Hash-Buster, D-TECT, routersploit and viSQL with one click.")
        print("----------------")
        hm = input("[?] Do you want to continue? (y/n): ")
        print("================================")
        if hm == "y":
            print("========================================================")
            print("[+] Please put down you android and go to the toilet...")
            print("Because this will take a long time.")
            print("========================================================")
            os.system("pkg update")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y python2")
            os.system("pkg install -y wget")
            os.sysetm("pkg install -y nmap")
            os.system("plg install -y hydra ")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg install wget")
            os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
            os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
            os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
            os.system("cd /data/data/com.termux/files/home && bundle install")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
            os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
            os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home && pip2 install requests")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y php")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y python2")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
            os.system("cd /data/data/com.termux/files/home && cd weeman")
            os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
            os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
            os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y nano")
            os.system("pip install requests")
            os.system("pip install beautifulsoup4")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pip install mechanicalsoup")
            os.system("pkg install -y nano")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            os.system("clear")
            print("========================================")
            print("[+] Satisfactoriamente instalado 3:)")
            print("[+] Happy Hacking <3")
            print("========================================")
        else:
            rmenu = input("[?] Regresar al Menu? (s/n): ")
            if rmenu == "s":
                menu()
            else:
                break
    if what == "1":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y nmap")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] nmap instalado correctamente :)")
        print("[+] Escribe 'nmap' para Iniciar.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (s/n): ")
        if rmenu == "s":
            menu()
        else:
            break
    elif what == "2":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y hydra")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] hydra instalado correctamente :)")
        print("[+] Escribe 'hydra' Para Iniciar.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (s/n): ")
        if rmenu == "s":
            menu()
        else:
            break
    elif what == "3":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] SQLMap instalado correctamente :)")
        print("[+] Escribe 'python2 sqlmap.py' para iniciar.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (s/n): ")
        if rmenu == "s":
            menu()
        else:
            break
    elif what == "4":
        os.system("pkg install -y wget")
        os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
        os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
        os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
        os.system("cd /data/data/com.termux/files/home && bundle install")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Metasploit instalado correctamente :)")
        print("[+] Escribe 'msfconsole' para iniciar.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (s/n): ")
        if rmenu == "s":
            menu()
        else:
            break
    elif what == "5":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] ngrok instalado correctamente :)")
        print("[+] ve al folder de ngrok  './ngrok http 80' y inicialo.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (s/n): ")
        if rmenu == "s":
            menu()
        else:
            break
    elif what == "6":
        os.system("pkg update -y")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Nethunter-In-Termux.git")
        os.system("cd /data/data/com.termux/files/home && cd Nethunter-In-Termux && chmod +x kalinethunter")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Nethunter instalado correctamente :)")
        print("[+] Ve a la ubicacion Nethunter-In-Termux y escribe './kalinethunter' to start.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (s/n): ")
        if rmenu == "s":
            menu()
        else:
            break
    elif what == "7":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
        os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
        os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home && pip2 install requests")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] angryFuzzer instalado correctamente :)")
        print("[+] ubicate en angryFuzzer y ejecuta 'python2 angryFuzzer.py' to para iniciar.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (s/n): ")
        if rmenu == "s":
            menu()
        else:
            break
    elif what == "8":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y php")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] RED_HAWK instalado correctamente :)")
        print("[+] Ve al folder RED_HAWK y ejecuta 'php rhawk.php' para iniciar.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (s/n): ")
        if rmenu == "s":
            menu()
        else:
            break
    elif what == "9":
        os.system("pkg update -y")
        os.system("pkg install -y python2")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
        os.system("cd /data/data/com.termux/files/home && cd weeman")
        os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] weeman instalado correctamente :)")
        print("[+] ve al folder de weeman y ejecuta 'python2 weeman.py' para iniciar.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (s/n): ")
        if rmenu == "s":
            menu()
        else:
            break
    elif what == "10":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
        os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
        os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] IPGeoLocation instalado correctamente :)")
        print("[+] Ve a el folder de IPGeoLocation y ejecuta 'python ipgeolocation.py' para iniciar.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (y/n): ")
        if rmenu == "s":
            menu()
        else:
            break
    elif what == "11":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
        print("====================================")
        print("[+] Cupp instalado correctamente :)")
        print("[+] ve al folder de cupp folder y ejecuta 'python cupp3.py' para iniciar.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (s/n): ")
        if rmenu == "s":
            menu()
        else:
            break
    elif what == "12":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pkg install -y nano")
        os.system("pip install requests")
        os.system("pip install beautifulsoup4")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
        print("====================================")
        print("[+] Instahack instalado correctamente :)")
        print("[+] vel al folder de instahack y ejecuta 'python hackinsta.py' para iniciar.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (s/n): ")
        if rmenu == "s":
            menu()
        else:
            break
    elif what == "13":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pip install mechanicalsoup")
        os.system("pkg install -y nano")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
        print("====================================")
        print("[+] TwitterSniper instalado correctamente :)")
        print("[+] ve al folder de TwitterSniper y ejecuta 'python TwitterSniper.py' para iniciar.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (s/n): ")
        if rmenu == "s":
            menu()
        else:
            break
    elif what == "14":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Neo-Oli/termux-ubuntu.git")
        os.system("cd /data/data/com.termux/files/home && cd termux-ubuntu && bash ubuntu.sh")
        print("====================================")
        print("[+] Ubuntu instalado correctamente :)")
        print("[+] ve al folder termux-ubuntu y ejecuta './start.sh' para iniciar.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (s/n): ")
        if rmenu == "s":
            menu()
        else:
            break
    elif what == "15":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y wget")
        os.system("apt update && apt install wget -y && /data/data/com.termux/files/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh")
        print("====================================")
        print("[+] Fedora instalado correctamente :)")
        print("[+] ejecuta 'sh termux-fedora.sh f26_arm64' o 'sh termux-fedora.sh f26_arm' para iniciar.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (s/n): ")
        if rmenu == "s":
            menu()
        else:
            break
    elif what == "16":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
        print("====================================")
        print("[+] viSQL instalado correctamente :)")
        print("[+] ve al folder de viSQL y ejecuta 'python2 viSQL.py --help' para iniciar.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (s/n): ")
        if rmenu == "s":
            menu()
        else:
            break
    elif what == "17":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
        print("====================================")
        print("[+] Hash-Buster instalado correctamente :)")
        print("[+] Ve al folder de Hash-Buster y ejecuta 'python2 hash.py' para iniciar.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (s/n): ")
        if rmenu == "s":
            menu()
        else:
            break
    elif what == "18":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
        print("====================================")
        print("[+] D-TECT instalado correctamente :)")
        print("[+] ve al folder Hash-Buster folder y ejecuta 'python2 hash.py' para iniciar.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (s/n): ")
        if rmenu == "s":
            menu()
        else:
            break
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            print("====================================")
            print("[+] routersploit instalado correctamente :)")
            print("[+] Ve al folder de routersploit y ejecuta 'python2 rsf.py' para iniciar.")
            print("====================================")
            rmenu = input("[?] Regresar al Menu? (s/n): ")
            if rmenu == "s":
                menu()
            else:
                break
    elif what == "99":
        print("Bye.")
        break
