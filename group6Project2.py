from tkinter import *
import math
import pandas as pd
import matplotlib.pyplot as plt


class MainPage:
    def __init__(self):

        window = Tk()
        window.title("Group six (6) project")
        window.geometry("900x500")

        df = pd.read_csv('movies_metadata.csv')
        #thirdmovie = df.iloc[1]
        # print(thirdmovie)

        # empty list to add all datas in the csv file
        data = []

        # added all the data in the csv file to the data array
        for i in df.iloc:
            data.append(i)
        # print(data)
        # print(data[0])

        # empty array to add all data genres with their respective counts
        dataGenreswithCount = []

        # empty array to add all the counts for totalling
        dataCounts = []
        for i in data:
            # empty array to add each genre with its respective count
            dataEachMovieGenreswithCount = []
            # adding each genre to the dataEachMovieGenreswithCount list
            dataEachMovieGenreswithCount.append(i.genres)
            # adding each count to the dataEachMovieGenreswithCount list
            dataEachMovieGenreswithCount.append(i.vote_count)
            # adding all dataEachMovieGenreswithCount lists to the dataGenreswithCount list
            dataGenreswithCount.append(dataEachMovieGenreswithCount)

            # adding each count to the dataCounts Array
            dataCounts.append(i.vote_count)

        # print(dataGenreswithCount[1][0])
        # print(dataGenreswithCount)

        # empty lists to add all genre counts
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

        # empty array to add all genres total count
        genresTotalCount = []

        # empty array to add all genres total count in degrees
        self.genresTotalCountsInDegrees = []

        # searching through the dataGenreswithCount array to see which contains the adventure genre
        # and getting the count of the genre with 'dataGenreswithCount[i][1]'
        # and adding all the counts to the adventure genre list
        for i in range(len(dataGenreswithCount)):
            # print(dataGenreswithCount[i][0])
            if 'Adventure' in dataGenreswithCount[i][0]:
                # print(dataGenreswithCount[i][1])
                adventureCountArray.append(dataGenreswithCount[i][1])
        # print(adventureCountArray)

        # sum of all counts of adventure movies
        adventureCountTotal = sum(adventureCountArray)
        # print(adventureCountTotal)
        genresTotalCount.append(adventureCountTotal)

        # repeating the same process for all the other genres

        for i in range(len(dataGenreswithCount)):
            if 'Romance' in dataGenreswithCount[i][0]:
                romanticCountArray.append(dataGenreswithCount[i][1])

        romanticCountTotal = sum(romanticCountArray)
        # print(romanticCountTotal)
        genresTotalCount.append(romanticCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Thriller' in dataGenreswithCount[i][0]:
                thrillerCountArray.append(dataGenreswithCount[i][1])

        # the sum function is returning nan so I'm creating my own sum loop
        # I checked if any value in the list is nan, then i skipped the value with the 'continue' keyword
        thrillerCountTotal = 0
        for i in thrillerCountArray:
            if math.isnan(i):
                continue
            thrillerCountTotal += i
        # print(thrillerCountTotal)
        genresTotalCount.append(thrillerCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Drama' in dataGenreswithCount[i][0]:
                dramaCountArray.append(dataGenreswithCount[i][1])

        # the sum function is returning nan so I'm creating my own sum loop
        # I checked if any value in the list is nan, then i skipped the value with the 'continue' keyword
        dramaCountTotal = 0
        for i in dramaCountArray:
            if math.isnan(i):
                continue
            dramaCountTotal += i
        # print(dramaCountTotal)
        genresTotalCount.append(dramaCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Fantasy' in dataGenreswithCount[i][0]:
                fantasyCountArray.append(dataGenreswithCount[i][1])

        fantasyCountTotal = sum(fantasyCountArray)
        # print(fantasyCountTotal)
        genresTotalCount.append(fantasyCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Family' in dataGenreswithCount[i][0]:
                familyCountArray.append(dataGenreswithCount[i][1])

        familyCountTotal = sum(familyCountArray)
        # print(familyCountTotal)
        genresTotalCount.append(familyCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Animation' in dataGenreswithCount[i][0]:
                animationCountArray.append(dataGenreswithCount[i][1])

        # the sum function is returning nan so I'm creating my own sum loop
        # I checked if any value in the list is nan, then i skipped the value with the 'continue' keyword
        animationCountTotal = 0
        for i in animationCountArray:
            if math.isnan(i):
                continue
            animationCountTotal += i
        # print(animationCountTotal)
        genresTotalCount.append(animationCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Comedy' in dataGenreswithCount[i][0]:
                comedyCountArray.append(dataGenreswithCount[i][1])

        comedyCountTotal = sum(comedyCountArray)
        # print(comedyCountTotal)
        genresTotalCount.append(comedyCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Action' in dataGenreswithCount[i][0]:
                actionCountArray.append(dataGenreswithCount[i][1])

        # the sum function is returning nan so I'm creating my own sum loop
        # I checked if any value in the list is nan, then i skipped the value with the 'continue' keyword
        actionCountTotal = 0
        for i in actionCountArray:
            if math.isnan(i):
                continue
            actionCountTotal += i
        # print(actionCountTotal)
        genresTotalCount.append(actionCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Crime' in dataGenreswithCount[i][0]:
                crimeCountArray.append(dataGenreswithCount[i][1])

        crimeCountTotal = sum(crimeCountArray)
        # print(crimeCountTotal)
        genresTotalCount.append(crimeCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Horror' in dataGenreswithCount[i][0]:
                horrorCountArray.append(dataGenreswithCount[i][1])

        # the sum function is returning nan so I'm creating my own sum loop
        # I checked if any value in the list is nan, then i skipped the value with the 'continue' keyword
        horrorCountTotal = 0
        for i in horrorCountArray:
            if math.isnan(i):
                continue
            horrorCountTotal += i
        # print(horrorCountTotal)
        genresTotalCount.append(horrorCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'History' in dataGenreswithCount[i][0]:
                historyCountArray.append(dataGenreswithCount[i][1])

        historyCountTotal = sum(historyCountArray)
        # print(historyCountTotal)
        genresTotalCount.append(historyCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Science Fiction' in dataGenreswithCount[i][0]:
                scienceFictionCountArray.append(dataGenreswithCount[i][1])

        # the sum function is returning nan so I'm creating my own sum loop
        # I checked if any value in the list is nan, then i skipped the value with the 'continue' keyword
        scienceFictionCountTotal = 0
        for i in scienceFictionCountArray:
            if math.isnan(i):
                continue
            scienceFictionCountTotal += i
        # print(scienceFictionCountTotal)
        genresTotalCount.append(scienceFictionCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Mystery' in dataGenreswithCount[i][0]:
                mysteryCountArray.append(dataGenreswithCount[i][1])

        mysteryCountTotal = sum(mysteryCountArray)
        # print(mysteryCountTotal)
        genresTotalCount.append(mysteryCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Documentary' in dataGenreswithCount[i][0]:
                documentaryCountArray.append(dataGenreswithCount[i][1])

        documentaryCountTotal = sum(documentaryCountArray)
        # print(documentaryCountTotal)
        genresTotalCount.append(documentaryCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'War' in dataGenreswithCount[i][0]:
                warCountArray.append(dataGenreswithCount[i][1])

        warCountTotal = sum(warCountArray)
        # print(warCountTotal)
        genresTotalCount.append(warCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Foreign' in dataGenreswithCount[i][0]:
                foreignCountArray.append(dataGenreswithCount[i][1])

        foreignCountTotal = sum(foreignCountArray)
        # print(foreignCountTotal)
        genresTotalCount.append(foreignCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Music' in dataGenreswithCount[i][0]:
                musicCountArray.append(dataGenreswithCount[i][1])

        musicCountTotal = sum(musicCountArray)
        # print(musicCountTotal)
        genresTotalCount.append(musicCountTotal)

        for i in range(len(dataGenreswithCount)):
            if 'Western' in dataGenreswithCount[i][0]:
                westernCountArray.append(dataGenreswithCount[i][1])

        westernCountTotal = sum(westernCountArray)
        # print(westernCountTotal)
        genresTotalCount.append(westernCountTotal)

        # finding the sum of all the counts
        totalCounts = sum(genresTotalCount)

        # converting all total genres to degrees and apending it to the empty self.genresTotalCountsInDegrees array
        for i in genresTotalCount:
            degrees = round(i / totalCounts * 360, 1)
            self.genresTotalCountsInDegrees.append(degrees)
        # print(genresTotalCount)
        # print(self.genresTotalCountsInDegrees)
        # print(sum(self.genresTotalCountsInDegrees))

        self.label = Label(text='Movies genre')
        self.button = Button(text='Show pie chart', command=self.showGraph)
        self.button.pack(side=TOP, anchor=CENTER)

        window.mainloop()


    def showGraph(self):
            # plotting the graph
            # Data to plot
            labels = 'Adventure', 'Romance', 'Thriller', 'Drama', 'Fantasy', 'Family', 'Animation', 'Comedy', 'Action', 'Crime', 'Horror', 'History', 'Science Fiction', 'Mystery', 'Documentary',  'War', 'Foreign', 'Music', 'Western'

            sizes = self.genresTotalCountsInDegrees
            colors = ['gold', 'yellowgreen', 'lightcoral', 'green', 'yellow', 'brown', 'purple', 'blue', 'red',
                  'pink', 'lime', 'magenta', 'orange', 'aquamarine', 'yellowgreen', 'coral', 'crimson', 'yellow', 'cyan']
            explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0, 0.1,
                   1.0, 0.2, 1.0, 0.3, 0.2)  # explode 1st slice

            # Plot
            pie = plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                      autopct='%1.1f%%', shadow=False, startangle=140)
            plt.legend(pie[0], labels, loc="upper right")

            plt.axis('equal')
            plt.show()

MainPage()
