###                           Developed by THARUUX                            ###

#       ______________ ___    _____ __________ ____ ___ ____ _______  ___       #
#       \__    ___/   |   \  /  _  \\______   \    |   \    |   \   \/  /       #
#         |    | /    ~    \/  /_\  \|       _/    |   /    |   /\     /        #
#         |    | \    Y    /    |    \    |   \    |  /|    |  / /     \        #
#         |____|  \___|_  /\____|__  /____|_  /______/ |______/ /___/\  \       #
#                       \/         \/       \/                        \_/       #

import os
import time
import subprocess
import platform
from datetime import datetime

import pyqrcode
import png

# Text Styles
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
# Style Reset
RESET = "\033[0m"

# Modules need to be installed
modules = ["pyqrcode", "png"]


def import_modules():
    print(f'{GREEN}   Importing modules... {RESET}')
    missing_modules = []

    for module in modules:
        try:
            __import__(module)
            print(f"✅ {GREEN} Successfully imported {module} {RESET}")
        except ImportError:
            print(f"❌ Failed to import {module}.")
            missing_modules.append(module)
    
    return missing_modules

def install_modules(missing_modules):
    if not missing_modules:
        return
    
    failed_modules = []
    
    for module in missing_modules:
        try:
            subprocess.check_call(["pip", "install", module])
            print(f"✅ {GREEN} Successfully installed {module} {RESET}")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {module}. Please install it manually using: pip install {module}")
            failed_modules.append(module)
    
    return failed_modules

def gen_qr():
    data = input('Enter the data: ')
    try:
        clear()
        url = pyqrcode.create(data)
        print(f'\nGenerating QR for - {data}...')
        time.sleep(2)
        return url
    except Exception as e:
        print(f'{RED}Error! Failed to create QR: {e}{RESET}')

def clear():
    system_type = platform.system()
    
    if system_type == "Windows":
        os.system('cls') 
    else:
        os.system('clear') 

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    

def save_file(data):

    NOW = datetime.now()
    FORMAT = NOW.strftime('%Y%m%d%H%M%S')

    directory = "QR_CODES" 
    create_directory(directory)

    while True:
        try:
            print('\n     1) Save as a png')
            print('     2) Save as a svg')
            selected = int(input('\n Please select an option: '))
            if 0 < selected < 3:
                try:
                    if selected == 1:
                        filename = directory + '/' + FORMAT + '.png'
                        data.png(filename, scale=20)
                    else:
                        filename = directory + '/' + FORMAT + '.svg'
                        data.svg(filename, scale=20)
                    filepath = os.path.abspath(filename)
                    print(f'\n\n{GREEN}{BOLD}✅ Successfully saved file at: {filepath}.{RESET}\n\n')
                    time.sleep(3)
                    break
                except:
                    print(f'{RED} Error! Failed to save file.{RESET}')
            else:
                print(f'\n      {RED}Invalid input, please select a valid option.{RESET}')
                time.sleep(2)
        except ValueError:
            print(f"\n      {RED}Invalid input! Please enter a valid integer.{RESET}")
            time.sleep(2)

def me():
    print(f'\n      {BLUE}{BOLD} QR-GEN{RESET}{ITALIC} by THARUUX{RESET}\n')

def thank():
    while True:
        try:
            clear()
            print(f'\n          Thanks for using {BLUE}{BOLD}QR-GEN{RESET} \n')
            print('\n     1) Create another')
            print('     2) Exit')
            selected = int(input('\n Please select an option: '))
            if 0 < selected < 3:
                try:
                    if selected == 1:
                        main()
                    else:
                        break
                except:
                    print(f'{RED} Error! Failed to save file.{RESET}')
            else:
                print(f'\n      {RED}Invalid input, please select a valid option.{RESET}')
                time.sleep(2)
        except ValueError:
            print(f"\n      {RED}Invalid input! Please enter a valid integer.{RESET}")
            time.sleep(2)
    return

def main():
    missing_modules = import_modules()

    if missing_modules:
        failed_modules = install_modules(missing_modules)
        if failed_modules:
            print(f"\n{BOLD}Modules importing failed! Please install {RED}{failed_modules}{RESET} manually and try again.{RESET}")
        else:
            print("\nRechecking module imports...")
            import_modules()
    clear()
    me()
    data = gen_qr()
    if data:
        clear()
        me()
        save_file(data)
        thank()

main()
