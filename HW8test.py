import pandas as pd
import csv
df = pd.read_csv("myprediction.csv")

#userID_itemID
"""
for i in range(len(df)):
    esh = str(df["userID"][0]) + "_" + str(df["itemID"][0])
"""
userID_list = []
for i in range(len(df)):
    if df["userID"][i] in userID_list:
        continue
    else:
        userID_list.append(df["userID"][i])

for i in range(len(userID_list)):
    esh = df[df["userID"]== userID_list[i]]
    predictions = []
    esh_list = list(esh["prediction"])
    for p in range(len(esh)):
        predictions.append(esh_list[p])
    predictions = list(reversed(sorted(predictions)))[:3]
    index_list = list(esh["Unnamed: 0"])
    for index in index_list:
        if esh.at[index,"prediction"] in predictions:
            df.at[index,"rating"] = 1.0
        else:
            df.at[index,"rating"] = 0.0
"""    
kaggle_dict = {"TrackID": [],"Predictor": []}
for i in range(len(df)):
    kaggle_dict["TrackID"].append(str(df["userID"][i]) + "_" + str(df["itemID"][i]))
    kaggle_dict["Predictor"].append(df["rating"][i])
kaggle_df = pd.DataFrame.from_dict(kaggle_dict)

kaggle_df.to_csv('myprediction1.csv')
"""

kaggle_output = 'myprediction1_kaggle.csv'
fOut_submission = open(kaggle_output, 'w')
csv_writer = csv.writer(fOut_submission)
header_submission = ["TrackID", "Predictor"]
csv_writer.writerow(header_submission)
for i in range(len(df)):
    csv_writer.writerow([f"{df['userID'][i]}_{df['itemID'][i]}", int(df["rating"][i])])
fOut_submission.close()
