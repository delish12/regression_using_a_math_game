# regression_using_a_math_game

## LIBS Needed:-
numpy,subprocess,time,pandas,os,datetime,matplotlib,scipy

## Working :-
initially run the 'end_number_generator.py' file and play the game

if no players enrolled then it will ask you to enroll a name
if players are enrolled already then select your name and play the game

the game works like this
the game has 3 modes :
                        1)addition
                        2)squares
                        3)cubes
if you want to play only the addition part of the game then change the type of 
question in 109th line to 1
and if addition and squares then 2
and if all three type of question then 3

## note:- answering addition type questions
we tried some vedic maths
since it is considered if practiced this way the speed for calculating arthematic addition
will get faster

so answer in this fashion
only input the ones place digit from the arthematic addition
egs:- 
    1+1 = 1
    9+1 = 0
    7+7 = 4
    8+8 = 6

## after completing the game:-
scores are entered in the excell sheet with name stats. 
there are some pre entered stats dont mind them those are mine and my frnds stats
the stats are enter as time stamp and average score,the average score is the score
that a person can solve the no.of questions in a second

## how to check the learnng curve:-

there are two other file in the project names liner and polynregre
liner signifing linear regression
and
polynregre signifing polynomial regression
these are machine learning techniques which helps to find the future predictions with past data


run the liner file to check the linear regression for a specific person or no.of persons
the user can select linear regression for multiple players by giving space to selected numbers
eg:- if players are
        1)delish
        2)durga
        3)hema
if the user want to check regression for 1,2,3 then give input as "1 2 3"

then you will get the graphs of the respective users

### polynomial regression
to check the polynomial regression run the 'polynregre.py' file

all are same as linear regression
except additional varial is order
this selects the order of the polynomial regression
generally more the order the more the precision
but too big of a number will cause over precision
recommendation : min 2 max 4