import numpy as np
import subprocess as sb
import time
import pandas as pd
import os
from datetime import datetime as dt

def player_name():  #prints all the unique names from the name column
    
    for idx,val in enum:
        print(idx+1,val)
    else:
        idx += 1
        print(idx+1,'new player?')

    choice = int(input('enter number = '))

    if choice <= (idx):             # if existing player
        name = names[choice - 1]
        return name
    else:                           #if new player
        name = input('enter name = ')
        return name


gd = 30           #game duration seconds

print(f'enter \'quit\' to quit \ngame is for {gd} seconds\n')

if os.path.exists('stats.xlsx'):         #if excel sheet exists
    df = pd.read_excel('stats.xlsx')
else:                             # if excel sheet doesnt exists
    column = ['time_stamp','name','avg_score']
    df = pd.DataFrame(columns = column)
    df.to_excel('stats.xlsx',index = False)


names = list(set(df['name']))
names.sort()


enum = enumerate(names)
                         
if names:       # if any name exists select the player
    name = player_name()
else:           # else   enter new player name
    name = input('enter name = ')


#--------------------------------file and player section------------------------
def cls():
    sb.call('cls',shell = True)

def additionpractice(a,b):         # addition function
    c = input(f'{a} + {b} = ')
    if c == 'quit':
        exit()
    try :
        if int(c) != (a + b)%10:
            print('x')
            additionpractice(a,b)
    except ValueError:
        additionpractice(a,b)

def squarepractice(a):              # square function
    c = input(f'{a}^2 =')
    if c=='quit':
        exit()
    try:
        if int(c) != (a**2):
            print('x')
            squarepractice(a)
    except ValueError:
        squarepractice(a)

def cubepractice(a):               # cube function
    c = input(f'{a}^3 =')
    if c == 'quit':
        exit()
    try:
        if int(c) != (a**3):
            print('x')
            cubepractice(a)
    except ValueError:
        cubepractice(a)

def zero(score_count):         #invokes multiplication
    a = np.random.randint(1,10)     #a variable range
    b = np.random.randint(1,10)     #b variable range
    additionpractice(a,b)
    cls()
    return score_count + 1

def one(score_count):          #invokes square
    a = np.random.randint(1,26)       #a variable range
    squarepractice(a)
    cls()
    return score_count + 1

def two(score_count):          #invokes cube
    a = np.random.randint(1,11)      #a variable range
    cubepractice(a)
    cls()
    return score_count + 1

score_count = 0
st = time.time()
while(True):
    typeofquestion = np.random.randint(1) # randomizer for type of operation

    if typeofquestion == 0:
        score_count = zero(score_count)
    elif typeofquestion == 1:
        score_count = one(score_count)
    elif typeofquestion == 2:
        score_count = two(score_count)

    if time.time() - st > gd:      #if end of game time
            now = dt.now()
            score_count -= 1
            break
#--------------------------------game section----------------------------------
    
avg_score = round((score_count)/gd,2)
print(f'Your score is {score_count}')
print(f'Your avg score is {avg_score} per second')

dt1 = now.strftime("%d-%m-%y, %H:%M:%S")
                                     #data frame to excel code
dit = {'time_stamp':[dt1],'name':[name],'avg_score':[avg_score]}
df1 = pd.DataFrame(dit)

df = pd.concat([df,df1])

df.to_excel('stats.xlsx',index = False)

#----------------------------data frame and excel section-----------------------
