# Three_letter_unique_abbreviation_generator

**Project:** THREE-LETTER UNIQUE ABBREVIATION GENERATOR FOR USER-SUPPLIED LIST OF PHRASES

**Rules:**
* Abbreviations consist entirely of upper-case letters
* All non-letter characters are completely ignored when generating abbreviations.
* Each abbreviation consists of the first letter of the name followed by two further letters from the name, in order.
* Each phrase in the supplied list must have the first character a letter.
* Each abbreviation is unique or any abbreviation which can be formed from more than one name on the list is excluded.
* Each abbreviation is given a score which indicates how good it is (the lower the score, the better the abbreviation). The score for an abbreviation is the sum of
scores for its second and third letters (the first letter is always the first letter of
the name, so it does not get a score). These individual letter scores depend on their position in a word of the name and are calculated as follows:
  * If a letter is the the first letter of a word in the name, then it has a score of 0.
  * Otherwise, if a letter is the last letter of a word in the name, then it has a score of 5 unless the letter is E, in which case the score is 20.
  * If a letter is neither the first nor last letter of a word, then its score is the sum of a position value, which is 1 for the second letter of a word, 2 for the third letter, and 3 for any other position, plus a value based on how common/uncommon this letter is in English: 1 for Q, Z, 3 for J, X, 6 for K, 7 for F, H, V, W, Y, 8 for B, C, M, P, 9 for D, G, 15 for L, N, R, S, T, 20 for O, U, 25 for A, I and 35 for E.
* For a name, the abbreviation with the lowest score is accepted. If more than one abbreviation for a name has the lowest score then all of them are accepted.
**Input:**
A text file containing the list of names to generate abbreviations where each name is given in a new line.
**Output:**
The output text file containing each name of the input followed by the generated abbreviation/s in the next line. If no acceptable abbreviation for some name a blank line is given after that name in the output file.

**Approach/ Algorithm:**
* The necessary libraries ‘re’ for special character search and NumPy for array operations are imported.
* A function called "form_abbr" is defined to extract all possible ordered abbreviations for a word.
* Another function called "scoregen" is defined to generate a score for an abbreviation of a word.
* A function called "letterscore" is defined to get the score of a letter in an abbreviation of a word.
* The main function is defined to read the user input file and surname for the output file.
* The input file is opened, and the data is read and split into words.
* The words are converted to uppercase.
* Abbreviations and scores are extracted for all words, using the "form_abbr" and "scoregen" functions.
* Duplicate abbreviations are removed from the list of abbreviations.
* The best abbreviation(s) for each word is determined based on the scores and printed in a suitable format. The output is also written to an output file.

**Testing:**
* Test 1: Input = names.txt, Output = surname_names_abbrevs.txt
* Test 2: Input = trees.txt, Output = surname_trees_abbrevs.txt 
