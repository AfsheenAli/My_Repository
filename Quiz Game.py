#-----------------------------------------------------

def new_game():
    
    guesses = []
    correct_guess = 0
    question_num = 1

    for key in questions:
        print("----------------------------------------------------------------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D) : ").upper()
        guesses.append(guess)

        correct_guess += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guess, guesses)
#-----------------------------------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT !")
        return 1
    else:
        print("WRONG !")
        return 0
#-----------------------------------------------------
def display_score(correct_guesses, guesses):
    print("----------------------------------------------------------------------------------------------")
    print("RESULTS")
    print("-----------------------------------------------------")
    
    print("Answers : " ,end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("Guesses : " ,end="")
    for i in guesses:
        print(i , end="")
    print()

    score = int((correct_guesses/len(questions)) * 100)
    print("Your score is : "+str(score)+"% .")
#----------------------------------------------------
def play_again():
    pass
#-----------------------------------------------------

questions = {
    "1. Who created Python ?" : "A",
    "2. What year was Python created ?" : "B",
    "3. Python is tributed to which comedy group ?" : "D",
    "4. Is the Earth round ?" : "C"
}

options = [["A.Guido Van Rossum", "B.Elon Musk", "C.Bill Gates", "D.Mark Zuckerberg"],
["A.1991", "B.1990", "C.1998", "D.1993"],
["A.Lonely Island", "B.SNL", "C.Smosh", "D.Monty Python"],
["A.Sometimes", "B.No", "C.Yes", "D.What's Earth ?"]]

new_game()
