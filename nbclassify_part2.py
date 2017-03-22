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

    for root, dirs, files in os.walk(src):
        for fname in files:
            if "ham" in fname:
                file_counter_ham=file_counter_ham +1
            elif "spam" in fname:
                file_counter_spam=file_counter_spam +1

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
    output = open("nboutput.txt", "r", encoding="latin1").readlines()
    for line in output:
        line=line.split()
        # print (line[0])
        # print(line[1])
        if line[0].lower() in line[1]:
            if line[0].lower() == "spam":
                correct_spam=correct_spam + 1
            else:
                correct_ham = correct_ham + 1


    #calculating precision
    #precision = (correctly classified as ck) / (classified as ck)

    precision_spam=correct_spam / spam_counter
    precision_ham = correct_ham / ham_counter

    # REcall = (correctly classified as ck) / (belongs to ck)

    recall_spam=correct_spam / file_counter_spam
    recall_ham = correct_ham / file_counter_ham


   # F-score calculation

    f_score_spam =(2* precision_spam * recall_spam )/ (precision_spam + recall_spam)
    f_score_ham = (2 * precision_ham * recall_ham) / (precision_ham + recall_ham)

    print ("precison spam is " ,precision_spam )
    print("precison ham is ", precision_ham)
    print("recall spam is ", recall_spam)
    print("recall ham is ", recall_ham)

    print("F score spam is" ,f_score_spam )
    print("F score ham is", f_score_ham)

    avg_weight = ((f_score_ham + f_score_spam) / 2)

    print("weighted Avg : ", avg_weight)

classify(sys.argv[1])