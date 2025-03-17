# Problem: the-minion-game - https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
    n = len(string)
    vowel = {"A","E","I","O","U",}
    stuart = kevin = 0
    for i in range(n):
        if string[i] in vowel:
            kevin += n - i
        else:
            stuart += n - i
    if stuart == kevin:
        print("Draw") 
    elif stuart > kevin:
        print("Stuart " + str(stuart)) 
    else:
        print("Kevin " + str(kevin)) 