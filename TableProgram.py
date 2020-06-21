#George Oliver Cook - Created: 21/06/2020, Version: 2.5

def table():
    j = 0;
    print(" ______________________ ");
    print("|"+playerOne+"|"+playerTwo+"|");
    for j in range(10): 
        print("| ",playerOneScoreArray[j]," |",playerTwoScoreArray[j],"|");
        j = j + 1;
    print(" ______________________ ");
    print("");



def writer():
    y = 1;
    z = 1;
    outputFile = open("scoreFile.txt","w");
    outputFile.write(playerOne);
    outputFile.write("\n");
    outputFile.write("\n");
    for x in playerOneScoreArray:
        outputFile.write("Round ");
        outputFile.write(str(y));
        outputFile.write(": ");
        outputFile.write(str(x));
        outputFile.write("\n");

        y = y + 1;
        
    outputFile.write("\n");
    outputFile.write(playerTwo);
    outputFile.write("\n");
    outputFile.write("\n");
    for x in playerTwoScoreArray:
        outputFile.write("Round ");
        outputFile.write(str(z));
        outputFile.write(": ");
        outputFile.write(str(x));
        outputFile.write("\n");

        z = z + 1;
        




playerOneScoreArray = [0] * 10;
playerTwoScoreArray = [0] * 10;

i = 0;


print("Scoring System");
print("");
playerOne = input("Please enter the name of the first player: ");
print("");
playerTwo = input("Please enter the name of the second player: ");
print("");

while True:
    option = int(input("What whould you like to do: (1)Rename "+playerOne+", (2) Rename "+playerTwo+", (3) View the scoring table, (4) Enter in a round score, (9) Exit? "));
    print("");

    if(option == 1):
        temp = input("What would you like to rename "+playerOne+" to? ")
        print("");
        playerOne = temp;

            
    elif(option == 2):
        temp = input("What would you like to rename "+playerTwo+" to? ")
        print("");
        playerTwo = temp;


    elif(option == 3):
        table();

    elif(option == 4):
        if(i < 10):
            playerOneScore = int(input("Input the round score for "+playerOne+": "));
            playerTwoScore = int(input("Input the round score for "+playerTwo+": "));
            print("");

            playerOneScoreArray[i] = playerOneScore;
            playerTwoScoreArray[i] = playerTwoScore;

            i = i + 1;

        else:
            print("All Scores have been inputed.");
            print("");

        #print("Score List for "+playerOne+": ");
        #for x in playerOneScoreArray:
        #    print(x);

        #print("Score List for "+playerTwo+": ");
        #for x in playerTwoScoreArray:
        #    print(x);

    elif(option == 9):
        writer();
        exit();

        
