from ctypes.wintypes import CHAR, INT
import random
import sys

txt = []
literals = list (
    ['a', 'b', 'c',
     'd', 'e', 'f',
     'g', 'h', 'i',
     'j', 'k', 'l',
     'm', 'n', 'o', 
     'p', 'q', 'r', 
     's', 't', 'u', 
     'v', 'w', 'x', 
     'y', 'z']
)


if __name__ == "__main__":
    # it_is = False

    # while not it_is:
    #     C = input("Give number of sentences for knolwedge database")
    #     try:
    #         int(C)
    #         it_is = True
    #     except ValueError:
    #         it_is = False

    # it_is = False

    # while not it_is:
    #     L = input("Give max number of literals for every sentence")
    #     try:
    #         int(L)
    #         it_is = True
    #     except ValueError:
    #         it_is = False

    # it_is = False

    # while not it_is:
    #     P = input("Give number of total literals that can be used(max 26)")
    #     try:
    #         int(P)
    #         it_is = True
    #     except ValueError:
    #         it_is = False
    #     if it_is == True:
    #         if (int(P) < 27) and (int(P) > -1):
    #             it_is = True
    #         else:
    #          it_is = False


    #debug
    C = 5
    L = 3
    P =26
    print(C, L, P)
    #

    f = open("Knowledge database.txt", "a")
    f.write(str(C) + '\n' + str(L) + '\n' + str(P) + '\n')
    f.close() 

    #debug
    total_tries = 0
    #
    
    for X in range(C) :
        sentence = '' 
        sentenceExists = True
        while sentenceExists == True : 
            total_tries = total_tries + 1

            #chech if randint has %possibility
            for Y in range(random.randint(1, L)) :
                R = literals[random.randint(1, P-1)]
                if random.randint(0, 1) == 1 :
                    R ='-' + R
                sentence = sentence + R
                #separate with ' '? /Xwrizoume me ' '?
            #f = open("Knowledge database.txt", "r") 

            sentenceExists = False

            for line in txt :
                if line == sentence :
                    sentenceExists = True  
                    break 
            
            #f.close()

           # f = open("Knowledge database.txt", "a") 
            if sentenceExists == False :
                txt.append(sentence)
                #f.write(sentence + '\n')
            
            #f.close()
    #debug
    print(total_tries)
    print(txt)
    #
    f = open("Knowledge database.txt", "a")
    
    for line in range(len(txt)) :
        f.write(txt[line] + '\n')
    f.close() 