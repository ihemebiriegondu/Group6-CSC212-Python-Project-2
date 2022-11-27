from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
import json

import pandas as pd


class MainPage:
    def __init__(self):
        df = pd.read_csv ('movies_metadata.csv')
        #thirdmovie = df.iloc[1]
        #print(thirdmovie)

        #empty list to add all datas in the csv file
        data = []

        #added all the data in the csv file to the data array
        for i in df.iloc:
            data.append(i)
        #print(data[0])
        
        #empty array to add all data genres with their respective counts
        dataGenreswithCount = []
        for i in data:
            #empty array to add each genre with its respective count
            dataEachMovieGenreswithCount = []
            #adding each genre to the dataEachMovieGenreswithCount list
            dataEachMovieGenreswithCount.append(i.genres)
            #adding each count to the dataEachMovieGenreswithCount list
            dataEachMovieGenreswithCount.append(i.vote_count)
            #adding all dataEachMovieGenreswithCount lists to the dataGenreswithCount list
            dataGenreswithCount.append(dataEachMovieGenreswithCount)
                        
        print(dataGenreswithCount[1])
        #print(dataGenreswithCount)




MainPage()