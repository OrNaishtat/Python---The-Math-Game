########################################################################################################################################
### NewLight - The Maths Game
### The Maths Game will generate random math questions.
########################################################################################################################################
import random
MIN_NUMBER = 1
MAX_NUMBER = 10
NB_QUESTIONS = 4
nb_points = 0
########################################################################################################################################
def ask_qustion():
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    o = random.randint(0, 1)
    operator_str = "+"
    if o == 1:
        operator_str = "*"
    str_question = input(f"Compute: {a} {operator_str} {b} = ")
    int_answer = int(str_question)
    compute = int(a) + int(b)
    if o == 1:
        compute = int(a) * int(b)
    if int_answer == compute:
        return True
    return False
########################################################################################################################################

for i in range(0, NB_QUESTIONS):
    print(f"Question Number {i+1} out of {NB_QUESTIONS}")
    if ask_qustion():
        print("You are correct!")
        nb_points += 1
    else:
        print("Wrong answer.")    
print(f"You have earned {nb_points} out of {NB_QUESTIONS} points!")
## If user scored 0 points output "You need to work on your maths"
# If user scored 4/4 points output "Excellent!"
# If user scored above avarage output "Good."
# If user scored below avarage output "You can do better!"
if nb_points == NB_QUESTIONS:
    print("Excellent!")
elif nb_points > 0 and nb_points < NB_QUESTIONS:
    avarage = int(NB_QUESTIONS/2)
    if avarage > nb_points:
        print ("You can do better!")
    elif avarage <= nb_points:
        print("Good.")
else:
    print("You need to work on your maths.")

