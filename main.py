import pyfiglet
import time
import os
import pyautogui
import matplotlib.pyplot as plt
import random

BRIGHT_GREEN = "\033[1;32m"
RESET = "\033[0m"

def print_banner():
   banner = pyfiglet.figlet_format("Hack-Chat")
   print(BRIGHT_GREEN + banner + RESET)

print_banner()

def clear():
   if os.name == 'nt':
      os.system('cls')
   else:
      os.system('clear')
def main():
    menu1 = """
[ 1 ] IP Tracker (International)
[ 2 ] Phone Number Tracker (International)
[ 3 ] Server OS Hijacking
[ 4 ] MAC Address Cracker (Local Handshaking)
[ 5 ] Bluetooth Decryption (WLAN)
[ 6 ] Social Media Hijacking (Cross-Platform)
[ 7 ] Reverse Engineering (Server, Kernel, Software)
[ 8 ] Social Engineering (Requires proper conduct)
[ 9 ] Vulnerability Scan and Attack (Default: Dictionary Attack {rockyou.txt})
[ 10 ] DNS Server and Domain Hijacking
[ 11 ] DDoS Attack (Default: Intensive Mode)
[ 12 ] Hash Cracking (Offline Bruteforcing [Status: $afe])
[ 13 ] Server Cracking (Online Bruteforcing [Status: Risky])
[ 14 ] Phishing Server Creation (Requires Domain Name)
[ 15 ] Malware Generation (Requires base.cpp)
[ 16 ] Keylogger Inclusion (Localhost and Server)
[ ** ] Bitcoin Hijacking (Contains High Risk)
[ $$ ] Root User (Further Testing Privilages)
[ ## ] Exit
"""
    os.system('cls')
    print_banner()
    print("\n\033[1;33m[ CODE BY @obxcuringdarknexx ]\033[0m\n")
    print(BRIGHT_GREEN + menu1 + RESET)
    ch1 = input("\033[1;33m[+] Select Option : \033[0m").lower()
    if 'bit' in ch1 or ch1 == '**':
        ch2 = input("Are you sure to proceed: [Y/N] ").lower()
        if ch2 == 'y':
            bitcoin()
        elif ch2 == 'n':
            print("Quiting...")
            time.sleep(1)
            os.system('cls')
            print_banner()
            main()
    elif 'root' in ch1 or ch1 == '$$':
        print("\nEntering Kali...")
        time.sleep(1.2)
        print("\n")
        os.system('kali')
    elif 'exit' in ch1 or ch1 == '##':
        print("Exiting Hack-Chat...")
        time.sleep(2.5)
        pyautogui.hotkey('alt', 'f4')

def bitcoin():
    print("Logging into Bitcoin Trading...")
    time.sleep(3)
    print("Waiting for Server Handshake...")
    time.sleep(3)
    print("Logged in. Decrypting tokens...")
    time.sleep(4)
    print("Admin access granted. Wallet cracking [1/3]...")
    time.sleep(2)
    print("Wallet cracking [2/3]...")
    time.sleep(1)
    print("Wallet cracking [3/3]...")
    time.sleep(3)
    print("\nWallet decrypted. Enloading Encryption...")
    time.sleep(2)
    print("\nEncryption Successful. Initializing Token Authtication...")
    time.sleep(1)
    print("Token Authtication code recieved; unpacking...")
    time.sleep(1.5)
    print("Authentication complete. Bitcoin Hijack Initialising...")
    time.sleep(2)
    print("Starting in 3...")
    time.sleep(1)
    print("Starting in 2...")
    time.sleep(1)
    print("Starting in 1...")
    time.sleep(1)
    print("\033[\n1;33mPress Ctrl + C to stop mining and then insert into wallet.\033[0m\n")
    time.sleep(3)

    # Real-time graph plotting
    try:
        token = 1
        bit = 45
        tokens = []
        bitcoins = []

        plt.ion()  # Interactive mode on
        fig, ax = plt.subplots(figsize=(6, 3))  # Smaller figure size (6x3 inches)
        ax.set_title("Bitcoin Mining Progression")
        ax.set_xlabel("Tokens")
        ax.set_ylabel("Bitcoin Value ($)")
        
        while True:
            tokens.append(token)
            bitcoins.append(bit)

            ax.clear()  # Clear previous plot
            ax.plot(tokens, bitcoins, color='green')

            # Keep the axis labels informative but compact
            ax.set_title("BTC Mining Progress", fontsize=10)
            ax.set_xlabel("Token", fontsize=8)
            ax.set_ylabel("BTC Value ($)", fontsize=8)

            # Adjust the ticks to reduce clutter
            ax.tick_params(axis='both', which='major', labelsize=8)

            plt.tight_layout()  # Adjust layout to fit elements
            plt.draw()
            plt.pause(0.001)
            
            print(f"Token Key: {token} Bitcoin Progression: ${bit}")
            token += 1
            
            # Introduce more extreme fluctuations around the average increase of $905.425
            fluctuation = random.uniform(-2000, 4000)  # Larger fluctuation range
            bit += 905.425 + fluctuation
            
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print(f"Mining Stopped. Total Mined: ${bit}")
        ch3 = input("Do you want to exit? [Y/N] ").lower()
        plt.ioff()  # Turn off interactive mode
        plt.show()  # Show the final graph
        if ch3 == 'y':
            main()
        elif ch3 == 'n':
            ch4 = input("Continue? [Y/N] ").lower()
            if ch4 == 'y':
                bitcoin()
            else:
                print("\nExiting...")
                time.sleep(2)
                main()

menu = """
[ 1 ] Password Bruteforce
[ 2 ] Server Vulnerability Scan (Only vulverabilites)
[ 3 ] DDoS Attack
[ 4 ] EvilTwin Attack
[ 5 ] Reverse Engineering Profile
[ 6 ] Social Engineering Profile (All Tools)
[ 7 ] Server Bruteforce (Intensive)
[ 8 ] Phone Number Tracker
[ 9 ] IP Tracker
[ 10 ] Social Media Hijacking
[ ## ] Exit
"""
print(BRIGHT_GREEN + menu + RESET)

ch0 = input("\033[1;33m[+] Select Option : \033[0m").lower()

if ch0 == "hacker_haven":
    print("\nLoading Administrator Privilages...") 
    time.sleep(3) #lol
    print("Loading Admin Tools...")
    time.sleep(2) #lolx2
    print("Loading password dictionaries...")
    time.sleep(6) #lolx3
    print("Loading Kali tools...")
    time.sleep(3) #lolx4
    print("Loading hack-kernel...")
    time.sleep(7) #lolx5
    print("Alocating Memory...")
    time.sleep(2)
    print("Initializing Last Scan...")
    time.sleep(3)
    print("\nStarting Admin Hack-Chat... [Thank you for your patience]")
    time.sleep(4)

    main()
elif "exit" in ch0 or ch0 == "##":
    print("\nExiting HackChat...")
    time.sleep(2)
    pyautogui.hotkey('alt', 'f4')
else:
    print("\n\033[1;33mYou are not an administrator. Your device's IP, DNS, and MAC have been extracted, try and hide.\033[0m")
    time.sleep(4)
    pyautogui.hotkey('alt', 'f4')


main()
