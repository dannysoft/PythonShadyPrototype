import calcMakerProdCan1 as cm
operatorIndex = -1
numberOfQuestionSets = 1
accuracyLevel = 0
def menu2operands():
    global operatorIndex
    global numberOfQuestionSets
    operatorIndex = -1
    numberOfQuestionSets = 1
    
    menuText = """
    Enter 1 to try another set of 20 random questions.
    Enter 2 to choose operator for set of 20 random questions.
    Enter 3 for multiple sets for export (random operator)
    Enter 4 for multiple sets for export (chosen operator)
    Enter 0 to Quit...
    """ 
    print(menuText)
    calcChoice = input("Please choose 1, 2, 3, 4 [or 0 to quit]: ")
    if calcChoice in ("2","4"):
        strOperator = input("Enter of of the following arithmetic operators...\n'+','-','*','/','%','**','//': ")
        #global operatorIndex 
        operatorIndex =  ("+","-","*","/","%","**","//").index(strOperator)
    #end if
        
    if calcChoice in ("3","4"):
        #global numberOfQuestionSets
        numberOfQuestionSets = int(input("Enter the number of question sets you want for export: "))
    #end if

    return calcChoice
#def end

def Twenty2operandQuestion():
   
    blnEndCalcs = False
    while not blnEndCalcs:
        for setNumber in range(0,numberOfQuestionSets):
            #Get list of twenty answers and twenty non-answers.
            potential40QnAs = cm.Generate40PotentialQnA(operatorIndex)
                
            #Display twenty questions to be answerd
            qnum = 1
            for q in range(0,40, 4):
                strQColLeft = potential40QnAs[q][1]
                strQColRight = potential40QnAs[q+2][1]

                print(" "*19,"{:>3})".format(qnum),"{:<20}".format(strQColLeft)," "*12, "{:>3})".format(qnum+10), "{:<20}".format(strQColRight))
                qnum += 1
            #end for
                
            #Shuff list of forty potential answers.
            cm.rnd.shuffle(potential40QnAs)

            #Display 40 possible answers as a 5 rows by 8 columns grid.    
            strRow = ""
            ansNum = 0
            for q in range (0,40):
                ansNum +=1
                potentialAnswer = potential40QnAs[q][2]
                if type(potentialAnswer) == float:
                    potentialAnswer = str(round(potentialAnswer,2))
                    potentialAnswer = "{:<9}".format(potentialAnswer)
                else:
                    potentialAnswer = "{:<9}".format(potentialAnswer)
                #end if
                    
                strRow = strRow + str(potentialAnswer) + " "
                
                if ansNum % 8 == 0:
                    print(" "*10,strRow)
                    strRow = ""
                #end if
            #end for

            instructions = '''
            Above are 20 calculation for you to attempt.
            The grid above shows 40 possible answers, i.e. 20 are corrct
            20 are wrong.  Your job, calculate and match up your answer
            with an answer from the grid.'''

            print(instructions)
        #end for

        #Show menu to allow user to choose mode of operation.
        blnEndCalcs = (menu2operands() == "0")
    #end while
#def end
            

def menuRounding():
    global accuracyLevel
    global numberOfQuestionSets
    accuracyLevel = 0
    numberOfQuestionSets = 1
    
    menuText = """
    Enter 1 to try another set of 20 random questions.
    Enter 2 to choose level of accuracy (-2 to 3).
    Enter 3 for multiple sets for export (random accuracy)
    Enter 4 for multiple sets for export (chosen accuracy)
    Enter 0 to Quit...
    """
    
    print(menuText)
    roundingChoice = input("Please choose 1, 2, 3, 4 [or 0 to quit]: ")
    if roundingChoice in ("2","4"):
        accuracyLevel = input("Enter level of accuracy (-2 dp to 3 dp   )...\nnegative numbers means significant figure rounding: ")
    #end if
        
    if roundingChoice in ("3","4"):
        #global numberOfQuestionSets
        numberOfQuestionSets = int(input("Enter the number of question sets you want for export: "))
    #end if

    return roundingChoice
#def end

def TwentyFloatsToRound():

    blnEndCalcs = False
    while not blnEndCalcs:
        for setNumber in range(0,numberOfQuestionSets):
            #Get list of twenty answers and twenty non-answers.
            potential40QnAs = cm.RoundToRequiredAccuracy((accuracyLevel == 0),accuracyLevel)
                
            #Display twenty questions to be answerd
            qnum = 1
            for q in range(0,40, 4):
                strQColLeft = potential40QnAs[q][1]
                strQColRight = potential40QnAs[q+2][1]

                print(" "*19,"{:>3})".format(qnum),"{:<10}".format(strQColLeft)," "*23, "{:>3})".format(qnum+10), "{:>10}".format(strQColRight))
                qnum += 1
            #end for
                
            #Shuff list of forty potential answers.
            cm.rnd.shuffle(potential40QnAs)

            #Display 40 possible answers as a 5 rows by 8 columns grid.    
            strRow = ""
            ansNum = 0
            for q in range (0,40):
                ansNum +=1
                potentialAnswer = potential40QnAs[q][2]
                potentialAnswer = str(potentialAnswer)
                if len(potentialAnswer) > 7:
                    potentialAnswer = str(round(float(potentialAnswer),2))[:7]
                #end if
                potentialAnswer = "{:<9}".format(potentialAnswer)   
                strRow = strRow + str(potentialAnswer) + " "
                
                if ansNum % 8 == 0:
                    print(" "*10,strRow)
                    strRow = ""
                #end if
            #end for

            instructions = '''
            Above are 20 roundings for you to attempt.
            The grid above shows 40 possible answers, i.e. 20 are corrct
            20 are wrong.  Your job, round value and match up your answer
            with an answer from the grid.'''

            print(instructions)
        #end for

        #Show menu to allow user to choose mode of operation.
        blnEndCalcs = (menuRounding() == "0")
    #end while
#def end

#Twenty2operandQuestion()

#TwentyFloatsToRound()



