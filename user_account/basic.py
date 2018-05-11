import os 
from .models import Listener
import csv
from . import music

def give_me_song_list(user_name):
    cwd = os.getcwd()
    os.chdir('C:\\Users\\HP\\Desktop\\')
    songs = []
    try:
        user_id = Listener.objects.get(listener_name = user_name)
        user_src = user_id.listener_id
    except Listener.DoesNotExist:
        return songs
    with open('combine.csv', newline='',encoding='utf8') as csvfile:
        spamreader = csv.reader(csvfile)
        ctr = 0
        for row in spamreader:
            if ctr == 0:
                ctr +=1
                continue
            if str(row[1]) == user_src:
                songs.append(row[8])
    os.chdir(cwd)
    return songs

