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

def GSAT(a, maxTries, maxFlips):
    for i in maxTries :
        T = a
    

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


    # #debug
    # C = 5
    # L = 3
    # P =26
    # print(C, L, P)
    # #

    # f = open("Knowledge database.txt", "a")
    # f.write(str(C) + '\n' + str(L) + '\n' + str(P) + '\n')
    # f.close() 

    # #debug
    # total_tries = 0
    # #
    
    # for X in range(C) :
    #     sentence = '' 
    #     sentenceExists = True
    #     while sentenceExists == True : 
    #         total_tries = total_tries + 1

    #         terms = random.randint(1, L)
    #         #chech if randint has %possibility
    #         for Y in range(terms) :
    #             R_repeats = True

    #             while  R_repeats == True : 
    #                 R = literals[random.randint(1, P-1)]
    #                 R_repeats = False
                    

    #                 for literal in sentence :
    #                     if literal == '-' or literal == ' ' or literal == '^':
    #                         continue
    #                     if literal == R :
    #                         R_repeats = True
    #                         break
                
    #             if random.randint(0, 1) == 1 :
    #                 R ='-' + R
    #             if Y != terms-1 :
    #                 sentence = sentence + R + ' ^ ' 
    #             else :
    #                 sentence = sentence + R 
                

    #         sentenceExists = False     

    #         for line in txt :
    #             if line == sentence :
    #                 sentenceExists = True  
    #                 break 
            
    #         if sentenceExists == False :
    #             txt.append(sentence)
       
    #debug
    txt = [ '-x ^ -v',
            '-z ^ s ^ j',
            '-h',
            '-w',
            'h ^ -o'    ]
    print(txt)
    given_literal = 'h'
    #

    # while 1:
    #     given_literal = input("give literal")
    #for char in given_literal :
    #    if char != '#' or (char > 'a' and char < 'z') :
                 
    #     #check if input = literal or #
    #     if given_literal == '#' :
    #         break
    #step in for while
    
    GSAT_data = txt 

    given_literal.replace(' ', '')
    if given_literal[0] == '-' :
        given_literal[0] = given_literal[1] 
        del given_literal[1]
    else :
        given_literal = given_literal + given_literal
        given_literal[0] = '-'           

    GSAT_data.append(given_literal)



    #step in for while 


    f = open("Knowledge database.txt", "a")
    
    for line in range(len(txt)) :
        f.write(txt[line] + '\n')
    f.close() 