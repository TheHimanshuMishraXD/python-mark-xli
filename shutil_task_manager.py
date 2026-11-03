# Goal: Ek program banana hai jo user ke commands ke according files aur folders manage kare.
# Requirements
# 1. User se operation input lo.
# 2. User ko ye options dikhao:
#    - 1 → File copy
#    - 2 → Folder copy
#    - 3 → File move
#    - 4 → Folder move
#    - 5 → Folder delete
#    - 6 → File delete
#    - 7 → Exit
# 3. User se source aur destination paths input lo.
# 4. Operation perform karo.
# 5. Successful operation par message print karo.
# Example output
# ===== FILE MANAGER =====

# 1. Copy File
# 2. Copy Folder
# 3. Move File
# 4. Move Folder
# 5. Delete Folder
# 6. Delete File
# 7. Exit

# Enter your choice: 1

# Enter source file: test.py
# Enter destination file: backup.py

# File copied successfully!


# Conditions
# - shutil.copy() use karna hai.
# - shutil.copytree() use karna hai.
# - shutil.move() use karna hai.
# - shutil.rmtree() use karna hai.
# - os.remove() use karna hai.
# - while loop use karna hai.
# - if-elif-else use karna hai.
# - Error handling ke liye try-except use karna hai.

import shutil
import os
# choice = int(input("enter the operation you want to perform: "))

# options = {1:"File.copy", 2:"Folder.copy", 3:"File.move", 4:"Folder.move", 5:"Folder.delete", 6:"File.delete" ,7:"Exit"}

# if choice in options:
#     print(f"you have selected {options[choice]}")

try:
        choice = int(input("enter the operation you want to perform: "))
        options = {1:"File.copy", 2:"Folder.copy", 3:"File.move", 4:"Folder.move", 5:"Folder.delete", 6:"File.delete" ,7:"Exit"}
        if choice in options:
            print(f"you have selected {options[choice]}")
        match choice:
            case 1:
                source = input("enter the source file path: ")
                destination = input("enter the destination the file path : ")
                shutil.copy(source, destination)
                print("file copied successfully brother !!")
            case 2:
                source = input("enter the source file path where the folder is present in ur pc: ")
                destination = input("enter the destination th file path or name where u want to copy the folder: ")
                shutil.copytree(source , destination)
                print("folder is copied succesfully brother !!")
            case 3:
                source = input("enter the source file path where the file is present in ur pc: ")
                destination = input("enter the destination file path where u want to move the file : ")
                shutil.move(source , destination)
                print("file is moved successfully brother !!")
            case 4:
                source = input("enter the source file path where the folder is present in ur pc: ")
                destination = input("enter the destination ehere  u want to move the folder: ")
                shutil.move(source , destination)
                print("folder is moved successfully brother !!:")
            case 5:
                source = input("enter the source of the folder that you want to delete: ")
                shutil.rmtree(source)
                print("folder is deleted successfully brother !!")
            case 6:
                source = input("enter the source of the file that you want to delete: ")
                os.remove(source)
                print("file is deleted successfully brother!!")
            case 7:
                print("bhai tune select kiya exit to chal bye bye !!")
except FileNotFoundError as e:
       print(f"File or folder not found! {e}")

except PermissionError as e:
       print("Permission denied! {e}")

except ValueError as e:
       print(f"Wrong value entered! {e} ")

except Exception as e:
       print(f"Something went wrong: {e}")
