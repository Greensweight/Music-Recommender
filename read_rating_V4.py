#!/usr/bin/env python

import csv
import numpy
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import os
import warnings
import pandas as pd
warnings.filterwarnings('ignore')

dataDir='{ADD PATH TO DATA DIRECTORY}'
file_name_test='testTrack_hierarchy.txt'
file_name_train='trainIdx2_matrix.txt'
output_file1= 'output4.txt'
output_file2= 'output4.csv'
os.remove(output_file1)
os.remove(output_file2)

fTest = open(file_name_test, 'r')
fTrain = open(file_name_train, 'r')
Trainline = fTrain.readline()
fOut_complete = open(output_file1, 'w')
fOut_submission = open(output_file2, 'w') 
header_complete = "UserID|TrackID|AlbumRating|ArtistRating|Genre1Rating|Genre2Rating|Genre3Rating|Genre4Rating|Genre5Rating|Genre6Rating|Genre7Rating|NumberRatedGenres|MaxGenreScore|MinGenreScore|SumGenreScores|AverageGenreScore|VarianceGenreScore|RangeGenre|AverageTrack|Num100Track|Num90Track|Num80Track|Num70Track|Num60Track|Num50Track|SumTrack|VarianceTrack|NumRatedTrack|AverageAlbum|Num100Album|Num90Album|Num80Album|Num70Album|Num60Album|Num50Album|SumAlbum|VarianceAlbum|NumRatedAlbum|AverageArtist|Num100Artist|Num90Artist|Num80Artist|Num70Artist|Num60Artist|Num50Artist|SumArtist|VarianceArtist|NumRatedArtist|RatingValue\n"
header_submission = ["TrackID", "Predictor"]
fOut_complete.write(header_complete)
csv_writer = csv.writer(fOut_submission)
csv_writer.writerow(header_submission)

df_test = pd.read_csv("testTrack_hierarchy.txt", header = None, delimiter = "|", on_bad_lines = "skip")
df_train = pd.read_csv("trainIdx2_matrix.txt", header = None, delimiter = "|")

trackID_vec = [0]*6
albumID_vec = [0]*6
artistID_vec = [0]*6
genre1ID_vec = [0]*6
genre2ID_vec = [0]*6
genre3ID_vec = [0]*6
genre4ID_vec = [0]*6
genre5ID_vec = [0]*6
genre6ID_vec = [0]*6
genre7ID_vec = [0]*6
rating_vec = [0]*6
genre_vec = [0]*7 # 7 genres
lastUserID = -1

user_rating_inTrain = numpy.zeros(shape=(6,46)) # change shape from (6,3) to (6,46) to account for genres and other features 

for line in fTest:
    arr_test = line.strip().split('|')
    userID = arr_test[0]
    trackID = arr_test[1]
    albumID = arr_test[2]
    artistID = arr_test[3]
    try:
        genre1ID = arr_test[4]
    except IndexError:
        genre1ID = 0

    try:
        genre2ID = arr_test[5]
    except IndexError:
        genre2ID = 0

    try:
        genre3ID = arr_test[6]
    except IndexError:
        genre3ID = 0

    try:
        genre4ID = arr_test[7]
    except IndexError:
        genre4ID = 0

    try:
        genre5ID = arr_test[8]
    except IndexError:
        genre5ID = 0

    try:
        genre6ID = arr_test[9]
    except IndexError:
        genre6ID = 0
    try:
        genre7ID = arr_test[10]
    except IndexError:
        genre7ID = 0
        
    if userID != lastUserID:
        ii = 0
        user_rating_inTrain = numpy.zeros(shape=(6,46)) # Reset for new user

    trackID_vec[ii] = trackID
    albumID_vec[ii] = albumID
    artistID_vec[ii] = artistID
    genre1ID_vec[ii] = genre1ID
    genre2ID_vec[ii] = genre2ID
    genre3ID_vec[ii] = genre3ID
    genre4ID_vec[ii] = genre4ID
    genre5ID_vec[ii] = genre5ID
    genre6ID_vec[ii] = genre6ID
    genre7ID_vec[ii] = genre7ID
    rating_vec[ii] = 0
    ii += 1
    lastUserID = userID
    # add dictionary to store how reccomended albums or tracks are across all users, maybe? need to get album statistics overall need to see how user rates

    if ii == 6:
        while Trainline:
            arr_train = Trainline.strip().split('|')
            trainUserID = arr_train[0]
            trainItemID = arr_train[1]
            trainRating = arr_train[2]
            Trainline = fTrain.readline()

            if trainUserID < userID:
                continue
            if trainUserID == userID:
                for nn in range(6):
                    if trainItemID == albumID_vec[nn]:
                        #use if else statements to possibly adjust weights based on rating
                        if int(trainRating) >= 90:
                            user_rating_inTrain[nn, 0] = trainRating
                        else:
                            user_rating_inTrain[nn, 0] = trainRating
                        #user_rating_inTrain[nn, 0] = trainRating
                    if trainItemID == artistID_vec[nn]:
                        if int(trainRating) >= 90:
                            user_rating_inTrain[nn, 1] = trainRating
                        else:
                            user_rating_inTrain[nn, 1] = trainRating
                        #user_rating_inTrain[nn, 1] = trainRating
                    if trainItemID == genre1ID_vec[nn]:
                        if int(trainRating) >= 90:
                            user_rating_inTrain[nn, 2] = trainRating
                        else:
                            user_rating_inTrain[nn, 2] = trainRating
                        #user_rating_inTrain[nn, 2] = trainRating
                    if trainItemID == genre2ID_vec[nn]:
                        if int(trainRating) >= 90:
                            user_rating_inTrain[nn, 3] = trainRating
                        else:
                            user_rating_inTrain[nn, 3] = trainRating
                        #user_rating_inTrain[nn, 3] = trainRating
                    if trainItemID == genre3ID_vec[nn]:
                        if int(trainRating) >= 90:
                            user_rating_inTrain[nn, 4] = trainRating
                        else:
                            user_rating_inTrain[nn, 4] = trainRating
                        #user_rating_inTrain[nn, 4] = trainRating
                    if trainItemID == genre4ID_vec[nn]:
                        #user_rating_inTrain[nn, 5] = trainRating
                        if int(trainRating) >= 90:
                            user_rating_inTrain[nn, 5] = trainRating
                        else:
                            user_rating_inTrain[nn, 5] = trainRating
                    if trainItemID == genre5ID_vec[nn]:
                        #user_rating_inTrain[nn, 6] = trainRating
                        if int(trainRating) >= 90:
                            user_rating_inTrain[nn, 6] = trainRating
                        else:
                            user_rating_inTrain[nn, 6] = trainRating
                    if trainItemID == genre6ID_vec[nn]:
                        #user_rating_inTrain[nn, 7] = trainRating
                        if int(trainRating) >= 90:
                            user_rating_inTrain[nn, 7] = trainRating
                        else:
                            user_rating_inTrain[nn, 7] = trainRating
                    if trainItemID == genre7ID_vec[nn]:
                        #user_rating_inTrain[nn, 8] = trainRating
                        if int(trainRating) >= 90:
                            user_rating_inTrain[nn, 8] = trainRating
                        else:
                            user_rating_inTrain[nn, 8] = trainRating
            if trainUserID > userID:
                number_rated_genres = 0
                max_genre_score = 0
                min_genre_score = 0
                sum_genre = 0
                average_genre = 0
                variance_genre = 0
                range_genre = 0
                for nn in range(6):
                    for i in range(2,9):
                        genre_vec[i-2] = user_rating_inTrain[nn, i]
                        if user_rating_inTrain[nn,i] != 0:
                            number_rated_genres += 1
                    max_genre_score = max(genre_vec)
                    min_genre_score = min(genre_vec)
                    range_genre = max_genre_score - min_genre_score
                    """
                    if max_genre_score >= 90:
                        max_genre_score *= 2
                    if max_genre_score <= 70:
                        max_genre_score /= 2
                    if min_genre_score >= 80:
                        min_genre_score *= 2
                    if min_genre_score <= 70:
                        min_genre_score /= 2
                    """
                    sum_genre = sum(genre_vec)
                    if number_rated_genres == 0:
                        average_genre = 0
                    else:
                        average_genre = sum_genre/number_rated_genres
                    variance_genre = numpy.var(genre_vec)
                    # more features
                    try:
                        track_df = df_train.loc[df_train[0]==int(trackID)].reset_index()
                    except:
                        track_df = []
                    average_track = 0 # average track score 
                    num_100_track = 0 # number of 100 ratings
                    num_90_track = 0 # number of 90 ratings
                    num_80_track = 0 # number of 80 ratings
                    num_70_track = 0 # number of 70 ratings
                    num_60_track = 0 # number of 60 ratings
                    num_50_track = 0 # number of 50 ratings
                    sum_track = 0 # sum of track ratings
                    variance_track = 0 # variance of track ratings
                    num_rated_track = 0 # number of ratings given to track
                    track_values = []
                    for i in range(len(track_df)):
                        #if (track_df[0]==int(trackID)) != []:
                            value = track_df[2][i]
                            track_values.append(value)
                            if value == 100:
                                num_100_track += 1
                            elif value == 90:
                                num_90_track += 1
                            elif value == 80:
                                num_80_track += 1
                            elif value == 70:
                                num_70_track += 1
                            elif value == 60:
                                num_60_track += 1
                            elif value == 50:
                                num_50_track += 1
                            else:
                                continue
                    num_rated_track = len(track_df)
                    sum_track = sum(track_values)
                    try:
                        average_track = sum_track/num_rated_track
                    except:
                        average_track = 0
                    variance_track = numpy.var(track_values)
                    try:
                        album_df = df_train.loc[df_train[0]==int(albumID)].reset_index()
                    except:
                        album_df = []
                    average_album = 0 # average album score
                    num_100_album = 0 # number of 100 ratings
                    num_90_album = 0 # number of 90 ratings
                    num_80_album = 0 # number of 80 ratings
                    num_70_album = 0 # number of 70 ratings
                    num_60_album = 0 # number of 60 ratings
                    num_50_album = 0 # number of 50 ratings
                    sum_album = 0 # sum of album ratings
                    variance_album = 0 # variance of album ratings
                    num_rated_album = 0 # number of ratings given to album
                    album_values = []
                    for i in range(len(album_df)):
                        #if (album_df[0]==int(albumID)) != []:
                            value = album_df[2][i]
                            album_values.append(value)
                            if value == 100:
                                num_100_album += 1
                            elif value == 90:
                                num_90_album += 1
                            elif value == 80:
                                num_80_album += 1
                            elif value == 70:
                                num_70_album += 1
                            elif value == 60:
                                num_60_album += 1
                            elif value == 50:
                                num_50_album += 1
                            else:
                                continue
                    num_rated_album = len(album_df)
                    sum_album = sum(album_values)
                    try:
                        average_album = sum_album/num_rated_album
                    except:
                        average_album = 0
                    variance_album = numpy.var(album_values)
                    try:
                        artist_df = df_train.loc[df_train[0]==int(artistID)].reset_index()
                    except:
                        artist_df = []
                    average_artist = 0 # average artist score
                    num_100_artist = 0 # number of 100 ratings
                    num_90_artist = 0 # number of 90 ratings
                    num_80_artist = 0 # number of 80 ratings
                    num_70_artist = 0 # number of 70 ratings
                    num_60_artist = 0 # number of 60 ratings
                    num_50_artist = 0 # number of 50 ratings
                    sum_artist = 0 # sum of artist ratings
                    variance_artist = 0 # variance of artist ratings
                    num_rated_artist = 0 # number of ratings given to artist
                    artist_values = []
                    for i in range(len(artist_df)):
                        #if (artist_df[0]==int(artistID)) != []:
                            value = artist_df[2][i]
                            artist_values.append(value)
                            if value == 100:
                                num_100_artist += 1
                            elif value == 90:
                                num_90_artist += 1
                            elif value == 80:
                                num_80_artist += 1
                            elif value == 70:
                                num_70_artist += 1
                            elif value == 60:
                                num_60_artist += 1
                            elif value == 50:
                                num_50_artist += 1
                            else:
                                continue
                    num_rated_artist = len(artist_df)
                    sum_artist = sum(artist_values)
                    try:
                        average_artist = sum_artist/num_rated_artist
                    except:
                        average_artist = 0
                    variance_artist = numpy.var(artist_values)
                    user_rating_inTrain[nn, 9] = number_rated_genres
                    user_rating_inTrain[nn, 10] = max_genre_score
                    user_rating_inTrain[nn, 11] = min_genre_score
                    user_rating_inTrain[nn, 12] = sum_genre
                    user_rating_inTrain[nn, 13] = average_genre
                    user_rating_inTrain[nn, 14] = variance_genre
                    user_rating_inTrain[nn, 15] = range_genre
                    user_rating_inTrain[nn, 16] = average_track
                    user_rating_inTrain[nn, 17] = num_100_track
                    user_rating_inTrain[nn, 18] = num_90_track
                    user_rating_inTrain[nn, 19] = num_80_track
                    user_rating_inTrain[nn, 20] = num_70_track
                    user_rating_inTrain[nn, 21] = num_60_track
                    user_rating_inTrain[nn, 22] = num_50_track
                    user_rating_inTrain[nn, 23] = sum_track
                    user_rating_inTrain[nn, 24] = variance_track
                    user_rating_inTrain[nn, 25] = num_rated_track
                    user_rating_inTrain[nn, 26] = average_album
                    user_rating_inTrain[nn, 27] = num_100_album
                    user_rating_inTrain[nn, 28] = num_90_album
                    user_rating_inTrain[nn, 29] = num_80_album
                    user_rating_inTrain[nn, 30] = num_70_album
                    user_rating_inTrain[nn, 31] = num_60_album
                    user_rating_inTrain[nn, 32] = num_50_album
                    user_rating_inTrain[nn, 33] = sum_album
                    user_rating_inTrain[nn, 34] = variance_album
                    user_rating_inTrain[nn, 35] = num_rated_album
                    user_rating_inTrain[nn, 36] = average_artist
                    user_rating_inTrain[nn, 37] = num_100_artist
                    user_rating_inTrain[nn, 38] = num_90_artist
                    user_rating_inTrain[nn, 39] = num_80_artist
                    user_rating_inTrain[nn, 40] = num_70_artist
                    user_rating_inTrain[nn, 41] = num_60_artist
                    user_rating_inTrain[nn, 42] = num_50_artist
                    user_rating_inTrain[nn, 43] = sum_artist
                    user_rating_inTrain[nn, 44] = variance_artist
                    user_rating_inTrain[nn, 45] = num_rated_artist
                    # copy below line with weights to rating_vec to make it easier to see all of the code
                    # + number_rated_genres + max_genre_score + min_genre_score + sum_genre + average_genre + variance_genre
                    # rating_vec[nn] stores the scores that we base the rating on modify the below line with weights or other features to improve score
                    features = 45
                    rating_vec[nn] = 0
                    for i in range(46):
                        rating_vec[nn] += user_rating_inTrain[nn,i]
                    #rating_vec[nn] = user_rating_inTrain[nn,0] + user_rating_inTrain[nn,1] + user_rating_inTrain[nn,2] + user_rating_inTrain[nn,3] + user_rating_inTrain[nn,4] + user_rating_inTrain[nn,5] + user_rating_inTrain[nn,6] + user_rating_inTrain[nn,7] + user_rating_inTrain[nn,8] + number_rated_genres + max_genre_score + min_genre_score + sum_genre + average_genre + variance_genre + range_genre + user_rating_inTrain[nn,16] + user_rating_inTrain[nn,17] + user_rating_inTrain[nn,18] + user_rating_inTrain[nn,19] + user_rating_inTrain[nn,20] + user_rating_inTrain[nn,21] + user_rating_inTrain[nn,22] + user_rating_inTrain[nn,23] + user_rating_inTrain[nn,24] +  +
                    #outStr=str(userID) + '|' + str(trackID_vec[nn])+ '|' + str(user_rating_inTrain[nn,0]) + '|' + str(user_rating_inTrain[nn, 1]) + '|' + str(user_rating_inTrain[nn, 2]) + '|' + str(user_rating_inTrain[nn, 3]) + '|' + str(user_rating_inTrain[nn, 4]) + '|' + str(user_rating_inTrain[nn, 5]) + '|' + str(user_rating_inTrain[nn, 6]) + '|' + str(user_rating_inTrain[nn, 7]) + '|' + str(user_rating_inTrain[nn, 8]) + '|' + str(number_rated_genres) + '|' + str(max_genre_score) + '|' + str(min_genre_score) + '|' + str(sum_genre) + '|' + str(average_genre) + '|' + str(variance_genre) + '|' + str(range_genre)
                    outStr=str(userID) + '|' + str(trackID_vec[nn])+ '|'
                    for i in range(46):
                        outStr = outStr + str(user_rating_inTrain[nn,i]) + '|'
                    outStr = outStr + '|' + str(rating_vec[nn]) # to make sure rating is at end of string
                    fOut_complete.write(outStr + '\n')
                    # if statment used to segment PCA implementation code
                    """
                    if nn == 5:
                        scaling = StandardScaler()
                        scaling.fit(user_rating_inTrain)
                        scaled_data = scaling.transform(user_rating_inTrain)
                        pca = PCA(n_components=3)
                        pca.fit(scaled_data)
                        pca_user_rating_inTrain = pca.transform(scaled_data)
                        #overwrite rating_vec for now
                        for i in range(6):
                            # weight control for this method
                            user_rating_inTrain[i, 0] = user_rating_inTrain[i, 0]*50 # album 
                            user_rating_inTrain[i, 1] = user_rating_inTrain[i, 1]*50 # artist
                            user_rating_inTrain[i, 2] = user_rating_inTrain[i, 2]*1 # genre1
                            user_rating_inTrain[i, 3] = user_rating_inTrain[i, 3]*1 # genre2
                            user_rating_inTrain[i, 4] = user_rating_inTrain[i, 4]*1 # genre3
                            user_rating_inTrain[i, 5] = user_rating_inTrain[i, 5]*1 # genre4
                            user_rating_inTrain[i, 6] = user_rating_inTrain[i, 6]*1 # genre5
                            user_rating_inTrain[i, 7] = user_rating_inTrain[i, 7]*1 # genre6
                            user_rating_inTrain[i, 8] = user_rating_inTrain[i, 8]*1 # genre7
                            user_rating_inTrain[i, 9] = user_rating_inTrain[i, 9]*10 # number_rated_genres
                            user_rating_inTrain[i, 10] = user_rating_inTrain[i, 10]*1.75 # max_genre_score
                            user_rating_inTrain[i, 11] = user_rating_inTrain[i, 11]*1 # min_genre_score
                            user_rating_inTrain[i, 12] = user_rating_inTrain[i, 12]*1 # sum_genre
                            user_rating_inTrain[i, 13] = user_rating_inTrain[i, 13]*1 # average_genre
                            user_rating_inTrain[i, 14] = user_rating_inTrain[i, 14]*1 # variance_genre
                            user_rating_inTrain[i, 15] = user_rating_inTrain[i, 15]*1 # range_genre
                            rating_vec[i] = user_rating_inTrain[i].sum()
                    """
                    if nn == 5:
                        rating_vec_sorted = list(reversed(sorted(rating_vec)))
                        reccomended = rating_vec_sorted[0:3]
                        reccomend_count = 0
                        for i in range(6):
                            if (rating_vec[i] in reccomended) and reccomend_count < 3:
                                rating_vec[i] = 1
                                reccomend_count += 1
                            else:
                                rating_vec[i] = 0
                        
                for nn in range(6):
                    csv_writer.writerow([f"{userID}_{trackID_vec[nn]}", int(rating_vec[nn])])
                break

fTest.close()
fTrain.close()
fOut_complete.close()
fOut_submission.close()
