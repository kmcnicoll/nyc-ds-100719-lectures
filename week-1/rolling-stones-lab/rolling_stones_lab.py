#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 09:08:45 2019

@author: kylemcnicoll
"""




import csv

with open("data.csv") as f:
    reader= csv.DictReader(f)
   # roll_dict=[{k:v for k,v in row.items()} for row in reader]
    print(type(reader))
    roll_dict=[]
    #for row in reader:
    
    
def find_by_name(album_name):
    for item in roll_dict:
        if item["album"]==album_name:
            return item
        
    return "None"


        
def find_by_rank(rank):
    for item in roll_dict:
        if item["number"]==rank or int(item["number"]) == rank:
            return item
    return "None"


def find_by_year(year):
    year=str(year)
    release = []
    for item in songs_dict:
        if item["year"]== year:
            release.append(item)
    return release


def find_by_years(start,end):
    start= str (start)
    end= str (end)
    start= int(start)
    end= int(end)
    release= []
    period= list(range(start,end +1))
    for item in roll_dict:
        if int(item["year"]) in period:
            release.append(item)
    return release

def find_by_ranks(start,end):
    start= str (start)
    end= str (end)
    start= int(start)
    end= int(end)
    release = []
    period= list(range(start,end +1))
    for item in roll_dict:
        if int(item["number"]) in period:
            release.append(item)
    return release


def all_titles():
    titles = []
    for item in roll_dict:
        titles.append(item["album"])
    return titles


def all_artists():
    titles = []
    for item in roll_dict:
        titles.append(item["artist"])
    return titles


from collections import Counter

def most_albums():
    answer= []
    lst_artists = all_artists()
    counter_dict = Counter(lst_artists)

    lst_values = counter_dict.values()
    for index in range(len(lst_keys)):
        if int(lst_values[index])== max(lst_values):
            answer.append(lst_keys[index])
    return answer

#    maxVal = max(lst_values)
#    for k, v in counter_dict.items():
        

def most_popword():
    working= []
    answer = []
    for title in all_titles():
        working = working + title.split()
    lst_words = working
    counter_dict=Counter(lst_words)
    lst_values= list(counter_dict.values())
    lst_keys = list(counter_dict.keys())
    lst_values = list(counter_dict.values())
    for index in range(len(lst_keys)):
        if int(lst_values[index])== max(lst_values):
            answer.append(lst_keys[index])
    return answer
    

import matplotlib.pyplot as plt
x = [int(album['year']) for album in roll_dict]
x = sorted(x)
plt.hist(x,range=(1950,2020),bins=7)



#import pandas as pd
#        
#
#import matplotlib.pyplot as plt
#genres = [album["genre"] for album in roll_dict]
#parsed_genre=[]
#for genre in genres:
#    parsed_genre.append(genre.split(',')[0])
#pd.Series(parsed_genre).value_counts().plot('bar')       
#x = sorted(x)
#plt.hist( x, genre , bins = len(genre) )





text_file = open('top-500-songs.txt', 'r')
    # read each line of the text file
    # here is where you can print out the lines to your terminal and get an idea 
    # for how you might think about re-formatting the data
lines = text_file.readlines()

list_songs= []
for string in lines:
    string= string.split("\t")
    list_songs.append(string)
songs_dict=[]
for song in list_songs:
    songs_dict.append({"number":song[0], "name":song[1], "artist":song[2], "year":song[3]})
for item in songs_dict:
    if len(item["year"]) > 4:
        item["year"] = item["year"][:4]
        
        

#didnt realise there was a json file. edit this function when have time to do it properly
def album_with_most_songs():
    artist_count=[]
    album_count=[]
    answer=[]
    for item in songs_dict:
        artist_count.append(item["artist"])
        album_count.append(item["name"])
    artist_count=Counter(artist_count)
    album_count= Counter(album_count)
    high_artist=list(artist_count.values())
    hig_artistsname=list(artist_count.keys())
    high_albumname=list(album_count.keys())
    high_album=list(album_count.values())
    for index in range(len(artist_count)):
        if int(high_artist[index]) == max(high_artist):
            answer.append({"Highest Artist":hig_artistsname[index]})
    for index in range(len(artist_count)):
        if int(high_album[index])== max(high_album):
            answer.append({"Highest Album":high_albumname[index]})
        
    return answer
    
import json

file = open('track_data.json', 'r')
json_data = json.load(file)

print(json_data)
    
def albums_with_top_songs():
    albums=[]
    songs=[]
    for song in songs_dict:
        songs.append(song["name"])
    for longs in json_data:
        long = longs["tracks"]
        for song in long:
            if song in songs:
                albums.append(longs["album"])
    return albums


def songs_from_top_albums():
    songs=[]
    for item in json_data:
        bingo = item["album"]
        for albums in roll_dict[0:-1]:
            albums= albums["album"]
            if bingo in albums:
                songs.append(item['tracks'])
    return songs



    

        
    

