#Simple sanke gun game 
#Coded by Pawan Tiwari
#Snake water gun game
#Using Python 3
#Using mobile phone to create this game 



import random
print('\t\t\t\tGame')
print('\t\t\tDeveloper Pawan Tiwari')
print('\t\tThis game is created for Play purpose')
print("\t\t\tlet'start the game\n")

print('s : for snake🐍 \nw :for water⛲ \ng : for gun🔫')

list = ['s', 'w','g']

chan = 10
n_chan =0
c_p = 0
h_p = 0

while n_chan<chan:
    I = input ('snake, water, gun :')
    rand = random.choice(list)
    
    if I == rand:
        print('\nBoth are same choice\n')
        
      #user input s
    elif I=='s'  and rand == 'g':
         
         c_p = c_p +1
         print(f'\nYour guess {I} and computer guess {rand}\n')
         print('Computer win\n')
         print(f'Computer point{ c_p} and human point {h_p}\n')
    elif I == 's' and rand =='w':
            h_p = h_p +1
            print(f'\nYour guess is {I} and computer guess is {rand}')
            print('Human win\n')
            print(f'Human point {h_p} and computer point {c_p}\n')
            
            
            #user chose water 
            
                 
    elif I == 'w' and rand =='s':
            c_p = c_p +1
            print(f'\nYour guess is {I} and computer guess is {rand}')
            print('Computer win')
            print(f'Human point {h_p} and computer point {c_p}\n')
            
    elif I =='w' and rand =='g':
            h_p = h_p +1
            print(f'\nYour guess is {I} and computer guess is {rand}')
            print('Human win')
            print(f'Human point {h_p} and computet point is {c_p}\n')
     
     #user chose Gun
    elif I== 'g' and rand=='s':
         h_p = h_p +1
         print(f'\nYour guess is {I} and computer Guess is {rand}')
         print('Human Win')
         print(f'Human point {h_p} and Computer Point {c_p}\n')
         
         
         
    elif  I == 'g' and rand =='w':
         c_p = c_p +1
         print(f'\nYour Guess {I} and computer Guess {rand}')
         print('Computer win')
         print(f'Human Points {h_p} and computer Points {c_p}\n')
         
    else:
           print('\nWrong input\n')  
           
           continue
      
    n_chan =n_chan+1
    print(f'\n_{chan}_you have only_{chan-n_chan}_chance left \n ')
    
print("\nGame Over\n")   
      
if c_p >h_p:
    print(f'\nComputer point {c_p}')
    print('Computer win and Human losse\n')
elif c_p <h_p:
    print(f'\nHuman point {h_p}')   
    print('Human win and Computer losse\n')

print(f'\nTotal Score of Computer {c_p}\nTotal Score of Human {h_p}\n')  
