
def userInput():
    Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    Index = int(input("Enter Index"))
    if Index > 26:
        print("Input out of range. Please check again")
    else:
        print(Alphabet[Index])
userInput()