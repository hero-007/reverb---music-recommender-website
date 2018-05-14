import pandas
from sklearn.cross_validation import train_test_split
import numpy as np 
import time
from sklearn.externals import joblib
from . import Recommenders
import os

def give_recommended_songs(user_index):
    # testing code here 
    filecsv = "C:\\Users\\HP\\Desktop\\combine.csv"
    song_df = pandas.read_csv(filecsv)
    # Creating a test and train data for recommender system
    train_data, test_data = train_test_split(song_df, test_size = 0.20, random_state=0)

    # Creating  a list of users and songs
    users = song_df['user_id'].unique()
    songs = song_df['song'].unique()

    # Class for an item similarity based personalized recommender system
    is_model = Recommenders.item_similarity_recommender_py()
    is_model.create(train_data, 'user_id', 'song')

    #Print the songs for the user in training data
    user_id = users[user_index]
    user_items = is_model.get_user_items(user_id)
    #Recommend songs for the user using personalized model

    # changes made from here #
    # original return is_model.recommend(user_id)
    recomend_df = is_model.recommend(user_id)
    recommended_songs = recomend_df['song'].tolist()
    return recommended_songs
