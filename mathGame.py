try:
    
    import myPythonFunctions as m

    userName = input('Please enter your user name or create a new one if this is your first time playing: ')

    userScore = int(m.getUserPoint(userName))

    if userScore == -1:
        newUser = True
        userScore = 0
    else:
        newUser = False

    userChoice = 0

    while userChoice != 'e':
        userScore += m.generateQuestion()
        print("Current Score:  ", userScore)
        userChoice = input('Press Enter to Continue or type e to Exit: ')
        
    m.updateUserPoints(newUser, userName, str(userScore))

except Exception as e:
    print ("An unexpected error occurred.  Program will exit.  Please try again later.")
