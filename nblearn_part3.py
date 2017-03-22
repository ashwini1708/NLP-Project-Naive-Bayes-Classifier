import sys
import os

import json
import math
from math import log10
def tokenize(input,dir_1,distinct_words):


    stopwords=open("stopwords.txt", "r", encoding="latin1").read()
    for i in input:
        if i not in stopwords:

            distinct_words.add(i)
            if i not in dir_1:
                dir_1[i]=1
            else:
                dir_1[i]=dir_1[i]+1

    return dir_1


def read_recursive(src):
   # src = '/./Users/ASHU/Spam or ham/train'
    file_counter_ham = 0
    file_counter_spam=0

    total_words_ham=0
    total_words_spam=0

    distinct_words=0

    spam_dir={}
    ham_dir = {}
    total_words=[]
    doc_count=[]

    distinct_words=set([])



    for root, directories, filenames in os.walk(src):

        for directory in directories:
            # if the directory is HAM

            if (directory == "ham"):

                # look for files in directory HAM
                for root_1, directories_1, filenames_1 in os.walk(os.path.join(root, directory)):
                    # open files in HAM folder

                    for filename_1 in filenames_1:
                        input = open(os.path.join(root_1, filename_1), "r", encoding="latin1").read()
                        input = input.split()
                        tokenize(input,ham_dir,distinct_words)
                        file_counter_ham=file_counter_ham+1;

            elif (directory == "spam"):
                # look for files in directory SPAM
                for root_1, directories_1, filenames_1 in os.walk(os.path.join(root, directory)):
                    # open files in SPAM folder

                    for filename_1 in filenames_1:

                        input = open(os.path.join(root_1, filename_1), "r", encoding="latin1").read()
                        input = input.split()

                        tokenize(input,spam_dir,distinct_words)
                        file_counter_spam=file_counter_spam+1;



    total_words_ham = sum(ham_dir.values())
    total_words_spam = sum(spam_dir.values())
    # counting V=>distinct words

    #counting M=>total no of documents
    total_docs=file_counter_ham + file_counter_spam


    #counting M => total number of documents
    jenc=json.JSONEncoder();

    #DOC COUNT HAS probability OF SPAM AND HAM
    doc_count.append(file_counter_spam/(file_counter_spam + file_counter_ham))
    doc_count.append(file_counter_ham/(file_counter_spam + file_counter_ham))

    #total_words has total word count in SPAM , HAM and  also the distinct words in both doc
    total_words.append(total_words_spam + len(distinct_words))
    total_words.append(total_words_ham + len(distinct_words))
    total_words.append(len(distinct_words))


    for i in distinct_words:
        if i in spam_dir:
            spam_dir[i] = log10 (spam_dir[i] ) - log10 (total_words_spam)
        else:
            spam_dir[i] = log10(1) - log10(total_words_spam + len(distinct_words))

        if i in ham_dir:
            ham_dir[i] = log10(ham_dir[i] + 1) -  log10(total_words_ham + len(distinct_words))
        else:
            ham_dir[i] = log10(1) - log10(total_words_ham + len(distinct_words))



    try:
        os.remove('nbmodel.txt')
    except OSError:
        pass


    f=open('nbmodel.txt', 'a')
    f.write(jenc.encode(doc_count)+ "\n")
    f.write(jenc.encode(total_words) + "\n")
    f.write(jenc.encode(spam_dir) + "\n")
    f.write(jenc.encode(ham_dir) + "\n")


# inputdata=open(sys.argv[1])
read_recursive(sys.argv[1])