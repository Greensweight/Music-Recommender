#!/usr/bin/env python

import numpy

file_name_test='testTrack_hierarchy.txt'
file_name_train='trainIdx2_matrix.txt'
output_file= 'output1.txt'

fTest = open(file_name_test, 'r')
fTrain = open(file_name_train, 'r')
Trainline = fTrain.readline()
fOut = open(output_file, 'w')

trackID_vec = [0]*6
albumID_vec = [0]*6
artistID_vec = [0]*6
genre1ID_vec = [0]*6
genre2ID_vec = [0]*6
genre3ID_vec = [0]*6
genre4ID_vec = [0]*6
genre5ID_vec = [0]*6
genre6ID_vec = [0]*6
lastUserID = -1

user_rating_inTrain = numpy.zeros(shape=(6,8)) # change shape from (6,3) to (6,8) to account for genres

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

    if userID != lastUserID:
        ii = 0
        user_rating_inTrain = numpy.zeros(shape=(6,8)) # Reset for new user

    trackID_vec[ii] = trackID
    albumID_vec[ii] = albumID
    artistID_vec[ii] = artistID
    genre1ID_vec[ii] = genre1ID
    genre2ID_vec[ii] = genre2ID
    genre3ID_vec[ii] = genre3ID
    genre4ID_vec[ii] = genre4ID
    genre5ID_vec[ii] = genre5ID
    genre6ID_vec[ii] = genre6ID
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
                        user_rating_inTrain[nn, 0] = trainRating
                    if trainItemID == artistID_vec[nn]:
                        user_rating_inTrain[nn, 1] = trainRating
                    if trainItemID == genre1ID_vec[nn]:
                        user_rating_inTrain[nn, 2] = trainRating
                    if trainItemID == genre2ID_vec[nn]:
                        user_rating_inTrain[nn, 3] = trainRating
                    if trainItemID == genre3ID_vec[nn]:
                        user_rating_inTrain[nn, 4] = trainRating
                    if trainItemID == genre4ID_vec[nn]:
                        user_rating_inTrain[nn, 5] = trainRating
                    if trainItemID == genre5ID_vec[nn]:
                        user_rating_inTrain[nn, 6] = trainRating
                    if trainItemID == genre6ID_vec[nn]:
                        user_rating_inTrain[nn, 7] = trainRating
            if trainUserID > userID:
                for nn in range(6):
                    outStr = f"{userID}|{trackID_vec[nn]}|{user_rating_inTrain[nn,0]}|{user_rating_inTrain[nn, 1]}|{user_rating_inTrain[nn, 2]}|{user_rating_inTrain[nn, 3]}|{user_rating_inTrain[nn, 4]}|{user_rating_inTrain[nn, 5]}|{user_rating_inTrain[nn, 6]}|{user_rating_inTrain[nn, 7]}"
                    fOut.write(outStr + '\n')
                break

fTest.close()
fTrain.close()
fOut.close()