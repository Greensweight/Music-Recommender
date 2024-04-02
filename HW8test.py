import pandas as pd
import csv
import os
#https://stackoverflow.com/questions/16683701/in-pandas-how-to-get-the-index-of-a-known-value

# use after AAI627spark.ipynb generates myprediction.csv

os.remove("C:/Users/Marc D/OneDrive - stevens.edu/AAI 627/myprediction1_kaggle.csv")
df = pd.read_csv("myprediction.csv")
df_old = pd.read_csv("output3.csv")
# output3.csv is the output from read_rating_V3.py

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
    
kaggle_dict = {"TrackID": [],"Predictor": []}
for i in range(len(df)):
    kaggle_dict["TrackID"].append(str(df["userID"][i]) + "_" + str(df["itemID"][i]))
    kaggle_dict["Predictor"].append(df["rating"][i])

kaggle_df = pd.DataFrame.from_dict(kaggle_dict)

kaggle_df.to_csv('myprediction1.csv')


#combined_df = pd.concat([df_old,df]).drop_duplicates().reset_index(drop=True)

kaggle_output = 'myprediction1_kaggle.csv'
fOut_submission = open(kaggle_output, 'w')
csv_writer = csv.writer(fOut_submission)
header_submission = ["TrackID", "Predictor"]
csv_writer.writerow(header_submission)
for i in range(len(df)):
    csv_writer.writerow([f"{df['userID'][i]}_{df['itemID'][i]}", int(df["rating"][i])])
fOut_submission.close()


df_new = pd.read_csv(kaggle_output)

"""
for i in range(len(df_new)):
    if df_new["TrackID"][i] in df_old.values:
        index_old = df_old.loc[df_old["TrackID"] == df_new["TrackID"][i]].index[0]
        index_new = df_new.loc[df_new["TrackID"] == df_new["TrackID"][i]].index[0]
        #df_old.at[index_old, "TrackID"] = df_new.at[index_new, "TrackID"]
        df_old.at[index_old, "Predictor"] = df_new.at[index_new, "Predictor"]
"""
"""
for i in range(len(df_new)):
    if df_new["TrackID"][i] in df_old.values:
        df_old = df_old.merge(df_new[['TrackID', 'Predictor']], on='TrackID', how='left')
#df_old is now updated matrix
"""

"""
print("len df_new: " + str(len(df_new)))
print("after remapping to updated")
df_new = df_old
print("len df_new: " + str(len(df_new)))
"""

df_update= pd.concat([df_old, df_new]).drop_duplicates(subset='TrackID', keep='last').reset_index(drop=True)
esh_df = df_old[df_old.duplicated("TrackID")]
df_update= pd.concat([df_update, esh_df]).reset_index(drop=True)

kaggle_output = 'myprediction1_kaggle.csv'
fOut_submission = open(kaggle_output, 'w')
csv_writer = csv.writer(fOut_submission)
header_submission = ["TrackID", "Predictor"]
csv_writer.writerow(header_submission)
for i in range(len(df_old)):
    csv_writer.writerow([f"{df_update['TrackID'][i]}", int(df_update["Predictor"][i])])
fOut_submission.close()
