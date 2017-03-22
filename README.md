# NLP-Projects


Naïve Bayes Classifier in Python:

nblearn.py will learn a naive Bayes model from labeled data, and nbclassify.py will use the model to classify new data. nblearn.py will be invoked in the following way:
  >python3 nblearn.py /path/to/input

The argument is a data directory. The script should search through the directory recursively looking for subdirectories containing the folders: "ham" and "spam". Emails are stored in files with the extension ".txt" under these directories.

"ham" and "spam" folders contain emails failing into the category of the folder name (i.e., a spam folder will contain only spam emails and a ham folder will contain only ham emails). Each email is stored in a separate text file. The emails have been preprocessed removing HTML tags, and leaving only the body and the subject. The files have been tokenized such that white space always separates tokens.

nblearn.py will learn a naive Bayes model from the training data, and write the model parameters to a file called nbmodel.txt. The format of the model is up to you, but it should contain sufficient information for nbclassify.py to successfully classify new data.
nbclassify.py will be invoked in the following way: >python3 nbclassify.py /path/to/input

nblearn_part2 and nbclassify_part2 will experiment on 10% of the total data to check the accuracy
nblearn_part3 and nbclassify_part3 will classify on the entire dataset with add one smoothing to it.

Calculation of Precision, Recall and F1
