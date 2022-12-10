def main():
    # open file
    with open("inputs/2.txt", 'r') as f:
        # score vars for each part
        score1 = 0
        score2 = 0
        # read lines
        for round in f.readlines():
            # calc score for each round, for each part
            score1 += calcScorePart1(round)
            score2 += calcScorePart2(round)
    print("Part1: " + str(score1))
    print("Part2: " +str(score2))


def calcScorePart1(input):
    # Get the ASCII values of the opponent and the user
    opp = ord(input[0])
    # Find the correspond A,B,C for the user's input
    user = ord("A" if input[2] == "X" else ("B" if input[2] == "Y" else "C"))

    # Determine who won the round with the result of substracting the two ASCII values
    if opp-user == 1 or opp-user == -2:
        roundVal = 0
    elif opp-user == -1 or opp-user == 2:
        roundVal = 6
    else:
        roundVal = 3
    
    # Add the value of the users move with the value of the round
    score = (user-64) + roundVal

    return score


def calcScorePart2(input):
    opp = input[0]
    user = input[2]

    # If user needs to lose
    if user == "X":
        #  the value of the move that will lose to the opponent
        roundVal = 3 if opp == "A" else (2 if opp == "C" else 1)
    # If user needs to tie
    elif user == "Y":
        # Add tie value to the user's move value
        roundVal = 3 + (ord(opp)-64)
    # If user needs to win
    else:
        # Add win value to the value of the move that will make the user win
        roundVal = 6 + (1 if opp == "C" else (2 if opp == "A" else 3))
    
    return roundVal

if __name__ == "__main__":
    main()

    


