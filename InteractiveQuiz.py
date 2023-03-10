# Interactive Quiz
# Practice Test Question (PSY101)

import timeit
import time
import random
import datetime as dt


class StartQuiz(object):

    def __init__(self, begin):
        self.begin = begin
    
    def play(message):
        print(message)
        print()
        print("\n\tPSYCHOLOGY PRACTICE TEST\n")
        print("Question 1. Who is associated with the Psycoanalytic approach?")
        user_input = input("[ Enter]> ")
        # check if the user's input matches the correct anwer or not
        if user_input.lower() == "Freud".lower() or "Sigmund Freud".lower():
            print("That is Correct!")
            viewResults.percentage(0)
            viewResults.correctAnswers(0)
        else:
            print("Sorry, the correct answer is Freud")
            viewResults.incorrect(0)
            print()

        print("Question 2. A theory explains a specific event.")
        user_input = input(" True or False\n\t")
        # check if the user's input matches the correct anwer or not
        if user_input.lower() == "False".lower():
            print("That is Correct!")
            viewResults.percentage(0)
            viewResults.correctAnswers(0)
        else:
            print("Sorry, the correct answer is False.\n\tTheories do not try to explain only one event,\n\tbut a variety of diverse observations.")
            viewResults.incorrect(0)
            print()
            # a List of question object
            # object store the question Test displayed and,
            # along with the correct answer, multiple Choice options, alternate answers

        quizQuestions = [
            QuestionA("Question 3. ____ examines the role of mental processes on behavior.", "Cognitivism", [], [], []),
            QuestionA("Question 4. ____ seeks to uncover the general principles of learning that explain all behaviors and particularly observable behavior", "Behaviorism",[], [], []),
            QuestionA("Question 5. ____ is the scientific study of the mind", "Psychology",[], [], []),
        ]   

        # For loop to iterate over the quizQuestion List
        for question in quizQuestions:
            print(f"{question.questionText}")
            user_input = input()

            if (user_input.lower() == question.answer.lower()):
                print("That is correct!")
                viewResults.percentage(0)
                viewResults.correctAnswers(0)
            elif (question.alternativeAnswers != None and user_input in question.alternativeAnswers):
                print("That is correct!")
                viewResults.percentage(0)
                viewResults.correctAnswers(0)
            else:
                print(f"Sorry, the correct answer is {question.answer}.")
                viewResults.incorrect(0)

        if (question.multipleChoiceOptions != None):
            print(f"{question.questionText}")

            for option in question.multipleChoiceOptions:
                print(option)
                user_input = input()
        else:
            print(f"{question.questionText}?")


        # MULTIPLE OPTION QUESTIONS
        # a List of question object
        # object store the question Test displayed and,
        # along with the correct answer, multiple Choice options, alternate answers

        quizQuestions2 = [
            QuestionB("Question 6. What is Kelly's humanistic theory based on?",["(a) Heirarchy of needs","(b) Physiological needs","(c) Self-actualization","(d) Fundamental Postulatate"],"d",[],[]),
            QuestionB("Question 7. According to Rotter's social learning theory,how can we have a full understanding of someone's behavior?", ["(a) By observing them in their socoial environment","(b) By considering both the individual and his environment", "(c) By learning their social characteristics","(d) By examining the individual's habits"], "b", [],[]),
            QuestionB("Question 8. Which is an example of aggression?",["(a) Chris intentionally got into a fight with another student at school.","(b) Diane changes her behavior to meet social norms.","(c) Amanda bonds with her newborn daughter.","(d) Bill accidentally trips another student at school and apologizes"], "a", [],[]),
            QuestionB("Question 9. Identify which of the following are valid types of therapy", ["(a) Family", "(b) Relationship", "(c) Group", "(d) All of the above"], "d", [], []),
            QuestionB("Question 10. Jake is a 25-year-old male seeking help to treat his fear of cats.\n\tJake's therapist suggests a therapy that invovles progressive steps,\n\tfrom Jake thinking about a nice cat entering the room\n\tup to Jake eventually allowing a cat to sit on his lap.\n\tChoose the type of individual therapy that correlates to the used by Jake's therapist.",["(a) Exposure therapy", "(b) Dream analysis therapy", "(c) Free association therapy", "(d) Humanistic therapy"], "c",  [], []),
            QuestionB("Question 11. Many psychologists today study behavior through five main lenses:\n\tcognitive, humanistic, social, developmental and _____ ",["(a) clinical","(b) psychodynamic","(c) structural","(d) functional"], "a", [], []),
            QuestionB("Question 12. Dr. Kelly is a psychologist that studies how people learn,\n\t\tsolve problems and make decisions.\n\t\tWhat kind of psychologist is Dr. Kelly", "b",["(a) Clinical","(b) Cognitive.","(c) Social.","(d) None of the answers are correct."], [],[]),
            QuestionB("Question 13. Which of the following is true?",["(a) Personality is inconsistent","(b) Personality is only psychological","(c) Personality is confined by actions and behaviors","(d) Personality is consistent"], "d", [],[])
        ]

        # For loop to iterate over the quizQuestion List & options
        for question in quizQuestions2:
            print(f"{question.questionText}")
            for option in question.multipleChoiceOptions:
                print(option)
                user_input2 = input()
                print(f"{question.alternativeAnswers}")

            if (user_input2.lower() == question.answer.lower()):
                print("That is correct!")
                viewResults.percentage(0)
                viewResults.correctAnswers(0)
            elif (question.alternativeAnswers != None and user_input in question.alternativeAnswers):
                print("That is correct!")
                viewResults.percentage(0)
                viewResults.correctAnswers(0)
            else:
                print(f"Sorry, the correct answer is {question.answer}.")
                viewResults.incorrect(0)
            
        if (question.multipleChoiceOptions != None):
            print(f"{question.questionText}?")

            for option in question.multipleChoiceOptions:
                print(option)
                user_input2 = input()
        else:
            print(f"{question.questionText}?")

            # how many minutes used in finishing 
            # import date and time module
            # 00: 28:57
            print(f"End time: {time_between}\n")

        print("_ " * 24)
        print("\n\tYou have completed the\n\tPsychology 101: Intro to Psychology Practice quiz.\n")
        final_result = viewResults()
        total_answer = viewResults()
        wrong_option = viewResults()

        final_result.percentage()
        total_answer.correctAnswers()
        wrong_option.incorrect()
        print("_ " * 24)

        # feedback of user's performance/View Results
        print("[ VIEW RESULT ]")
        view2 = input("Y    /    N\n") 
        if view2.capitalize() == "Y".capitalize():
            viewResults.percentage(0)
            viewResults.correctAnswers(0)
            viewResults.incorrect(0)
            print()
        else:
            print("THE END")
    

# Adding Multiple Question, Choice option and, 
# question that has Alternative Correct Answers and,
# giving a user HINTS to the Quiz.

# A Question class
class QuestionA(object):
    # Defines the values that Question class can store (Constructor)
    def __init__(self,questionText,answer, multipleChoiceOptions=None, alternativeAnswers=None, hints =None):
        self.questionText = questionText
        self.answer = answer
        self.multipleChoiceOptions = multipleChoiceOptions
        self.alternativeAnswers = alternativeAnswers
        self.hints = hints

    def  __repr__(self):
        return '{'+ self.questionText +', '+ self.answer +',' + str(self.multipleChoiceOptions) + ',' + str(self.alternativeAnswers) + ',' + self.hints + '}'

class QuestionB(object):
    # Defines the values that Question class can store (Constructor)
    def __init__(self,questionText, multipleChoiceOptions,answer, alternativeAnswers=None, hints =None):
        self.questionText = questionText
        self.multipleChoiceOptions = multipleChoiceOptions
        self.answer = answer
        self.alternativeAnswers = alternativeAnswers
        self.hints = hints

    def  __repr__(self):
        return '{'+ self.questionText +', ' + str(self.multipleChoiceOptions) + ',' + self.answer +',' + str(self.alternativeAnswers) + ',' + self.hints + '}'


class viewResults(object):

    # Grade Point
    def percentage(self):
        score = 0
        score += 10
        point = 1
        total_point = score * point
        grade = []
        grade.append(total_point)
        for grade_point in grade:
            if total_point > 50:
                print(grade[-1])
            #print(f"You scored:\n {total_point}%")
            return f"You scored:\n {(grade[-1])}%"

    # Answers correct
    def correctAnswers(self):
        correct = 0
        correct += 1
        if correct >= 4:
            print(f"{correct} questions correct")

    # Questions missed/incorrect
    def incorrect(self):
        missed = 0
        missed += 1
        if missed >= 4:
            print(f"{missed} questions missed")


class replay(object):

    #def __init__(self)

    def tryAgain(self):
        print(decide)
        print("YES   /   NO")
        play_again = input("ENTER: ")

        if play_again.upper() == "YES".upper():
            chances = 2
            if chances >= 1:
                StartQuiz.play(welcome_user)
                # DO SOMETHING ********** 
                
                #**********
                chances -= 1
            elif chances == 0:
                print("Kindly try again in the next 24 hours.")
            else:
                print("ERROR")
        elif play_again.upper() == "NO".upper():
            print("GAME OVER!")
        else:
            print("Invalid option")
            return replay.tryAgain(decide)


# store today's date in a variable named today
today = dt.date.today()
start_time = dt.datetime(2023,3,8)
finish_time = dt.datetime(2023,3,7)
time_between = finish_time - start_time
# store some other date in a veriable called last_of_teens
# Default date display is yyyy-mm-dd
last_of_teens = dt.date(2020,12,31)
todays_date = f"{today:%m/%d/%Y}"
#print(f"{last_of_teens: %A,%B %d,%Y}")
print(todays_date)

# welcome the user to the quiz
welcome_user = """\tHello, welcome to the psychology quiz.\n\tCarefully answer the questions as they are presented."""

StartQuiz.play(welcome_user)
decide = "Would you like to take the quiz again?"
replay.tryAgain(decide)