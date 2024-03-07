#!/usr/bin/env python

import numpy

dataDir='C:/Users/Marc D/OneDrive - stevens.edu/AAI 627/'
file_name_test=dataDir + 'testTrack_hierarchy.txt'
file_name_train=dataDir + 'trainIdx2_matrix.txt'
output_file= dataDir + 'output1.txt'

fTest= open(file_name_test, 'r')
fTrain=open(file_name_train, 'r')
Trainline= fTrain.readline()
fOut = open(output_file, 'w')

trackID_vec=[0]*6
albumID_vec=[0]*6
artistID_vec=[0]*6
genre1ID_vec=[0]*6
genre2ID_vec=[0]*6
genre3ID_vec=[0]*6
genre4ID_vec=[0]*6
genre5ID_vec=[0]*6
genre6ID_vec=[0]*6
lastUserID=-1

user_rating_inTrain=numpy.zeros(shape=(6,8)) # change shape from (6,3) to (6,8) to account for genres

for line in fTest:
        print("for loop")
        print("arr_test")
        arr_test=line.strip().split('|')
        print(arr_test)
        print("userID")
        userID= arr_test[0]
        print(userID)
        print("trackID")
        trackID= arr_test[1]
        print(trackID)
        print("albumID")
        albumID= arr_test[2]
        print(albumID)
        print("artistID")
        artistID=arr_test[3]
        print(artistID)
        try:
                genre1ID=arr_test[4]
        except:
                #genre1ID="None"
                genre1ID = 0
        #print("genre1ID " + genre1ID)
        print("genre1ID " + str(genre1ID))
        try:
                genre2ID=arr_test[5]
        except:
                #genre2ID="None"
                genre2ID = 0
        #print("genre2ID " + genre2ID)
        print("genre2ID " + str(genre2ID))
        try:
                genre3ID=arr_test[6]
        except:
                #genre3ID="None"
                genre3ID = 0
        #print("genre3ID " + genre3ID)
        print("genre1ID " + str(genre3ID))
        try:
                genre4ID=arr_test[7]
        except:
                #genre4ID="None"
                genre4ID = 0
        #print("genre4ID " + genre4ID)
        print("genre4ID " + str(genre4ID))
        try:
                genre5ID=arr_test[8]
        except:
                #genre5ID="None"
                genre5ID = 0
        #print("genre5ID " + genre5ID)
        print("genre5ID " + str(genre5ID))
        try:
                genre6ID=arr_test[9]
        except:
                #genre6ID="None"
                genre6ID = 0
        #print("genre6ID " + genre6ID)
        print("genre6ID " + str(genre6ID))
        
        print("Before if userID!= lastUserID:")
        if userID!= lastUserID:
                print("Inside if")
                ii=0
                print("ii")
                print(ii)
                print("user_raiting_inTrain")
                user_rating_inTrain=numpy.zeros(shape=(6,8))# change shape from (6,3) to (6,8) to account for genres
                print(user_rating_inTrain)

        print("trackID_vec[ii]")
        trackID_vec[ii]=trackID
        print(trackID_vec[ii])
        print("albumID_vec[ii]")
        albumID_vec[ii]=albumID
        print(albumID_vec[ii])
        print("artistID_vec[ii]")
        artistID_vec[ii]=artistID
        print(artistID_vec[ii])
        print("genre1ID_vec[ii]")
        genre1ID_vec[ii]=genre1ID
        print(genre1ID_vec[ii])
        print("genre2ID_vec[ii]")
        genre2ID_vec[ii]=genre2ID
        print(genre2ID_vec[ii])
        print("genre3ID_vec[ii]")
        genre3ID_vec[ii]=genre3ID
        print(genre3ID_vec[ii])
        print("genre4ID_vec[ii]")
        genre4ID_vec[ii]=genre4ID
        print(genre4ID_vec[ii])
        print("genre5ID_vec[ii]")
        genre5ID_vec[ii]=genre5ID
        print(genre5ID_vec[ii])
        print("genre6ID_vec[ii]")
        genre6ID_vec[ii]=genre6ID
        print(genre6ID_vec[ii])
        print("ii")
        ii=ii+1
        print(ii)
        print("lastUserID")
        lastUserID=userID
        print(lastUserID)
        print("Before if ii==6")

        if ii==6 :
                print("Inside if ii==6")
                while (Trainline):
                        print("Inside while loop")
                        print("Trainline " + str(Trainline))
                        arr_train = Trainline.strip().split('|')
                        print("arr_train " + str(arr_train))
                        trainUserID=arr_train[0]
                        print("trainUserID " + str(trainUserID))
                        trainItemID=arr_train[1]
                        print("trainItemID " + str(trainItemID))
                        trainRating=arr_train[2]
                        print("trainRaiting " + str(trainRating))
                        Trainline=fTrain.readline()
                        print("Trainline " + str(Trainline))
                        print("Before If statements")
                        if trainUserID< userID:
                                print("Inside if trainUserID< userID: ")
                                continue
                        if trainUserID== userID:
                                print("Inside if trainUserID== userID: ")
                                for nn in range(0, 6):
                                        print("for loop")
                                        print("nn " + str(nn))
                                        if trainItemID==albumID_vec[nn]:
                                                print("Inside if trainItemID==albumID_vec[nn]:")
                                                user_rating_inTrain[nn, 0]=trainRating
                                                print("user_rating_inTrain[nn,0] " + str(user_rating_inTrain[nn, 0]))
                                        if trainItemID==artistID_vec[nn]:
                                                print("Inside if trainItemID==artistID_vec[nn]:")
                                                user_rating_inTrain[nn, 1]=trainRating
                                                print("user_rating_inTrain[nn, 1] " + str(user_rating_inTrain[nn, 1]))
                                        if trainItemID==genre1ID_vec[nn]:
                                                print("Inside if trainItemID==genre1ID_vec[nn]:")
                                                user_rating_inTrain[nn, 2]=trainRating
                                                print("user_rating_inTrain[nn, 2] " + str(user_rating_inTrain[nn, 2]))
                                        if trainItemID==genre2ID_vec[nn]:
                                                print("Inside if trainItemID==genre2ID_vec[nn]:")
                                                user_rating_inTrain[nn, 3]=trainRating
                                                print("user_rating_inTrain[nn, 3] " + str(user_rating_inTrain[nn, 3]))
                                        if trainItemID==genre3ID_vec[nn]:
                                                print("Inside if trainItemID==genre3ID_vec[nn]:")
                                                user_rating_inTrain[nn, 4]=trainRating
                                                print("user_rating_inTrain[nn, 4] " + str(user_rating_inTrain[nn, 4]))
                                        if trainItemID==genre4ID_vec[nn]:
                                                print("Inside if trainItemID==genre4ID_vec[nn]:")
                                                user_rating_inTrain[nn, 5]=trainRating
                                                print("user_rating_inTrain[nn, 5] " + str(user_rating_inTrain[nn, 5]))
                                        if trainItemID==genre5ID_vec[nn]:
                                                print("Inside if trainItemID==genre5ID_vec[nn]:")
                                                user_rating_inTrain[nn, 6]=trainRating
                                                print("user_rating_inTrain[nn, 6] " + str(user_rating_inTrain[nn, 6]))
                                        if trainItemID==genre6ID_vec[nn]:
                                                print("Inside if trainItemID==genre6ID_vec[nn]:")
                                                user_rating_inTrain[nn, 7]=trainRating
                                                print("user_rating_inTrain[nn, 7] " + str(user_rating_inTrain[nn, 7]))
                                
                                        
                        if trainUserID> userID:
                                print("Inside trainUserID> userID:")
                                for nn in range(0, 6):
                                        print("for loop")
                                        print("nn " + str(nn))
                                        outStr=str(userID) + '|' + str(trackID_vec[nn])+ '|' + str(user_rating_inTrain[nn,0]) + '|' + str(user_rating_inTrain[nn, 1]) + '|' + str(user_rating_inTrain[nn, 2]) + '|' + str(user_rating_inTrain[nn, 3]) + '|' + str(user_rating_inTrain[nn, 4]) + '|' + str(user_rating_inTrain[nn, 5]) + '|' + str(user_rating_inTrain[nn, 6]) + '|' + str(user_rating_inTrain[nn, 7])
                                        print("outStr " + str(outStr))
                                        fOut.write(outStr + '\n')
                        break



fTest.close()
fTrain.close()
