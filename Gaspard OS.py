import os
import time
from colorama import Fore
import json
version = '1.1.0'
os.system('cls')
print("Welcome on :")
print()
time.sleep(2)
os.system('cls')
print('  _______      ___           _______..______      ___      .______      _______         ________  ________  ')
print(' /  _____|    /   \         /       ||   _  \    /   \     |   _  \    |       \       |\   __  \|\   ____\ ')
print('|  |  __     /  ^  \       |   (----`|  |_)  |  /  ^  \    |  |_)  |   |  .--.  |      \ \  \ \  \ \  \___|_ ')
print('|  | |_ |   /  /_\  \       \   \    |   ___/  /  /_\  \   |      /    |  |  |  |       \ \  \ \  \ \_____  \ ')
print("|  |__| |  /  _____  \  .----)   |   |  |     /  _____  \  |  |\  \--. |  '--'  |        \ \  \_\  \|____|\  \  ")
print(" \______| /__/     \__\ |_______/    | _|    /__/     \__\ | _| `.___| |_______/          \ \_______\____\_\  \ ")
print("                                                                                           \|_______|\_________\ ")
print("                                                                                                    \|_________| ")
print()
try:
    with open('donnees.json', 'r', encoding='utf-8') as fichier:
        Users = json.load(fichier)
except FileNotFoundError:
    print('non')
    time.sleep(1)
    Users = {
        "user1":"1234",
        "user2":"AZERTY",
    }
def verifyUsername():
    global userVerified, user
    if user in Users:
        userVerified = True
def verifyPassword():
    global passwordVerified, password
    try:
        if password == Users[user]:
            passwordVerified = True
    except KeyError:
        None
time.sleep(4)
print("version:", version)
print()
connected = False
userVerified = False
passwordVerified = False
while connected == False:
    user = input('login : ')
    print()
    password = input('password : ')
    verifyUsername()
    verifyPassword()
    print()
    if passwordVerified == True and userVerified == True:
        connected = True
        print('ok')
    else:
        print('login incorrect :(')
        print('Try again')
        print()
with open('donnees.json', 'w', encoding='utf8') as fichier:
    json.dump(Users, fichier, ensure_ascii=False)
# https://blog.stephane-robert.info/docs/developper/programmation/python/json/