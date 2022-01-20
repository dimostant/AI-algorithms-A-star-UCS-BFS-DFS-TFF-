from ctypes.wintypes import CHAR, INT
import random
import sys

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
    #     P = input("Give number of total literals that can be used")
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
# :(
    C = 5
    L = 3
    P =26
    print(C, L, P)



    # Loop for C
        # exists = True
        # While exists == True
            # choose a number from 0 to L
            # loop for L
                # choose a number from 1 to P
                # 50% probability for the number to have a not in front ( - for now , actual character if there is time)
                # Add word to sentence
            # loop for txt sentences(skip sentences that give data?)
            # if new sentence exists in txt continue?? (exists == True)
            # exists == False
        # Add sentence to txt and change line

    total_tries = 0
    
    for X in range(C) :
        sentence = '' 
        sentenceExists = True
        while sentenceExists == True : 
            total_tries = total_tries + 1

            for Y in range(random.randint(1, L)) :
                R = literals[random.randint(1, P-1)]
                if random.randint(0, 1) == 1 :
                    R ='-' + R
                sentence = sentence + R
                #separate with ' '? /Xwrizoume me ' '?
            f = open("Knowledge database.txt", "r") 

            sentenceExists = False

            for line in f :
                if line == sentence :
                    sentenceExists = True  
                    break 

            if sentenceExists == False :
                f = open("Knowledge database.txt", "a") 
                f.write(sentence + '\n')
            f.close()
    print(total_tries)

            # print(f.read())