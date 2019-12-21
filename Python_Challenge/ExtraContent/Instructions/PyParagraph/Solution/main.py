import os
import csv
import re
import collections
import string

print("Analysis for Two Paragraphs \n--------------------------------")
all_rows = []
words_num = 0
sentence_num = 0
csvpath1 = os.path.join('raw_data','paragraph_1.txt')
csvpath2 = os.path.join('raw_data','paragraph_2.txt')
with open(csvpath1, 'r') as csvfile1, open(csvpath2, 'r') as csvfile2: 
    par1 = csvfile1.read()
    par2 = csvfile2.read()
    both_par = par1 + par2
    words_ct = len(both_par.split( ))
    sentence_ct = both_par.count('.')
    print("Approximate Word Count:",words_ct)
    print("Approximate Sentence Count:",sentence_ct)
    text = both_par.lower()
    alphabet = string.ascii_lowercase
    alphabet_set = set(alphabet)
    counts = collections.Counter(c for c in text if c in alphabet_set)
    for letter in alphabet:
        Average_letter_count = round(sum(counts.values())/ words_ct,1)
    print("Average letter count:",Average_letter_count )
    Sentence_length = round(words_ct / sentence_ct,1)
    print("Average Sentence Length:",Sentence_length)