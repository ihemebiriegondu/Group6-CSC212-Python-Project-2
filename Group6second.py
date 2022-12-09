import requests
from tkinter import *
import tkinter.messagebox
import webbrowser



class MainPage:
    def __init__(self):

        window = Tk()
        window.title("Group six (6) project")
        window.geometry("900x500")

            # set frame for the search field
        self.frame1 = Frame(window, bg='white')
        self.frame1.pack(fill="both", expand=True, ipady=40)

            #app info name
        topLabel = Label(self.frame1, text="Movie Search App", anchor='n', padx=20,
                        pady=30, bg='white', fg='#dd1717', font=('Arial Bold', 17), justify=CENTER)
        topLabel.pack()

            #mini frame for the input fields
        self.frame1b = Frame(self.frame1, bg='white')
        self.frame1b.pack(pady=20)

            #search input label
        searchValue = Label(self.frame1b, text="Enter movie name", anchor='w', padx=20,
                        pady=10, bg='white', fg='black', font=('Arial semibold', 13), justify=LEFT)
        searchValue.pack(anchor='w')

            #empty variable to store the name of the movie searched
        self.Movie_Name = StringVar()

            #search input, value of the input will the stored in the empty variable above
        self.searchEntry = Entry(self.frame1b, width=30, font=('Arial 15'), justify=LEFT, highlightthickness=2, 
            relief='groove', textvariable=self.Movie_Name)
        self.searchEntry.focus()
        self.searchEntry.config(highlightcolor='blue2',
                            highlightbackground='blue4')
        self.searchEntry.pack(ipadx=10, ipady=10, anchor='n', padx=20)

            #search button
        searchButton = Button(self.frame1b, text='Search', font=('Arial semibold', 13), relief='flat', bg='#ff4949', activebackground='#ff4949', activeforeground='white',fg='white', cursor="hand2",command=self.searchMovie)
        searchButton.pack(pady=15, padx=20,ipadx=30, ipady=10, anchor='e')


            #frame 2 for displaying the searched movie details
        self.frame2 = Frame(window, bg='white')

            #frame 2 informations

            #title of the second frame
        detailsFrameTitle = Label(self.frame2, text='Movie Details', anchor='n', padx=20,
                        pady=20, bg='white', fg='black', font=('Arial', 16), justify=CENTER)
        detailsFrameTitle.pack()

        self.frame2b = Frame(self.frame2, bg='white')
        self.frame2b.pack()

            #movie details
        self.movieTitle = Label(self.frame2b, text='Original Title: ', anchor='w', padx=20,
                        pady=15, bg='white', fg='black', font=('Arial semibold', 13), justify=LEFT, width=100)
        self.movieTitle.pack(anchor='w')

        self.movieOverviewTitle = Label(self.frame2b, text='Movie Overview: ', anchor='w', padx=20,
                        pady=10, bg='white', fg='black', font=('Arial semibold', 13), justify=LEFT)
        self.movieOverviewTitle.pack(anchor='w')

        self.movieOverview = Label(self.frame2b, text='', anchor='w', padx=30,
                        pady=15, bg='white', fg='black', font=('Arial semibold', 13), justify=LEFT, width=50)
        self.movieOverview.pack(anchor='w')

        self.movieGenresHeading = Label(self.frame2b, text='Genres: ', anchor='w', padx=20,
                        pady=10, bg='white', fg='black', font=('Arial semibold', 13), justify=LEFT)
        self.movieGenresHeading.pack(anchor='w')

                #creating new label for diplaying all the genres
        self.genreList = Label(self.frame2b, text='', font=('Arial 13'), padx=30, 
                bg='white', fg='black', justify=LEFT)
        self.genreList.pack(anchor=W)

        moviePosterTitle = Label(self.frame2b, text='Movie Poster: ', anchor='w', padx=20,
                        pady=10, bg='white', fg='black', font=('Arial semibold', 13), justify=LEFT)
        moviePosterTitle.pack(anchor=W)

                #label to add movie poster link
        self.movieposter = Label(self.frame2b, text='', anchor='w', padx=30,
                pady=0, bg='white', fg='blue', cursor='hand2', font=('Arial semibold', 13), justify=LEFT)
        self.movieposter.pack(anchor='w')

        movieHomepageTitle = Label(self.frame2b, text='Movie Homepage: ', anchor='w', padx=20,
                        pady=10, bg='white', fg='black', font=('Arial semibold', 13), justify=LEFT)
        movieHomepageTitle.pack(anchor=W)

                #label to add movie homepage link
        self.moviehomepage = Label(self.frame2b, text='', anchor='w', padx=30,
                pady=0, bg='white', fg='blue', cursor='hand2', font=('Arial semibold', 13), justify=LEFT)
        self.moviehomepage.pack(anchor='w')

        window.mainloop()



    def searchMovie(self):
            #getting the movie title inputted in the search field
        self.movie_Name = self.Movie_Name.get()

        if self.movie_Name == '':
            tkinter.messagebox.showerror(
                "Error", "Search field is empty!")
        else:
                #url for sending the get request
            URL = 'https://api.themoviedb.org/3/search/movie?api_key=2bb667341550fea3ae5c335a339c8ead&query='+self.movie_Name

                # sending get request and saving the response as response object
            r = requests.get(url=URL)

                # extracting data in json format
            data = r.json()
                #print(data)

                #assigning the results object from the data dictionary to a variable
            firstSearchResult = data['results']
                #print(firstSearchResult)
            movie_ID = str(firstSearchResult[0]['id'])

                #creating another get request to search the movie with its id instead of the name, so as to be able to get the genre list
            newURL = 'https://api.themoviedb.org/3/movie/'+movie_ID+'?api_key=2bb667341550fea3ae5c335a339c8ead&query'

                # sending get request and saving the response as response object
            newr = requests.get(url=newURL)

                # extracting data in json format
            newData = newr.json()
            print(newData)

                #getting informations from the json file (python dictionary)
            originalTitle = newData['original_title'].upper()
            genres = newData['genres']
            movieImageUrl = 'https://image.tmdb.org/t/p/w500/'+newData['poster_path']
            overview = newData['overview']
            movieHomepage = newData['homepage']

                #using the informations gotten

                #adding the original title of the movie to the 'movie title' label
            self.movieTitle['text'] += originalTitle

                #getting the genre's name from each dictionary and storing them in the genreArray variable
            genreArray = []
            for i in genres:
                #print(i)
                genreArray.append(i['name'])
            #print(genreArray)

            def addGenreToGenreList():
                genre = ''
                for i in range(len(genreArray)):
                    genre = genre + genreArray[i]+'\n'
                return genre

                # adding the texts to the genreList label created above
            self.genreList['text'] = addGenreToGenreList()

            
                #function for changing the movie image link into a clickable link
            def linkChange(url):
                webbrowser.open_new_tab(url)

                #adding the original title of the movie to the 'movie title' label
            self.movieposter['text'] = movieImageUrl
                #Create a Label to display the link
            self.movieposter.bind("<Button-1>", lambda e:
            linkChange(movieImageUrl))


                #adding the overview to the overview label
            self.movieOverview['text'] = overview


                #adding the homepage link to the homepage label
            self.moviehomepage['text'] = movieHomepage
                #Create a Label to display the link
            self.moviehomepage.bind("<Button-1>", lambda e:
            linkChange(movieHomepage))

                #clear input field
            self.searchEntry.delete(0, END)
            self.searchEntry.insert(0, '')

                #close the first frame and open the second
            self.frame2.pack(fill="both", expand=True, ipady=40)
            self.frame1.forget()
            


MainPage()
