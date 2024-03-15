#!/usr/bin/env python

import csv
import numpy
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

dataDir='{ADD FILEPATH HERE}'
file_name_test='testTrack_hierarchy.txt'
file_name_train='trainIdx2_matrix.txt'
output_file1= 'output3.txt'
output_file2= 'output3.csv'

fTest = open(file_name_test, 'r')
fTrain = open(file_name_train, 'r')
Trainline = fTrain.readline()
fOut_complete = open(output_file1, 'w')
fOut_submission = open(output_file2, 'w')
header_complete = "UserID|TrackID|AlbumRating|ArtistRating|Genre1Rating|Genre2Rating|Genre3Rating|Genre4Rating|Genre5Rating|Genre6Rating|Genre7Rating|NumberRatedGenres|MaxGenreScore|MinGenreScore|SumGenreScores|AverageGenreScore|VarianceGenreScore|RatingValue\n"
header_submission = ["TrackID", "Predictor"]
fOut_complete.write(header_complete)
csv_writer = csv.writer(fOut_submission)
csv_writer.writerow(header_submission)

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

user_rating_inTrain = numpy.zeros(shape=(6,9)) # change shape from (6,3) to (6,15) to account for genres and other features 

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
        user_rating_inTrain = numpy.zeros(shape=(6,15)) # Reset for new user

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
                for nn in range(6):
                    for i in range(2,9):
                        genre_vec[i-2] = user_rating_inTrain[nn, i]
                        if user_rating_inTrain[nn,i] != 0:
                            number_rated_genres += 1
                    max_genre_score = max(genre_vec)
                    min_genre_score = min(genre_vec)
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
                    user_rating_inTrain[nn, 9] = number_rated_genres
                    user_rating_inTrain[nn, 10] = max_genre_score
                    user_rating_inTrain[nn, 11] = min_genre_score
                    user_rating_inTrain[nn, 12] = sum_genre
                    user_rating_inTrain[nn, 13] = average_genre
                    user_rating_inTrain[nn, 14] = variance_genre
                    # copy below line with weights to rating_vec to make it easier to see all of the code
                    # + number_rated_genres + max_genre_score + min_genre_score + sum_genre + average_genre + variance_genre
                    # rating_vec[nn] stores the scores that we base the rating on modify the below line with weights or other features to improve score
                    rating_vec[nn] = user_rating_inTrain[nn,0] + user_rating_inTrain[nn,1] + user_rating_inTrain[nn,2] + user_rating_inTrain[nn,3] + user_rating_inTrain[nn,4] + user_rating_inTrain[nn,5] + user_rating_inTrain[nn,6] + user_rating_inTrain[nn,7] + user_rating_inTrain[nn,8] + number_rated_genres + max_genre_score + min_genre_score + sum_genre + average_genre + variance_genre
                    outStr=str(userID) + '|' + str(trackID_vec[nn])+ '|' + str(user_rating_inTrain[nn,0]) + '|' + str(user_rating_inTrain[nn, 1]) + '|' + str(user_rating_inTrain[nn, 2]) + '|' + str(user_rating_inTrain[nn, 3]) + '|' + str(user_rating_inTrain[nn, 4]) + '|' + str(user_rating_inTrain[nn, 5]) + '|' + str(user_rating_inTrain[nn, 6]) + '|' + str(user_rating_inTrain[nn, 7]) + '|' + str(user_rating_inTrain[nn, 8]) + '|' + str(number_rated_genres) + '|' + str(max_genre_score) + '|' + str(min_genre_score) + '|' + str(sum_genre) + '|' + str(average_genre) + '|' + str(variance_genre)
                    outStr = outStr + '|' + str(rating_vec[nn]) # to make sure rating is at end of string
                    fOut_complete.write(outStr + '\n')
                    # if statment used to segment PCA implementation code
                    if nn == 5:
                        scaling = StandardScaler()
                        scaling.fit(user_rating_inTrain)
                        scaled_data = scaling.transform(user_rating_inTrain)
                        pca = PCA(n_components=3)
                        pca.fit(scaled_data)
                        pca_user_rating_inTrain = pca.transform(scaled_data)
                        #overwrite rating_vec for now
                        for i in range(6):
                            rating_vec[i] = user_rating_inTrain[i].sum()
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
