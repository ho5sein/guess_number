import random
number = random.randint(1,100)
# get a random number by system
# ==================================================================
try:
    for step in range(1,9):
        guess = int(input(f'step {step} >>>>> please input your guess : '))
        new_difrence = abs(guess - number)
    # ---------------------------------------    
        if guess >100 or guess<1:
            print('out of bounds')
            break
        
        elif new_difrence ==0:
            print( f' WOW you found the number with {step} guesses')
            print('\n your score is : ' , 1000 / step)
            break
        
        elif step ==1:
            if new_difrence < 10:
                print('!WARM')
            elif new_difrence > 9:
                print('!Cold') 
           # difrence = new_difrence
        elif step == 8 and guess != number:
            print(' sorry, you tried 8 times without correct guess\
                  \n and your score is 0')
            
        elif new_difrence < difrence:
            print('Warmer')
           
        elif new_difrence > difrence:
            print('Colder')
           
        else: print('distance is same')
    # ---------------------------------------    
        difrence = new_difrence
except ValueError:
    print('The intiger number had to import')
# ==================================================================
