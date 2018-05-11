import pandas
from sklearn.cross_validation import train_test_split
import numpy as np 
import time
from sklearn.externals import joblib
from . import Recommenders
import os

def give_recommended_songs(user_index):
    file1 = "C:\\Users\\HP\\Desktop\\My Implementation\\10000.txt"
    filecsv = "C:\\Users\\HP\\Desktop\\My Implementation\\song_data.csv"

    song_df_1 = pandas.read_table(file1,header=None)
    song_df_1.columns = ['user_id','song_id','listen_count']

    song_df_2 = pandas.read_csv(filecsv)

    song_df = pandas.merge(song_df_1,song_df_2.drop_duplicates(['song_id']), on="song_id", how="left")

    song_df = song_df.head(10000)
    song_df['song'] = song_df['title'].map(str)+" - "+song_df['artist_name']

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
