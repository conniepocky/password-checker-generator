import re
import random
import string

keyboard = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"], ["a", "s", "d", "f", "g", "h", "j", "k", "l"], ["z", "x", "c", "v", "b", "n", "m"]]

def checkForThreeInARow(string, arr):

    string = string.lower()
    count = 0

    for r in arr:
        row = "".join(r)
        for i,v in enumerate(row):
            if (i+2 >= len(row)):
                break
            if (v + row[i+1] + row[i+2]) in string:
                count -= 5

    return count

def points(passw):

    points = len(passw)

    #add points

    foundAll = 0

    if re.findall("[+A-Z]", passw):
        points += 5
        foundAll += 1

    if re.findall("[+a-z]", passw):
        points += 5
        foundAll += 1

    if re.findall("[+0-9]", passw):
        points  += 5
        foundAll += 1

    if re.findall("[!$%^*&()\-_=+]", passw):
        points += 5
        foundAll += 1

    if foundAll == 4:
        points += 10

    #take points

    if len(re.findall("[a-zA-Z]", passw)) == len(passw):
        points -= 5
    elif len(re.findall("[!$%^*&()\-_=+]", passw)) == len(passw):
        points -= 5
    elif len(re.findall("[0-9]", passw)) == len(passw):
        points -= 5

    points += checkForThreeInARow(passw, keyboard)

    if points >= 20:
        print("Score " + str(points) + ". Strong password.")
    elif points <= 0:
        print("Score " + str(points) + ". Weak password.")
    else:
        print("Score " + str(points) + ". Medium strength password.")

    print("")

def checkPassword():
    passw = ""

    while True:
        print("")
        print("Please enter a password")
        print("Must be between 8-24 characters.")
        print("Allowed characters - A-Z, a-z, 0-9, !, $, %, ^, &, *, (, ), -, _, =, + .")
        print("Spaces are not allowed")
        print("")

        passw = input("")

        if len(passw) > 24 or len(passw) < 8:
            print("Not allowed. Please enter a password between 8 and 24 characters.")
        elif len(re.findall("[A-Za-z0-9!$%^*&()\-_=+]", passw)) == len(passw):
            break
        else:
            print("Please enter a password using the allowed symbols.")

    points(passw)

   

def generatePassword():
    length = random.randint(8, 12)
    passw = []
    symbols = ["!", "$", "%", "*", "+", "=", "-", "_", "^", "(", ")"]

    for i in range(0, length):
        char = random.randint(0,2)

        if char == 0:
            passw.append(random.choice(list(string.ascii_letters)))
        elif char == 1:
            passw.append(str(random.randint(0,9)))
        elif char == 2:
            passw.append(random.choice(symbols))

    passw = "".join(passw)

    print(passw)
    points(passw)
   
while True:
    print("1. Check Password")
    print("2. Generate Password")
    print("3. Quit")

    choice = input("")

    if (choice.isnumeric() != True):
        print("Please pick a number.")
    elif (choice == "1"):
        checkPassword()
    elif (choice == "2"):
        generatePassword()
    elif (choice == "3"):
        print("Goodbye!")

        break
    else:
        print("Please pick a number between 1 and 3.")
