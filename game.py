from word import *
#word ='heely'
#figure out how to import alphabet characters
import os
import subprocess

subprocess.run('clear',shell=True)
from string import ascii_uppercase as ab
if word=='':
    try:
        word = os.environ['word']
    except KeyError:
       # print("Answer not set correctly!, exiting game now")
        raise KeyError("Answer not set correctly!, exiting game now") from KeyError 
print("Welcome to the Aidandle! Make guesses below!")
ls = list(ab)
ld = dict()
gd = dict()
for l in ls:
    ld[l] = 0
    gd[l] = 0
word= word.upper()
wsp = list(word)

for l in wsp:
    ld[l]+=1
#print(ld)
i=0
while True:
    try:
        gs = input('GUESS: ')
    except BaseException:
        #subprocess.run(args="source ./us.sh",shell=True)
        raise BaseException('An error has occurred, exiting game now') from BaseException
    gsp = list(gs.upper())
    out = ''
    if len(gsp) !=len(wsp):
        print('Invalid word length!')
        continue
    for l in ls:
        gd[l] = 0
    wrong = False
    for k in range(len(gsp)):
        try:
            gd[gsp[k]]+=1
        except KeyError:
            print('Invalid character! Not found in ASCII Alphabet')
            wrong=True
            break
    

    if wrong:
        # continues guessing and does not penalize player
        continue
    for j in range(len(gsp)):
        #gd[gsp[j]]+=1
        if gsp[j] == wsp[j]:
            out+="\u001b[32m"+gsp[j]+"\u001b[0m"
        elif gsp[j] in word and gd[gsp[j]]<=ld[gsp[j]] :
            out+="\u001b[33m"+gsp[j]+"\u001b[0m"
        else:
            out+="\u001b[37m"+gsp[j]+"\u001b[0m"
    print(f"Guess {i+1}/6")
    print(out)
    i+=1
    if gs.upper() == word:
        print(f"Congratulations! You have guessed the word in {i} tries!")
        break
    if i >5:
        print('You did not guess the correct word!\nYOU LOSE :(')
        break

    

