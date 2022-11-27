from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
import csv

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
        #print(data)
        #print(data[0])
        
        #empty array to add all data genres with their respective counts
        dataGenreswithCount = []

        #empty array to add all the counts for totalling
        dataCounts = []
        for i in data:
            #empty array to add each genre with its respective count
            dataEachMovieGenreswithCount = []
            #adding each genre to the dataEachMovieGenreswithCount list
            dataEachMovieGenreswithCount.append(i.genres)
            #adding each count to the dataEachMovieGenreswithCount list
            dataEachMovieGenreswithCount.append(i.vote_count)
            #adding all dataEachMovieGenreswithCount lists to the dataGenreswithCount list
            dataGenreswithCount.append(dataEachMovieGenreswithCount)
            #adding each count to the dataCounts Array
            dataCounts.append(i.vote_count)
                        
        #print(dataGenreswithCount[1][0])
        #print(dataGenreswithCount)

        #finding the sum of all the counts
        totalCounts = sum(dataCounts)

        #empty lists to add all genre counts
        adventureCountArray = []
        romanticCountArray = []
        thrillerCountArray = []
        dramaCountArray = []
        fantasyCountArray = []
        familyCountArray = []
        animationCountArray = []
        comedyCountArray = []
        actionCountArray = []
        crimeCountArray = []
        horrorCountArray = []
        historyCountArray = []
        scienceFictionCountArray = []
        mysteryCountArray = []
        documentaryCountArray = []
        warCountArray = []
        foreignCountArray = []
        musicCountArray = []
        westernCountArray = []


        #searching through the dataGenreswithCount array to see which contains the adventure genre
        #and getting the count of the genre with 'dataGenreswithCount[i][1]'
        #and adding all the counts to the adventure genre list
        for i in range(len(dataGenreswithCount)):
            #print(dataGenreswithCount[i][0])
            if 'Adventure' in dataGenreswithCount[i][0]:
                #print(dataGenreswithCount[i][1])
                adventureCountArray.append(dataGenreswithCount[i][1])
        #print(adventureCountArray)

        #sum of all counts of adventure movies
        adventureCountTotal = sum(adventureCountArray)
        print(adventureCountTotal)


        #repeating the same process for all the other genres

        for i in range(len(dataGenreswithCount)):
            if 'Romance' in dataGenreswithCount[i][0]:
                romanticCountArray.append(dataGenreswithCount[i][1])

        romanticCountTotal = sum(romanticCountArray)
        print(romanticCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Thriller' in dataGenreswithCount[i][0]:
                thrillerCountArray.append(dataGenreswithCount[i][1])

        thrillerCountTotal = sum(thrillerCountArray)
        print(thrillerCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Drama' in dataGenreswithCount[i][0]:
                dramaCountArray.append(dataGenreswithCount[i][1])

        dramaCountTotal = sum(dramaCountArray)
        print(dramaCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Fantasy' in dataGenreswithCount[i][0]:
                fantasyCountArray.append(dataGenreswithCount[i][1])

        fantasyCountTotal = sum(fantasyCountArray)
        print(fantasyCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Family' in dataGenreswithCount[i][0]:
                familyCountArray.append(dataGenreswithCount[i][1])

        familyCountTotal = sum(familyCountArray)
        print(familyCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Animation' in dataGenreswithCount[i][0]:
                animationCountArray.append(dataGenreswithCount[i][1])

        print(animationCountArray)
        animationCountTotal = sum(animationCountArray)
        print(animationCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Comedy' in dataGenreswithCount[i][0]:
                comedyCountArray.append(dataGenreswithCount[i][1])

        comedyCountTotal = sum(comedyCountArray)
        print(comedyCountTotal)





MainPage()