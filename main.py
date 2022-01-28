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

    for trie in range(maxTries) :

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

        for flip in range(maxFlips) :
            
            solution = True
            
            #save runs if no solution can be found
            if solution == False:
                continue

            print("maxflips")
            if cost == 0 : 
                print("returned")
                return True
            
            else :
                flip_assignments = []
                flip_assignments_costs = []

                for assignment in range(len(assignments)) :
                    new_assignments = assignments.copy() #so that only new assignments is edited
                    print(new_assignments)
                    new_assignments[assignment] = not new_assignments[assignment]
                    print(new_assignments)
                    flip_assignments.append(new_assignments[:])# : operator so list can get new items and not copy new ones
                    print(flip_assignments) 
                    new_cost = calculateClausesResult(a, new_assignments, unique_literals).count(False)
                    flip_assignments_costs.append(new_cost)
                
                print(flip_assignments_costs)

                #sort cost and assignments through cost (from minimum to maximum)
                flip_assignments_sorted = [x for _, x in sorted(zip(flip_assignments_costs, flip_assignments), key=lambda pair: pair[0])]
                #optimize in one command?
                flip_assignments_costs_sorted = sorted(flip_assignments_costs)
                print(flip_assignments_sorted)
                print(flip_assignments_costs_sorted)
                
                if flip_assignments_costs_sorted[0] < cost :
                    assignments = flip_assignments_sorted[0]
                    cost = flip_assignments_costs_sorted[0]
                else :
                    solution = False

                print(assignments)

        
        if cost == 0 : 
            print("returned")
            return True
        
    print("false")
    return False



if __name__ == "__main__":

    """
        it_is = False

    while not it_is:
        C = input("Give number of sentences for knolwedge database")
        try:
            int(C)
            it_is = True
        except ValueError:
            it_is = False

    it_is = False

    while not it_is:
        L = input("Give max number of literals for every sentence")
        try:
            int(L)
            it_is = True
        except ValueError:
            it_is = False

    it_is = False

    while not it_is:
        P = input("Give number of total literals that can be used(max 26, must be bigger than L)")
        try:
            int(P)
            it_is = True
        except ValueError:
            it_is = False
        if it_is == True:
            if (int(P) < 27) and (int(P) > int(L)):
                it_is = True
            else:
             it_is = False

    C = int(C)
    L =int(L)
    P = int(P)  

    # # print (C, L, P) 
    # #debug
    # C = 3
    # L = 3
    # P = 4
    # print(C, L, P)
    # #

    f = open("Knowledge database.txt", "a")
    f.write(str(C) + '\n' + str(L) + '\n' + str(P) + '\n')
    f.close

    #debug
    total_tries = 0
    #
    
    for X in range(C) :
        sentence = '' 
        sentenceExists = True
        while sentenceExists == True : 
            total_tries = total_tries + 1

            terms = random.randint(1, L)
            #chech if randint has %possibility
            for Y in range(terms) :
                R_repeats = True

                while  R_repeats == True : 
                    R = literals[random.randint(1, P-1)]
                    R_repeats = False
                    

                    for literal in sentence :
                        if literal == '-' or literal == ' ' or literal == '^':
                            continue
                        if literal == R :
                            R_repeats = True
                            break
                
                if random.randint(0, 1) == 1 :
                    R ='-' + R
                if Y != terms-1 :
                    sentence = sentence + R + ' | ' 
                else :
                    sentence = sentence + R 
                

            sentenceExists = False     

            for line in txt :
                if line == sentence :
                    sentenceExists = True  
                    break
                #if line 
                #check for opposite clause       1611, 1603 copy paste. Melinaki copy paste.  
            if sentenceExists == False :
                txt.append(sentence)

    f = open("Knowledge database.txt", "a")
    
    for line in range(len(txt)) :
        f.write(txt[line] + '\n')
    f.close() 
    """

    #debug
    txt = [ '-a | -b',
            'c'
                    ]
    # given_literal = '-b'
    #

    GSAT_data = txt #clauses connected with ^

    
    while 1:
        given_literal = ''

        while not (len(given_literal) == 1 and (((given_literal.isalpha() and given_literal.islower()) or ('#' == given_literal)))):
            given_literal = input("give literal")
        
        if given_literal == '#' :
            print("Exit")
            break

        notation = ''

        while not notation.upper() == 'Y' and not notation.upper() == 'N' :
            notation = input("does literal have - in front of it? (y/n)").upper()
        
        if notation.upper() == 'Y':
            notated_literal = '-' + given_literal
        else :
            notated_literal = given_literal

        print(notated_literal)

        GSAT_data.append(notated_literal)
        print(GSAT_data)

        #can be given by user 
        max_flips = 5
        max_retries = 5

        entailment = False  
        Gsat = False 

        entailment = GSAT(GSAT_data, max_retries, max_flips)
        if entailment == False :
            print(entailment)#debug
            #Resolutions = #resolution 
            #GSAT_data = Resolutions
            # f = open("Knowledge database.txt", "a")
    
            # for line in range(len(txt)) :
            #     f.write(Resolutions + '\n')
            # f.close() 
        else :
            Gsat = True

        print(notated_literal + ",")

        if entailment == True:
            print("Literal is entailed by KB, ")
            if Gsat == True :
                print("entailment was proven by GSAT\n\n")
            else :
                print("entailment was proven by resolution\n\n")
        else :
            print("Literal is not entailed by KB")
        