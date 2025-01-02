#Rock Paper Scissor

import random

print("Rock Paper Scissor Game")

while True:
    n=input("Enter Your Choice: \n a: Rock \n b: Paper \n c: Scissor \n ")
    if n=='a':
        n='rock'
    elif n=='b':
        n='paper'
    elif n=='c':
        n='scissor'
    else:
        print("Invalid!!")
        continue

    # if n not in ['rock','paper','scissor']:
    #     print("Invalid!!")
    #     continue
    com=random.choice(['rock','paper','scissor'])
    print(f"Your Choice: {n}")
    print(f"Computer Choice: {com}")
    if n==com:
        print("It's Tie")
    elif(n=='rock' and com=='scissor') or\
        (n=='scissor' and com=='paper') or\
        (n=='paper' and com=='rock'):
            print("You Wins..")
    else:
        print("You Loose!..")
