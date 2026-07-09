#welcome to Big Bang Theory 

import random
loop = 0

while loop == 0 :
 #initial messages
 print ('================================================')
 print ('welcome to Rock ✊, Paper ✋, Scissors ✌️, Lizard 🦎, Spock🖖 ?')
 print ('================================================')
 print (' ')
 print ('Rules and Regulations')
 print (' ')
 print ('Scissors ✌️ cut Paper ✋.')
 print ('Paper ✋ covers Rock ✊.')
 print ('Rock ✊ crushes Lizard 🦎.')
 print ('Lizard 🦎 poisons Spock 🖖.')
 print ('Spock 🖖 smashes Scissors ✌️.')
 print ('Scissors ✌️ beat Lizard 🦎.')
 print ('Lizard 🦎 eats Paper ✋.')
 print ('Paper ✋ disproves Spock 🖖.')
 print ('Spock 🖖 vaporizes Rock ✊.')
 print ('Rock✊ breaks Scissors ✌️.')
 print (' ')
 print ('write the number')



 choice = int(input ('What do you choose (1)Rock (2)Paper (3)Scissors (4)Lizard (5)Spock : '))
 rand = random.randint(1,5)

#game theory
#computer wins commands

 if rand == 3 and choice == 2 :
    print ("computer's choice : Scissors ✌️")
    print ('Your choice : Paper ✋')
    loop += 1
    print ("Result : Computer Wins")
    print ('Reason : Scissors ✌️ cut Paper ✋.')


 elif rand == 2 and choice == 1 :
    print ("computer's choice : Paper ✋")
    print ('Your choice : Rock ✊')
    loop += 1
    print("Result : Computer Wins") 
    print('Reason : Paper ✋ covers Rock ✊.')
 

 elif rand == 1 and choice == 4 :
    print ("computer's choice : Rock ✊")
    print ('Your choice : Lizard 🦎')
    loop += 1
    print("Result : Computer Wins")
    print('Reason : Rock ✊ crushes Lizard 🦎.') 


 elif rand == 4 and choice == 5 :
    print ("computer's choice : Lizard 🦎")
    print ('Your choice : spock 🖖')
    loop += 1
    print("Result : Computer Wins")
    print('Reason : Lizard 🦎 poisons Spock 🖖.')
    

 elif rand == 5 and choice == 3 :
    print ("computer's choice : Spock 🖖")
    print ('Your choice : Scissors ✌️')
    loop += 1
    print("Result : Computer Wins")
    print('Reason : Spock 🖖 smashes Scissors ✌️.')


 elif rand == 3 and choice == 4 :
    print ("computer's choice : Scissors ✌️")
    print ('Your choice : Lizard 🦎')
    loop += 1
    print("Result : Computer Wins") 
    print('Reason : Scissors ✌️ beat Lizard 🦎.') 


 elif rand == 4 and choice == 2 :
    print ("computer's choice : Lizard 🦎")
    print ('Your choice : Paper ✋')
    loop += 1
    print("Result : Computer Wins")
    print('Reason : Lizard 🦎 eats Paper ✋.')  


 elif rand == 2 and choice == 5 :
    print ("computer's choice : Paper ✋")
    print ('Your choice : spock 🖖')
    loop += 1
    print("Result : Computer Wins") 
    print('Reason : Paper ✋ disproves Spock 🖖.') 


 elif rand == 5 and choice == 1 :
    print ("computer's choice : Spock 🖖")
    print ('Your choice : Rock ✊')
    loop += 1
    print("Result : Computer Wins") 
    print('Reason : Spock 🖖 vaporizes Rock ✊.')


 elif rand == 1 and choice == 3 :
    print ("computer's choice : Rock ✊")
    print ('Your choice : Scissors ✌️')
    loop += 1
    print("Result : Computer Wins") 
    print('Reason : Rock ✊ breaks Scissors ✌️.') 

#user wins

 elif choice == 3 and rand == 2 :
    print ("computer's choice : Paper ✋")
    print ('Your choice : Scissors ✌️')
    loop += 1
    print ("Result : User Wins")
    print ('Reason : Scissors ✌️ cut Paper ✋.')


 elif choice == 2 and rand == 1 :
    print ("computer's choice : Rock ✊")
    print ('Your choice : Paper ✋')
    loop += 1
    print("Result : User Wins") 
    print('Reason : Paper ✋ covers Rock ✊.')


 elif choice == 1 and rand == 4 :
    print ("computer's choice : Lizard 🦎")
    print ('Your choice : Rock ✊')
    loop += 1
    print("Result : User Wins")
    print('Reason : Rock ✊ crushes Lizard 🦎.') 


 elif choice == 4 and rand == 5 :
    print ("computer's choice : Spock 🖖")
    print ('Your choice : Lizard 🦎')
    loop += 1
    print("Result : User Wins")
    print('Reason : Lizard 🦎 poisons Spock 🖖.')
    

 elif choice == 5 and rand == 3 :
    print ("computer's choice : Scissors ✌️")
    print ('Your choice : spock 🖖')
    loop += 1
    print("Result : User Wins")
    print('Reason : Spock 🖖 smashes Scissors ✌️.')


 elif choice == 3 and rand == 4 :
    print ("computer's choice : Lizard 🦎") 
    print ('Your choice : Scissors ✌️')
    loop += 1  
    print("Result : User Wins") 
    print('Reason : Scissors ✌️ beat Lizard 🦎.') 


 elif choice == 4 and rand == 2 :
    print ("computer's choice : Paper ✋")
    print ('Your choice : Lizard 🦎')
    loop += 1
    print("Result : User Wins")
    print('Reason : Lizard 🦎 eats Paper ✋.')  


 elif choice == 2 and rand == 5 :
    print ("computer's choice : Spock 🖖")
    print ('Your choice : Paper ✋')
    loop += 1
    print("Result : User Wins") 
    print('Reason : Paper ✋ disproves Spock 🖖.') 


 elif choice == 5 and rand == 1 :
    print ("computer's choice : Rock ✊")
    print ('Your choice : spock 🖖')
    loop += 1
    print("Result : User Wins") 
    print('Reason : Spock 🖖 vaporizes Rock ✊.')


 elif choice == 1 and rand == 3 :
    print ("computer's choice : Scissors ✌️")
    print ('Your choice : Rock ✊')
    loop += 1
    print("Result : User Wins") 
    print('Reason : Rock ✊ breaks Scissors ✌️.') 


 elif choice == rand :
    print ("Result : It's a Tie ")
    print ("User Choice = Computer's Choice")


 else:
    print('Invalid Choice')





    
    
