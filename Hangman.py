
characterList=[]
#
counter=0
numberOfLives=8

def ClearScreen():
    print(50*"\n")
'''    
def guess():    
    Guess=input("Enter your character guess: ")
    while Guess!="" or Guess!=" " :
        for charac in Guess:
            if charac==characterList[counter]:
                vowel.replace(characterList[counter],charac)
            else:
                numberOfLives-=1
                print("you have only ",numberOfLives,"lives remaining try again ")
            break
        counter+=1
        guess()
'''

def hangMan():
    numberOfLives=8
    characterList=[]
    designList=[]
    counter=0
    x=0
    Answer=input("Enter the name of the movie: ")
    ClearScreen()
    print("You Have ",numberOfLives," lives left")
    characterList=list(Answer)
    for word in range (len(characterList)):
        if characterList[word]=='a' or characterList[word]=='e' or characterList[word]=='i' or characterList[word]=='o' or characterList[word]=='u':
            characterList[word]="º"
        elif 48<=ord(characterList[word])<=57:
            characterList[word]="#"
        elif characterList[word]==" ":
            characterList[word]="/"
        else:
            characterList[word]="_"
    print(' '.join(characterList))
'''
    while x<len(Answer) or numberOfLives>0:
        yourGuess=input("Please guess a letter: ")
        for char in range (len(Answer)):
            if Answer[char]==yourGuess :
                characterList=yourGuess
                print("you guessed a correct word,number or space")
                x+=1
            else:
                numberOfLives-=1
                print("wrong guess try again, you life has reduced by 1", numberOfLives)
        print(' '.join(characterList))
        
'''

'''
    for char in Answer:
        if char=='a' or char=='e'or char=='i'or char=='o'or char=='u':
            vowel="º "
        elif 48<=ord(char)<=57:
            vowel="# "
        elif char==" ":
            vowel= "/ "
        else :
            vowel="__ "
        print(vowel,end="")
        designList.append(vowel)#has list of design elements
        characterList.append(char)#has list of all characters
    print(designList,characterList)
    print("\n")
    while x<=len(designList):
        yourGuess=input("enter your guess: ")
        if characterList.count(yourGuess)>0:
            #search on how to replace item
            designList[counter]=yourGuess
            print(designList)
            counter+=1
        elif characterList.count(yourGuess)==0:
            print("guess again this does not exist in the list")
            
        else:
            print("bye")
        x+=1
'''
'''
    #print(characterList)
    def func():
        Guess=input("Enter your character guess: ")
        for charac in Guess:
            if characterList[counter]==charac:
                new=list(vowel)
                new[counter]=charac
                ''.join(new)
                print(new)
                func()
            else:
                print("you lost")
            counter+=1


'''


'''
    while Guess!="" or Guess!=" " :
        for charac in Guess :
            for item in characterList:
                if charac==item:
                    vowel.replace(vowel[counter],charac)
                else:
                    numberOfLives-=1
                    print("you have only ",numberOfLives,"lives remaining try again ")
            break
        counter+=1

#guess();
'''
'''
                      
hangMan()             
'''

