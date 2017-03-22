import sys
import os
import json
import math
from math import log10

record=[]
def classify(src):
    intermediate_output= open("nbmodel.txt", "r", encoding="latin1")
    for line in intermediate_output:
        record.append(json.loads(line))


    probability=record[0]
    words=record[1]
    spam_dic=record[2]
    ham_dic=record[3]

    # FETCHING ACTUAL FILE COUNT
    file_counter_ham=0
    file_counter_spam=0

    spam_counter=0
    ham_counter=0

    correct_spam=0
    correct_ham=0



    try:
        os.remove('nboutput.txt')
    except OSError:
        pass

    f = open('nboutput.txt', 'w')
    for root, dirs, files in os.walk(src):
        for file in files:
            if file.endswith(".txt"):
                file_open=open(root + "/" + file, "r", encoding="latin1").read()
                tokens=file_open.split()
                prob_spam_words = 0.0
                prob_ham_words = 0.0
                for i in tokens:
                    if i in spam_dic:
                        prob_spam_words = (prob_spam_words) + spam_dic[i]
                    # else:
                    #     prob_spam_words+=0.0


                    if i in ham_dic:
                        prob_ham_words = (prob_ham_words) + (ham_dic[i])
                    # else:
                    #     prob_ham_words+=0.0


                prob_spam_words=log10(probability[0]) + (prob_spam_words)
                prob_ham_words = log10(probability[1]) +(prob_ham_words)

                if(prob_spam_words > prob_ham_words):
                    f.write("spam" +" " + root + '/' +  file + "\n")
                    spam_counter=spam_counter+1
                elif(prob_spam_words < prob_ham_words):
                    f.write("ham" +" " + root + '/'+ file + "\n")
                    ham_counter=ham_counter+1
                else:
                    f.write(root + file + "\n")
    f.close()


classify(sys.argv[1])