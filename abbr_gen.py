# importing necessary libraries
import re
import numpy as np

# Function for extracting all possible ordered abbreviations for a word
def form_abbr(word):
    fltr = word[0]
    abbr_list = []
    i = 1
    while i <= len(word)-2:
        for j in range(i,len(word)-1):
            for k in word[j+1:]:
                abbr = fltr+word[j]+k
                if (abbr.isalpha()) & (abbr not in abbr_list):
                    abbr_list.append(abbr)
        i = i+1
    return abbr_list

# function for generating score for a abbreviation of a word 
def scoregen(word,abbr):
    wordmod = word.replace("'","")
    words = re.split('[^a-zA-Z]', wordmod)
    ltr2 = abbr[1]
    ltr3 = abbr[2]
    score = letterscore(ltr2,words) + letterscore(ltr3,words)
    return score
   
# function for getting the score of a letter in abbreviation of a word
def letterscore(ltr,words):
    minscore = 1e9
    score = 1e9
    for w in words:
        if ltr in w:
            if len(w) == 1:
                score = 0
            elif len(w) == 2:
               if ltr == w[0]:
                   score= 0
               elif ltr == w[-1]:
                    if ltr == 'E':
                        score = 20
                    else:
                        score = 5
            elif len(w) == 3:
               if ltr == w[0]:
                   score= 0
               elif ltr == w[-1]:
                    if ltr == 'E':
                        score = 20
                    else:
                        score = 5
               else:
                   score = 1 + valsdict[ltr]
            elif len(w) == 4:
               if ltr == w[0]:
                   score= 0
               elif ltr == w[-1]:
                    if ltr == 'E':
                        score = 20
                    else:
                        score = 5
               elif ltr == w[1]:
                   score = 1 + valsdict[ltr]
               else:
                   score = 2 + valsdict[ltr]
                   
            else:
                if ltr == w[0]:
                   score= 0
                elif ltr == w[-1]:
                     if ltr == 'E':
                         score = 20
                     else:
                         score = 5
                elif ltr == w[1]:
                    score = 1 + valsdict[ltr]
                elif ltr == w[2]:
                    score = 2 + valsdict[ltr]
                else:
                    score = 3 + valsdict[ltr]
        minscore = min(score,minscore)                    
    return minscore

# main  function for reading user input file and surname of output file
def main():
    f = input('Please enter the name of the input file:')
    file = open(f+'.txt','r')
    data = file.read()
    words = data.split(sep='\n')
    file.close()
    surname = input('Please enter your surname which will be name of the output file:')
    # converting all words to uppercase
    wordsup = list(map(lambda x: x.upper(),words))
    # Extracting abbreviations and scores for all words
    abbrs = []
    scores = []    
    for w in wordsup:
        abbr_list = form_abbr(w)
        abrscores = [] 
        for abr in abbr_list:
            score = scoregen(w,abr)
            abrscores.append(score)       
        abbrs.append(abbr_list)
        scores.append(abrscores)
    # removing duplicate abbreviations
    i = 0
    while i<=len(abbrs)-2:
        for j in range(i,len(abbrs)-1):
            restabbr = abbrs[j+1:]
            restscore = scores[j+1:]
            for k in range(len(restabbr)):
                both = set(abbrs[j]).intersection(restabbr[k])
                if len(both) != 0:
                    indices_A = [abbrs[j].index(x) for x in both]
                    indices_B = [restabbr[k].index(x) for x in both]
                    for index in sorted(indices_A, reverse=True):
                        del abbrs[j][index]
                        del scores[j][index]
                    for index in sorted(indices_B, reverse=True):
                        del restabbr[k][index]
                        del restscore[k][index]
        i = i+1
    # Appending the best abbreviation/s for a word along with word in string and printing in suitable format    
    strwrite = ''
    for s in range(len(scores)):
        if len(scores[s]) == 0:
            print(words[s],":",'')
            strwrite = strwrite+words[s]+'\n\n'
        else:
            indices = [index for index, element in enumerate(scores[s]) if element == min(scores[s])]
            print(words[s],":",np.array(abbrs[s])[indices])
            strwrite = strwrite+words[s]+'\n'+' '.join(np.array(abbrs[s])[indices])+'\n'
    
    # printing the generated string to a output file
    out = open(surname+'_'+f+'_abbrevs.txt','w')
    n = out.write(strwrite)
    out.close()


# dictionary for value of letter based on how common/uncommon it is in english language
valsdict = {'A':25,'B':8,'C':8,'D':9,'E':35,'F':7,'G':9,'H':7,'I':25,'J':3,'K':6,'L':15,'M':8,'N':15,'O':20,
            'P':8,'Q':1,'R':15,'S':15,'T':15,'U':20,'V':7,'W':7,'X':3,'Y':7,'Z':1}


main()







    

        