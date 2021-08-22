#  © 2021 All Rights Reserved by Tahsin


import sys
from time import sleep
from art import *
# type "pip install art" in Terminal

command = input("Type Congratulations/Happy Birthday {name} to wish\n>>> ")
if 'Congratulations' in command:
    if 'Congratulations' in command:
        command = command.replace('Congratulations', '')
    birthday_text = text2art("\nCongratulations\n" + command, 'roman')
    speed = 0.001
    for char in birthday_text:
        sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()

elif 'Happy Birthday' in command:
    if 'Happy Birthday' in command:
        command = command.replace('Happy Birthday', '')
    birthday_text = text2art("\nHappy   Birthday\n" + command, 'roman')
    speed = 0.001
    for char in birthday_text:
        sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()
else:
    print("Sorry input correct command")

