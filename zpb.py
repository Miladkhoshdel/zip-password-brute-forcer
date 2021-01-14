import zipfile
from tqdm import tqdm

def banner():
     print('''\n
 ############################################
 #                                          #
 #                                          #
 #  888888888888  88888888ba   88888888ba   #  
 #           ,88  88      "8b  88      "8b  #  
 #         ,88"   88      ,8P  88      ,8P  # 
 #       ,88"     88aaaaaa8P'  88aaaaaa8P'  # 
 #     ,88"       88""""""'    88""""""8b,  #
 #   ,88"         88           88      `8b  #
 #  88"           88           88      a8P  #
 #  888888888888  88           88888888P"   #
 #                                          #
 #  Zip Password Brute Forcer (Max Speed)   #
 #                                          #
 ############################################
 # Milad Khoshdel                           #
 # Website: https://www.regux.com           #
 # Email: miladkhoshdel@gmail.com           #
 # Telegram: @miladkhoshdel                 #
 ############################################\n
 ''')

banner()
zip_file = input("Please Enter Zip File Path: ")
wordlist = input("Please Enter Wordlist Path: ")

zip_file = zipfile.ZipFile(zip_file)
n_words = len(list(open(wordlist, "rb")))
print("Total passwords to test:", n_words)

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("\n[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Password not found, try other wordlist.")
