import random

line0=[' ',' ',' ']
line1=[' ',' ',' ']
line2=[' ',' ',' ']

#Below is list of all permutation of winning a game.
w=[[5,1,9],[5,3,7],[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9]]


def display():
    print()
    print('    |   | ')
    print('  {0} | {1} | {2}'.format(line0[0], line0[1], line0[2]))
    print('----|---|----')
    print('  {0} | {1} | {2}'.format(line1[0], line1[1], line1[2]))
    print('----|---|----')
    print('  {0} | {1} | {2}'.format(line2[0], line2[1], line2[2]))
    print('    |   |     ')
    print()

def execute(y,x,c):
    y=int(y)-1
    x=int(x)-1
    if y==0:
        line0[int(x)]=c
    elif y==1:
        line1[int(x)]=c
    elif y==2:
        line2[int(x)]=c


#Retuns a bool.
def isvalid(x,y):
    try:
        if eval('line'+str(int(x)-1))[int(y)-1]==' ' and (1<=int(x)<=3) and (1<=int(y)<=3):
            return True
        return False
    except:
        return False


#Convert X's or O's to list
def lines2list(x):
    l=[]
    for i in range(3):
        if line0[i]==x:
            l.append(i+1)
    for i in range(3):
        if line1[i]==x:
            l.append(i+4)
    for i in range(3):
        if line2[i]==x:
            l.append(i+7)
    return l

#Returns bool
def win(x):
    '''
    Input  :c or cr
    Output :boolean
    '''
    l=lines2list(x)

    for i in w:
        if (i[0] in l) and (i[1] in l) and (i[2] in l):
            return True
    return False


#Need to convert in (x,y) format.
def compPlay(c,cr):
    '''
    returns : an integer between 1 and 9.
    '''

    lc=lines2list(c)
    lcr=lines2list(cr)
    l=lc+lcr

    #comp will look for it's own victory in next move.
    for i in w:
        count=0
        t=[]
        for n in i:
            if n in lcr:
                count+=1
            else:
                t.append(n)
        if count>=2 and (t[0] not in l):
            return t[0]
    #If comp can't win in next move then it will check and block the user from winning in next move.
    for i in w:
        count=0
        t=[]
        for n in i:
            if n in lc:
                count+=1
            else:
                t.append(n)
        if count>=2 and (t[0] not in l):
            return t[0]
    #Neither comp or user can win in next move.
    for i in w:
        count=0
        t=[]
        for n in i:
            if n not in lcr:
                continue
            elif n not in lc:
                count+=1
                t.append(n)
            else:
                continue
        if count==2 and  (t[0] not in l):
            return t[0]
    for i in w:
        for n in i:
            if n not in l:
                return n

#Convert compPlay's integer to (x,y) format.
def kanchanPlay(c,cr):
    conversion={1:(1,1),2:(1,2),3:(1,3),4:(2,1),5:(2,2),6:(2,3),7:(3,1),8:(3,2),9:(3,3)}
    return conversion[compPlay(c,cr)]

def play():
    user = input("Enter your name: ")
    first = random.choice([user, 'Kanchan'])# Kanchan --> computer
    print(first, "is going to start game.")
    if first == user:
        play = [user, "Kanchan", user, "Kanchan", user, "Kanchan", user, "Kanchan", user]
    else:
        play = ["Kanchan", user, "Kanchan", user, "Kanchan", user, "Kanchan", user, "Kanchan"]
    while True:
        c = input("Choose X or O: ")
        if c == 'x' or c == 'X':
            c = 'X'
            break
        elif c=='0'or c=='o' or c=='O':
            c = 'O'
            break
        else:
            print()
            print("Invalid command.")

    if c == 'X':
        cr = 'O'
    else:
        cr = 'X'


    for u in play:
        print()
        print(u+"'s turn.")
        if u== user:
            try:
                x,y=map(int,input("Enter Row No. <space> Column No. ---> ").split())
            except:
                x,y=20,20 #Just to make this invalid combination
            while not isvalid(x,y):
                print()
                print("Invalid X and Y.")
                try:
                    x, y = map(int, input("Enter Row No. <space> Column No. ---> ").split())
                except:
                    x,y=20,20
            execute(x,y,c)
        else:
            x,y=kanchanPlay(c,cr)
            execute(x,y,cr)

        display()

        if win(c):
            print(user," has won the game.")
            return None
        elif win(cr):
            print("Kanchan has won the game.")
            return None
    print("DRAW!!")

if __name__=='__main__':
    play()