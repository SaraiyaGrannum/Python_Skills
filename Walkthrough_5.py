def getInput():
    scores = []
    score = int(input("Please enter a bowling score (-1 to exit): "))
    while score != -1:
        while score < 0 or score > 300:
            score = int(input("Please enter a VALID score (0 through 300): "))
        scores.append(score)
        print("Score " + str(scores) + " accepted")
        score = int(input("Please enter a bolwing score (-1 to exit): "))
    return scores

def calculateAverage(scores):
    average = sum(scores) / len(scores)
    return average

def displayResults(scores, average):
    print("You bowled the following scores: ")
    for s in scores:
        print(str(s))
    print("Your bowling average is {: .0f}".format(average))


bowling_scores = getInput()
average = calculateAverage(bowling_scores)
displayResults(bowling_scores, average)
