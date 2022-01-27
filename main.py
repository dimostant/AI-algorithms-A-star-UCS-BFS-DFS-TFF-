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

def calculateClausesResult(a, assignments, unique_literals):
    
    clauses_assignments = []

    print(a)

    for clause in a :

        literals = [line for line in clause if line != '|' and line != ' ']
        print(literals)

        literal_index = 0
        
        for literal in literals :
            if literal_index == 0 :
                if not literal == '-' :
                    clause_result = assignments[unique_literals.index(literals[literal_index])]
                    #debug
                    #print(clause_result)
                    #print("1st")
                    #
                
                else :
                    clause_result = not assignments[unique_literals.index(literals[literal_index  + 1])]
                    #debug
                    #print(clause_result)
                    #print("2nd")
                    #
                    
                literal_index +=1
                #debug
                #print("3rd")
                #
                continue
            
            if literals[literal_index -1] == '-':
                literal_index +=1
                #debug
                #print("4th")
                #
                continue

            if not literal == '-' :
                clause_result = clause_result or assignments[unique_literals.index(literals[literal_index])]
                #debug
                #print(clause_result)
                #print("5th")
                #

            else :
                clause_result = clause_result or not assignments[unique_literals.index(literals[literal_index  + 1])]
                #debug
                #print(clause_result)
                #print("6th")
                #
            literal_index +=1

        print(clause_result)
        clauses_assignments.append(clause_result)
    print(clauses_assignments)
    
    return clauses_assignments

def GSAT(a, maxTries, maxFlips):
        
        unique_literals = []
        for clause in range(len(a)) : 
            for literal in a[clause]:
                if literal in unique_literals :
                    continue
                else :
                    unique_literals.append(literal)
        
        unique_literals.remove(' ')
        unique_literals.remove('|')
        unique_literals.remove('-')

        print(unique_literals)

    #for try in range(maxTries) :

        assignments = []
        #chech if randint has %possibility
        for assignment in range(len(unique_literals)) :
           if random.randint(0, 1) == 1 :
              assignments.append(True)
           else :
              assignments.append(False)
        
        print(assignments)

        #clause result
        clauses_assignments = calculateClausesResult(a, assignments, unique_literals)

        cost = clauses_assignments.count(False)
        print(cost)

        #for flip in range(maxFlips) :
        for i in [1, 2] : #debug    

            if cost == 0 : 
                print("returned")
                return clauses_assignments
            
            else :
                flip_assignments = []
                flip_assignments_costs = []

                #for assignment in range(assignments) :
                for assignment in range(3) :
                    new_assignments = assignments.copy()#so that only new assignments is edited
                    print(new_assignments)
                    new_assignments[assignment] = not new_assignments[assignment]
                    print(new_assignments)
                    flip_assignments.append(new_assignments[:])# : operator so list can get new items and not copy new ones
                    print(flip_assignments) 
                    cost = calculateClausesResult(a, new_assignments, unique_literals).count(False)
                    # does one more iteration ??
                    flip_assignments_costs.append(cost)
                
                print(flip_assignments_costs)

                #sort cost and assignments through cost (from minimum to maximum)
                flip_assignments_sorted = [x for _, x in sorted(zip(flip_assignments_costs, flip_assignments), key=lambda pair: pair[0])]
                #optimize in one command?
                flip_assignments_costs_sorted = sorted(flip_assignments_costs)
                print(flip_assignments_sorted)
                print(flip_assignments_costs_sorted)
                assignments = flip_assignments_sorted[0]
                cost = flip_assignments_costs_sorted[0]

                print(assignments)

        print("false")
        return False

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
    #                 sentence = sentence + R + ' | ' 
    #             else :
    #                 sentence = sentence + R 
                

    #         sentenceExists = False     

    #         for line in txt :
    #             if line == sentence :
    #                 sentenceExists = True  
    #                 break 
                #check for opposite clause
            
    #         if sentenceExists == False :
    #             txt.append(sentence)
       
    #debug
    txt = [ '-x | -v',
            '-z | s | j',
            '-h',
            '-w',
            'h | -o'    ]
    given_literal = '-b'
    #

    GSAT_data = txt #clauses connected with ^

    # while 1:
    #     given_literal = input("give literal")
    #for char in given_literal :
    #    if char != '#' or (char > 'a' and char < 'z') :
                 
    #     #check if input = literal or #
    #     if given_literal == '#' :
    #         break
    #step in for while
    

    given_literal.replace(' ', '')
    if given_literal[0] == '-' :
        given_literal = given_literal[1:2]
    else :
        given_literal = "-"+ given_literal          

    
    max_flips = 5
    max_retries = 5
    GSAT_data.append(given_literal)

    GSAT(GSAT_data, max_retries, max_flips)

    #step in for while 


    f = open("Knowledge database.txt", "a")
    
    #for line in range(len(txt)) :
      #  f.write(txt[line] + '\n')
    f.close() 