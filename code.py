while True: 
        import random
        import re
        print("\n")
        print ("Rock, Paper, Scissors - Shoot!")
        us = input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ")
        if not re.match("[SsRrPp]", us):
            print("plz enter your weapon")
            print("{R}","{P}","{S}")
            continue
            

        print( "You chose: " + us)
        choices = ['R', 'P', 'S']
        mc= random.choice(choices)
        print ("PC chose " + mc)
        if mc == str.upper(us):
                print ("Tie! ")
                continue    
        elif mc == 'S' and us.upper() == 'R':
                    print ("You win!")
        
        elif mc == 'R' and us.upper() == 'P':      
                    print ("You win!")
        
        elif mc == 'P' and us.upper() == 'S':      
                    print ("You win! ")
       
                    

        else:
            print("YOU LOST")
    