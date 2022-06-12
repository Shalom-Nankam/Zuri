import random

def Rock_Paper_Scissors():
    while(1):
        game_choices= ['R', 'P', 'S']
        print('Welcome to the game\n')
        print('Please select an option: R for rock, P for paper, S for scissors')
        
        player_choice= input()
        play = player_choice.upper()
        correct_choice= play in game_choices
        
        cpu_choice= random.choice(game_choices)

        while(1):
            if(correct_choice==False):
                 print("You picked an invalid option, pick again.")
                 break;
            
            elif(cpu_choice=='R'):
                if(play=='S'):
                    print("Computer picked", cpu_choice, ". Computer won!")
                elif(play=='P'):
                    print("Computer picked", cpu_choice, ". You won!")
                elif(play=='R'):
                    print("Computer picked", cpu_choice, "too, it was a draw play again")
                break;
    
            elif(cpu_choice=='S'):
                if(play=='P'):
                    print("Computer picked", cpu_choice, ". Computer won!")
                elif(play=='R'):
                    print("Computer picked", cpu_choice, ". You won!")
                elif(play=='S'):
                    print("Computer picked", cpu_choice, "too, it was a draw play again")
                break;

            elif(cpu_choice=='P'):
                if(play=='R'):
                    print("Computer picked", cpu_choice, ". Computer won!")
                elif(play=='S'):
                    print("Computer picked", cpu_choice, ". You won!")
                elif(play=='R'):
                    print("Computer picked", cpu_choice, "too, it was a draw play again")    
                break;

        
        
    
   
