def quraan_player():
                 import os
                 os.system("apt update && apt upgrade")
                 os.system("apt -y install play-audio")
                 os.system("play-audio 'سورة البقرة آخر ايتين.mp3'")
def banner():
          print ("""
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''#
# AUTHOR: ABDALLAH HUSSEIN MAHMOUD (ABDALLAH X1L)       #
# AGE: 15                                               #
# LANGUAGE: ARABIC AND ENGLISH                          #
# FROM: EGYPT                                           #
# PROGRAMING LANGUAGE: PYTHON                           #
# MESSAGE: ALSALAMU ALAIKUM WA RAHMAT ALLAH WA BARAKATO #
# . I HOPE TO STOP KILLING OUR SELVES. I HOPE STOPPING  #
# FIGHT OURSELVER. I HOPE STOP KILLING PALESTINES MEN,  #
# WOMEN, BOYS, GIRLS, OLDER MEN AMD WOMEN AMD CHILDREN. #
# THEY DON'T HAVE ANY WEAPON OR ANY ENERGY OR AND POWER #
# TO FIGHT YOU. MY WORDS IS GOING TO PEOPLE WHO ARE     #
# TALKING ABOUT FREEDOM. I'M TALKING TO PEOPLE WHO SAID #
# THAT THERE IS AN LAW TO PRTECT THEM. I'M TALKING TO   #
# PEOPLE WHO SAID THAT WE ARE A CRAZY AND DIRTY AREA.   #
# TAHNKS FOR READING MY MESSAGE, I HOPE YOU COULD       #
# UNDERSTAND ME. {(ABDALLAH X1L)}                       #
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''#
""")

def os():
      import os
      print ("""
#----------------------------------------------------------#
# 1- KALI LINUX                                            #
# 2- KALI NET HUNTER                                       #
# 3- ARCH LINUX                                            #
# 4- BLACK ARCH LINUX (MUST INSTALL ARCH LINUX)            #
# 5- DEBIAN                                                #
# 6- PARROT OS                                             #
# 7- UBUNTU                                                #
# 8- FEDORA                                                #
# 9- CENTOS                                                #
# 10- OPENSUSE                                             #
# 11- ALPINE                                               #
#----------------------------------------------------------#
""")
      user_input = input("Enter Your Choose: ")
      if user_input == "1":
         os.system("pkg install wget proot -y && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")
         print ("LINUX INSTALLES SUCCESSFULLY")
      elif user_input == "2":
           os.system("pkg install wget proot -y && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Nethunter/nethunter.sh && bash nethunter.sh")
           print ("NET HUNTER INSTALLED SUCCESSFULLY")
      elif user_input == "3":
           os.system("pkg install wget proot tar -y && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Arch/armhf/arch.sh && bash arch.sh")
           print ("ARCH LINUX INSTALLED SUCCESSFULLY")
      elif user_input == "4":
           os.system("pacman-key --init && pacman-key --populate archlinuxarm && pacman -Sy --noconfirm curl && curl -O https://blackarch.org/strap.sh && chmod +x strap.sh && ./strap.sh")
           print ("BLACK ARCH LINUX INSTALLED SUCCESSFULLY")
      elif user_input == "5":
           os.system("pkg install wget proot -y && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh")
           print ("DEBIAN INSTALLED SUCCESSFULLY")
      elif user_input == "6":
           os.system("pkg install wget proot -y && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Parrot/parrot.sh && bash parrot.sh")
           print ("PARROT OS INSTALLED SUCCESSFULLY")
      elif user_input == "7":
           os.system("pkg install wget proot -y && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh")
           print ("UBUNTU INSTALLED SUCCESSFULLY")
      elif user_input == "8":
           os.system("pkg install wget proot tar -y && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Fedora/fedora.sh && bash fedora.sh")
           print ("FEDORA INSTALLED SUCCESSFULLY")
      elif user_input == "9":
           os.system("pkg install wget proot tar -y && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && bash centos.sh")
           print ("CENTOS INSTALLED SUCCESSFULLY")
      elif user_input == "10":
           os.system("pkg install wget proot tar -y && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/armhf/opensuse.sh && bash opensuse.sh")
           print ("OPENSUSE INSTALLED SUCCESSFULLY")
      elif user_input == "11":
           os.system("pkg install wget proot tar -y && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Alpine/alpine.sh && bash alpine.sh")
           print ("ALPINE INSTALLED SUCCESSFULLY")
      else:
          sys.exit()

quraan_player()
banner()
os()