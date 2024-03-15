import pandas as pd

# Initialize an empty dictionary to store user ratings
user_ratings = {}

# Counter for tracking the number of users processed
user_count = 0

# Read the training set. Set file_path to location of the training data
with open("trainItem2.txt", "r") as file:
    for line in file:
        # Split the line into user_id and the number of ratings
        if "|" in line:
            user_id, num_ratings = line.strip().split("|")
            num_ratings = int(num_ratings)
            user_ratings[user_id] = {}
            continue

        # Split each line into item_id and item_rating
        item_id, item_rating = line.strip().split("\t")
        item_id = int(item_id)
        item_rating = int(item_rating)
        
        # Store the rating in the dictionary
        user_ratings[user_id][item_id] = item_rating
        
        # Check if we have processed data for the first 3 users --- for testing purposes
        # if len(user_ratings) == 3 and len(user_ratings["199810"]) == 140:
        #     break

# Convert the dictionary into a DataFrame
df_sparse_matrix = pd.DataFrame.from_dict(user_ratings, orient='index')

# Fill missing values with zeros
df_sparse_matrix = df_sparse_matrix.fillna(0)

# Save the DataFrame to a CSV file
df_sparse_matrix.to_csv("sparse_matrix.csv")

print("Size of the DataFrame: ", df_sparse_matrix.shape)

# Print confirmation message
print("Sparse matrix saved to sparse_matrix.csv")





####################-------------------------------------##########################################

#####          Code below is for doing a batch approach in a Google Colab Notebook             ####

####################-------------------------------------##########################################
# from google.colab import drive
# drive.mount('/content/drive')
# import pandas as pd
# import gc

# # Function to process a batch of data
# def process_batch(file_path, batch_size, output_file):
#     with open(file_path, "r") as file:
#         # Initialize an empty dictionary to store user ratings
#         user_ratings = {}

#         # Read the training set in batches
#         while True:
#             # Read data for a batch
#             for _ in range(batch_size):
#                 # Read the next line
#                 line = file.readline().strip()

#                 # If line is empty, exit loop
#                 if not line:
#                     break

#                 # Split the line into user_id and the number of ratings
#                 if "|" in line:
#                     user_id, num_ratings = line.split("|")
#                     num_ratings = int(num_ratings)
#                     user_ratings[user_id] = {}
#                     continue

#                 # Split each line into item_id and item_rating
#                 item_id, item_rating = line.split("\t")
#                 item_id = int(item_id)
#                 item_rating = int(item_rating)

#                 # Store the rating in the dictionary
#                 user_ratings[user_id][item_id] = item_rating

#             # If no more lines, break the loop
#             if not line:
#                 break

#             # Convert the dictionary into a DataFrame
#             df_sparse_matrix = pd.DataFrame.from_dict(user_ratings, orient='index')

#             # Fill missing values with zeros
#             df_sparse_matrix = df_sparse_matrix.fillna(0)

#             # Save the DataFrame to a CSV file (append mode)
#             df_sparse_matrix.to_csv(output_file, mode='a', header=False)

#             # Clear memory
#             del df_sparse_matrix
#             gc.collect()

#         # Print confirmation message
#         print("Sparse matrix for all batches saved to", output_file)

# # Set the batch size
# batch_size = 1000

# # Set the file path
# file_path = "/content/drive/My Drive/CPE627-BigData/trainItem2.txt"

# # Set the output file path
# output_file = "/content/drive/My Drive/CPE627-BigData/sparse_matrix.csv"

# # Process the data in batches and append to the existing CSV file
# process_batch(file_path, batch_size, output_file)
