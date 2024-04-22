
import numpy as np
import pandas as pd
import csv
import os


# accuracy score list to keep track of each submissions score on kaggle to be used for the formula on slide 15
accuracy = []
# corresponding filename for accuracy scores
files = []
# holds the prediction vectors from each submission
S = []
STx = []
Sensemble = [] 

directory = os.fsencode("{ADD PATH TO FOLDER CONTAINING KAGGLE SUBMISSIONS}")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    files.append(filename)
    accuracy_score = int(filename[-7:][:3])/1000
    accuracy.append(accuracy_score)
    df = pd.read_csv("ensemble_submissions/" +filename)
    S.append(np.array(df["Predictor"]))
    N = len(df["Predictor"]) # should be 120000
    Pi = accuracy_score
    stx = 2*Pi-1
    STx.append(stx)
    
S = np.array(S)
STx = np.array(STx)

# memory allocation error, need to break up into sections of 6 for each user to reduce the memory burden

for i in range(len(S[0])):
    if (i+1) % 6 == 0: # 0-5 hold ratings for first user, do matrix calculations per user to make memory load smaller then add predictios to Sensemble
        S_sub = []
        for j in range(len(S)):
            S_sub.append(S[j][i-5:i+1])
        





