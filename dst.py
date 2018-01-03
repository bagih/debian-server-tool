#!/usr/bin/python

import os
import sys
import traceback
import platform

if not os.geteuid() == 0:
 sys.exit("warning : please run it with root permission")

if str(platform.system()) != "Linux":
 sys.exit("warning : you are not using a linux based os!")

def main():
    try:
        print '''
    ____       __    _                _____
   / __ \___  / /_  (_)___ _____     / ___/___  ______   _____  _____
  / / / / _ \/ __ \/ / __ `/ __ \    \__ \/ _ \/ ___/ | / / _ \/ ___/
 \033[1;36m/ /_/ /  __/ /_/ / / /_/ / / / /   ___/ /  __/ /   | |/ /  __/ /
/_____/\___/_.___/_/\__,_/_/ /_/   /____/\___/_/    |___/\___/_/\033[0m


\033[1;31m                              #    #    #    
#####  ####   ####  #          #    #    #   
  #   #    # #    # #           #    #    #  
  #   #    # #    # #            #    #    # 
  #   #    # #    # #           #    #    #  
  #   #    # #    # #          #    #    #   
  #    ####   ####  ######    #    #    #\033[1;m    \033[1;31m v1.0 \033[1;m
                                             

\033[33m---------- DST | author : Artha Bagih -----------------------------
-
- PILIH TOOL YANG INGIN ANDA INSTALL PADA SERVER                  -
- nb : run it with root user permission !
-------------------------------------------------------------------\033[1;m
        '''
        while True:
            print '''
1) Remote Acess				11) Repository Server (apt-mirror)
2) Web Server & LAMPP		        12) Radio Server (icecast2)
3) DNS Server (bind9)		        13) VPN Server (pptpd)
4) FTP Server 				14) VOiP Server (asterisk)
5) NTP Server 				15) KVM (Virtual Server (qemu))
6) Samba Server 			16) update system repository
7) Mail Server (postfix)                17) upgrade system
8) Webmail (squirellmail)
9) DHCP Server
10) Proxy Server

help = bantuan
            '''
            pilih0 = raw_input("\033[1;31mDST> \033[1;m")
            while (pilih0 == "1"):
                print '''
-------------------Remote Server-----------------------
1) openssh-server
2) telnetd

0) all
                '''
                pil = raw_input("\033[33mMana yang ingin anda install?> \033[1;m")
                if (pil == "1"):
                    cmd = os.system("apt-get install openssh-server")
                    cmd1 = os.system("clear")
                elif (pil == "2"):
                    cmd = os.system("apt-get install telnetd")
                    cmd1 = os.system("clear")
                elif (pil == "0"):
                    cmd = os.system("apt-get install openssh-server telnetd")
                    cmd1 = os.system("clear")
                elif (pil == "exit"):
                    sys.exit(0)
                elif (pil == "gohome"):
                    main()
                elif (pil == "help"):
                    print '''
\033[1;31mpilih menu dengan memasukkan nomor kategori aplikasi

gohome 	= kembali ke halaman awal
exit 	= keluar\033[1;m
                                '''
                else :
                    print "\033[1;31mperintah yang dimasukkan salah!\033[1;m"

            while (pilih0 == "2"):
                print '''
-------------Web Server & LAMPP-------------------------
1) apache2
2) php7.0
3) mysql server & mysql client
4) phpmyadmin

0) all
                    '''
                pil = raw_input("\033[33mMana yang ingin anda install?> \033[1;m")
                if (pil == "1"):
                    cmd = os.system("apt-get install apache2")
                    cmd1 = os.system("clear")
                elif (pil == "2"):
                    cmd = os.system("apt-get install php7.0")
                    cmd1 = os.system("clear")
                elif (pil == "3"):
                    cmd = os.system("apt-get install mysql-server mysql-client")
                elif (pil == "4"):
                    cmd = os.system("apt-get install phpmyadmin")
                elif (pil == "0"):
                    cmd = os.system("apt-get install apache2 php7.0 mysql-server mysql-client phpmyadmin")
                    cmd1 = os.system("clear")
                elif (pil == "help"):
                    print '''
\033[1;31mpilih menu dengan memasukkan nomor kategori aplikasi

gohome 	= kembali ke halaman awal
exit 	= keluar\033[1;m
                                '''
                elif (pil == "gohome"):
                    main()
                elif (pil == "exit"):
                    sys.exit(0)
                else :
                    print "\033[1;31mperintah yang dimasukkan salah!\033[1;m"

            while (pilih0 == "4"):
                print '''
---------------FTP Server-----------------------
1) proftpd
2) vsftpd

0) all  
                '''
                pil = raw_input("\033[33mMana yang ingin anda install?> \033[1;m")
                if (pil == "1"):
                    cmd = os.system("apt-get install proftpd")
                    cmd1 = os.system("clear")
                elif (pil == "2"):
                    cmd = os.system("apt-get install vsftpd")
                    cmd1 = os.system("clear")
                elif (pil == "0"):
                    cmd = os.system("apt-get install proftpd vsftpd")
                    cmd1 = os.system("clear")
                elif (pil == "gohome"):
                    main()
                elif (pil == "exit"):
                    sys.exit(0)
                elif (pil == "help"):
                    print '''
\033[1;31mpilih menu dengan memasukkan nomor kategori aplikasi

gohome 	= kembali ke halaman awal
exit 	= keluar\033[1;m
                                '''
                else:
                    print "\033[1;31mperintah yang dimasukkan salah!\033[1;m"

            if (pilih0 == "3"):
                cmd = os.system("apt-get install bind9")
                cmd1 = os.system("clear")
            elif (pilih0 == "5"):
                cmd = os.system("apt-get install ntp ntpdate")
                cmd1 = os.system("clear")
            elif (pilih0 == "6"):
                cmd = os.system("apt-get install samba")
                cmd1 = os.system("clear")
            elif (pilih0 == "7"):
                cmd = os.system("apt-get install postfix courier-imap courier-pop")
                cmd1 = os.system("clear")
            elif (pilih0 == "8"):
                cmd = os.system("apt-get install squirellmail")
                cmd1 = os.system("clear")
            elif (pilih0 == "9"):
                cmd = os.system("apt-get install isc-dhcp-server")
                cmd1 = os.system("clear")
            elif (pilih0 == "10"):
                cmd = os.system("apt-get install squid")
                cmd1 = os.system("clear")
            elif (pilih0 == "11"):
                cmd = os.system("apt-get install apt-mirror")
                cmd1 = os.system("clear")
            elif (pilih0 == "12"):
                cmd = os.system("apt-get install icecast2")
                cmd1 = os.system("clear")
            elif (pilih0 == "13"):
                cmd = os.system("apt-get install pptpd")
                cmd1 = os.system("clear")
            elif (pilih0 == "14"):
                cmd = os.system("apt-get install asterisk")
                cmd1 = os.system("clear")
            elif (pilih0 == "15"):
                cmd = os.system("apt-get install qemu-kvm libvirt-bin virtinst bridge-utils")
                cmd1 = os.system("clear")
            elif (pilih0 == "16"):
                cmd = os.system("apt-get update")
                cmd1 = os.system("clear")
            elif (pilih0 == "17"):
                cmd = os.system("apt-get upgrade")
                cmd1 = os.system("clear")
            elif (pilih0 == "help"):
                print '''
\033[1;31mpilih menu dengan memasukkan nomor kategori aplikasi

gohome 	= kembali ke halaman awal
exit 	= keluar\033[1;m
                '''
            elif (pilih0 == "exit"):
                sys.exit(0)
            else :
                print "\033[1;31mperintah yang dimasukkan salah!\033[1;m"



    except KeyboardInterrupt:
        print "goodbye...."
    except Exception:
        traceback.print_exc(file=sys.stdout)
        sys.exit(0)

if __name__ == "__main__":
    main()
