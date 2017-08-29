# averages scores from 3 quizzes and assigns letter grade
# made an unnecessarily large amount of functions in order to practice chaining arg passing

# function practice to return average score
def averageScore(score1, score2, score3):
    return (score1 + score2 + score3)/3


#get input from
def main():
    quiz1 = float (input ("Enter three quiz scores\n:"))
    quiz2 = float (input (":"))
    quiz3 = float (input (":"))
    # the one confusing line that does all the work:
    outputData(quiz1, quiz2, quiz3, averageScore(quiz1, quiz2, quiz3), getLetterGrade(averageScore(quiz1, quiz2, quiz3)))


# assign letter grade based on average score
def getLetterGrade(average):
    if average >= 96:
        return 'A+'
    elif average >= 93:
        return 'A'
    elif average >= 90:
        return 'A-'
    elif average >= 86:
        return 'B+'
    elif average >= 83:
        return 'B'
    elif average >= 80:
        return 'B-'
    elif average >= 76:
        return 'C+'
    elif average >= 73:
        return 'C'
    elif average >= 70:
        return 'C-'
    elif average >= 66:
        return 'D+'
    elif average >= 63:
        return 'D'
    elif average >= 60:
        return 'D-'
    else:
        return 'F'

def outputData(quiz1, quiz2, quiz3, average, letterGrade):
    print ("\nQuiz Grades:\n{:02.2f}\n{:02.2f}\n{:02.2f}\n\nAverage: {:02.2f}\nFinal Grade: ".format(quiz1, quiz2, quiz3, average), letterGrade)

main()