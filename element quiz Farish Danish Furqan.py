import random

def guess():
    """answer the correct element in down below."""
    print("Guess the number!")
    list=("nitrogen","oxygen","hydrogen","aluminium","carbon")
    
    x = random.choice(list)
    guess = None
    
    while x != guess:
        
        guess = str(input("select one of the right elements:"))
         
        if x == guess:
             print("Good Job")
        elif x != guess:
             print("Almost Right, Try again")
        
guess()