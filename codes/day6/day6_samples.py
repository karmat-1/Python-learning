# FILE HANDLING : Reading and Writing Text Files
 # r - read w - write a - append r+ - read and write
 
try:
    with open("sample.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File Not Found!")