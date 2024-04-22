
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
ratings = []

directory = os.fsencode("{ADD PATH TO DIRECTORY CONTAINING ONLY THE PREDICTION VECTORS}")

count = 0
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
    if count == 0: # only do once
        ratings = df
        count +=1

for i in range(len(S)):
    for j in range(len(S[0])):
        if S[i][j] == 0:
            S[i][j] = -1
    
S = np.array(S)
STx = np.array(STx)

esh = np.matmul(S, np.transpose(S))
iesh = np.linalg.inv(esh)
sesh = np.matmul(np.transpose(S), iesh)
Sensemble = np.matmul(sesh, STx)


for i in range(len(Sensemble)):
    if (i+1) % 6 == 0: # 0-5 hold ratings for first user, do matrix calculations per user to make memory load smaller then add predictios to Sensemble
        S_sub_ensemble = Sensemble[i-5:i+1]
        S_sub_ensemble_sort_max = list(reversed(sorted(S_sub_ensemble)))[0:3]
        index = 0
        for j in range(i-5, i):
            if S_sub_ensemble[index] in S_sub_ensemble_sort_max:
                ratings.at[j, "Predictor"] = 1
            else:
                ratings.at[j, "Predictor"] = 0
            index += 1

os.remove("kaggle_submission_ensemble.csv")

ratings.to_csv("kaggle_submission_ensemble.csv", index=False)
        
        




