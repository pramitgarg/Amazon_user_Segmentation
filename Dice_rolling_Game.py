# Question need to be asked [ want to roll the dice ?]
#if user said yes then two random number need to be generated and user said no then \
# thank you message need to be sent and if user printed other than invalid message need to be send. 
# user can play as long as he/she wants to so infinite loop needs to be created. 

import random
roll_count = 0 # intialize the counter  
while True:
  choice = input( 'Roll the dice? (Y/N) : ' ).lower()
  if choice == 'y':
     dice1 = random.randint(1,6)
     dice2 = random.randint(1,6)
     print(f'{dice1},{dice2}')
     roll_count += 1
  elif choice == 'n':
     print(f'You rolled the dice {roll_count}')
     print('Thanks for playing! :)')
     break
  else:
   print('Invalid choice!')

# I have made changes to the code in order to count the number of times user has rolled the dice.
# I added the roll_count variable and added the counter within while loop. 

   