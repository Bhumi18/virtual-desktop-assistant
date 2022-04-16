import random
import os

music_dir = 'D:\\songs'
songs = os.listdir(music_dir)
print(songs)
num = random.randint(0,1)
print(num)
file_name = music_dir+'\\'+songs[num]
os.startfile(file_name)