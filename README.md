# Three_letter_unique_abbreviation_generator

**Project: ** THREE-LETTER UNIQUE ABBREVIATION GENERATOR FOR USER-SUPPLIED LIST OF PHRASES

**Rules:**
* Abbreviations consist entirely of upper-case letters
* All non-letter characters are completely ignored when generating abbreviations.
* Each abbreviation consists of the first letter of the name followed by two further letters from the name, in order.
* Each phrase in the supplied list must have the first character a letter.
* Each abbreviation is unique or any abbreviation which can be formed from more than one name on the list is excluded.
* Each abbreviation is given a score which indicates how good it is (the lower the score, the better the abbreviation). The score for an abbreviation is the sum of
scores for its second and third letters (the first letter is always the first letter of
the name, so it does not get a score). These individual letter scores depend on their position in a word of the name and are calculated as follows:
  i.	If a letter is the the first letter of a word in the name, then it has a score of 0.
  ii.	Otherwise, if a letter is the last letter of a word in the name, then it has a score of 5 unless the letter is E, in which case the score is 20.
  iii.	If a letter is neither the first nor last letter of a word, then its score is the sum of a position value, which is 1 for the second letter of a word, 2 for the third letter, and 3 for any other position, plus a value based on how common/uncommon this letter is in English: 1 for Q, Z, 3 for J, X, 6 for K, 7 for F, H, V, W, Y, 8 for B, C, M, P, 9 for D, G, 15 for L, N, R, S, T, 20 for O, U, 25 for A, I and 35 for E.
* For a name, the abbreviation with the lowest score is accepted. If more than one abbreviation for a name has the lowest score then all of them are accepted.
