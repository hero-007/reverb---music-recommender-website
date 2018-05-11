from django.db import models

# Create your models here.
class Listener (models.Model):
    listener_id = models.CharField(max_length=100)
    listener_name = models.CharField(max_length=100)
    
    def __str__(self):
        return 'Listener Id : {} \n Listener Name : {}'.format(self.listener_id,self.listener_name)

    def listener_save(self):
        self.save()

class User_Id (models.Model):
    user_index = models.IntegerField(primary_key = True)
    user_id = models.CharField(max_length = 100)

    def user_id_save(self):
        self.save()

class Song (models.Model):
    song_number = models.IntegerField(primary_key=True)
    song_id = models.CharField(max_length=100)
    song_title = models.CharField(max_length=300)
    song_release = models.CharField(max_length=300)
    song_artist = models.CharField(max_length=200)
    song_year = models.IntegerField()

    def __str__(self):
        return 'Song : {} || Song ID : {}'.format(self.song_title,self.song_id)
    
    def save_song(self):
        self.save()
    
