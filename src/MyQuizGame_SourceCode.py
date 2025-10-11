
# This is a source code for a multi users quiz game written in python code.
# It is a console based code and should be run with any python compatible console or code editor. 
# Any sentence after # (hash tag) is a comment used to describe/ explain the codes 

import random     # This is a python built-in module used to randomise questions. 

data = {}         # This is an empty python dictionary used to hold users score with username as key and score as a value.

def myQuiz(username):           # Whenever it's called this function creates a new quiz for the username, it takes an argument username.
    userCorrectAnswers = 0      # userCorrectAnswers is a variable used to keep a track of users correct answers which will be used to display users score
    myQuestionsInList = list(questions.keys())    # This variable holds list of questions (our question in a list) 

# Now we need to display questions and options for users one after the other.
# Our 10 questions and options are at the bottom in a dictionary and list accordingly. 
# the following code randomise the list of our questions for each user, iterate through the dictionary and display the question separetly. 
  
    for _ in range(10):  
        random.shuffle(myQuestionsInList)   # This shuffle the questions so it does not repeat the questions again and display for user. 
        key = myQuestionsInList.pop()       # remove random question from the list so it does not repeat the questions again for the same user.       print(key)
        print(key)                          # displays questions

# The following code displays the options in questions index.

        questionIndex = list(questions.keys()).index(key)   # this keeps the keys(questions) as a list with index 
        for i in options[questionIndex]:                     
            print(i)                                         

        userAnswersList = []                       # Empty list for user answers.
        userGuess = input("Please enter (A, B, C, or D): ")     # a variable used to hold user answer
        userGuess = userGuess.upper()            # Changes user answer lowercase in to uppercase to prevent error.
        userAnswersList.append(userGuess)        # This adds each answer into the list. 

        userCorrectAnswers += checkAnswer(key, userGuess)  # Pass the question and user's answer and check it using the function then add up the value into usersCorrectanswers variable

    displayScore(username, userCorrectAnswers)              # This calls displayScore function and print users score
    data[username] = userCorrectAnswers                    

def checkAnswer(question, userGuess):          # This is a function defined for checking users answer, it takes parameters question and userguess
    correctAnswer = questions[question]        # A variable used to hold correct answer for a question, we used the key as an index.
    if correctAnswer == userGuess:             # This is a comparison between the correct answer and the user answer. I used boolean compasion sign == 
        print("That's CORRECT!")               # if the value is true it print that's correct and else which is false then print thats incorrect. 
        return 1
    else:
        print("That's INCORRECT! The correct answer is:", correctAnswer)
        if userGuess not in ["A","B","C","D"]:                         # if statment for as a safety check if users answer outside the choices 
            print("please enter your answer either A or,B or,C or,D. you just answered", userGuess)
        return 0
    
# The following function defined to play the quiz again based on user answer.
def playQuizAgain():
    userResponse = input("Is there anyone else wants to play? (y/n): ") # This asks user for relaunching the game again.
    userResponse = userResponse.upper()    # This check user answer, if user answered in lowercase, this changes it into uppercase.
    if userResponse == "Y":                # boolean comparison ==, the vaue is either true or false 
        return True
    else:
        return False

def displayScore(username, userCorrectAnswers):      # This is a function defined to diplay user score.
    score = int((userCorrectAnswers / 10) * 100)     # a variable used to hold and display individual score.
    print("Hey,", username, "you went through all the questions and " + "YOUR SCORE IS!")
    print("You answered correctly:", userCorrectAnswers, "out of 4 questions")
    print("Your score in percentage is: " + str(score) + "%")

# Questions in dictionary easy to access the value which is the correct answers using the keys as an index which is the questions.
questions = {
    "Which one of the following is not a comparison operator? ": "D",
    "Which one of the following word must be used to define a function in Python before the name of the function?: ": "C",
    "Assignments in Python programming language is represented by?: ": "C",
    "One of the following is used in programming language to describe some instructions or codes but not executed by the computers?: ": "A",
    "Which one of the following is not a reserved keyword in Python?: ": "D",
    "Which one of the following commands used by programming language to perform an action or a job do not return any value?: ": "B",
    "Which one of the following does represents a data structure? ": "D",
    "Keys and values in a dictonary data structure are separated by? ": "B",
    "A comparison operator used to compare two values are not equal or the same is? ": "C",
    "The value of boolean expression can be? ": "D"
}

options = [["A. !=", "B. ==", "C. >", "D. ="],
           ["A. defin", "B. my_function", "C. def", "D. function"],
           ["A. ==", "B. >=", "C. =", "D. !="],
           ["A. Comments", "B. Expressions", "C. Variables", "D. Functions"],
           ["A. return", "B. if", "C. break", "D. hello"],
           ["A. Functions", "B. Statements", "C. Expressions", "D. None"],
           ["A. List", "B. Tuple", "C. Dictionary", "D. All"],
           ["A. Comma", "B. Colon", "C. Fullstop", "D. Exclamation mark"],
           ["A. ==", "B. =", "C. !=", "D. =!"],
           ["A. True", "B. False", "C. Anything", "D. A and B"]
           ]

while True:                                          # This is while loop statment with boolean expresson value true, used to repeat the quiz game by calling myQuiz function, before that it checks the validity of username. 
    username = input("Please enter your name: ")     # This is a variable which holds users name.
    def InValidName(username):                       
        return len(username) < 2                     # Define a function to check if username is less than 2 charaters.
    if InValidName(username):                        # An if statment which checks the function defind is true, then will perform the print action 
        print("Please enter a valid name which is a minimum of two characters ")
    else:
        myQuiz(username)                                 # While true it calls myQuiz function which take username as parameter and launche the game again.
        if not playQuizAgain():                          # This is an if statment uses boolean expression value, when it false it terminates the the loop. (if user responded there is no one else wants to play the game = false, print scores and goodbay messages. 
            print("Here are all the scores:")
            sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
            user_scores = dict(sorted_items)
            number_of_user = len(user_scores)
            total_sum = 0

            for user, score in user_scores.items():
                percentage = int((score / 10) * 100)
                total_sum += percentage
                print(f"{user} your score is: {score} out of 10 " + f'({str(percentage)}%)')     # print users score 
            average = total_sum / number_of_user
            print(f'The Average Score between all users is: {str(average)}%')                   # print the aveage score
            print("Thanks for playing and Good bye for now!")
            break                                                                               # Terminate the action outside myQuiz game - close the game 

