import webbrowser

class Movie():
    '''
    This class stores movie, this will help us define what elements does a movie will contain a know which elements has to have
    '''

    def __init__(self, movie_title, movie_storyline, 
				 poster_image, trailer_youtube):

	    self.title = movie_title
	    self.storyline = movie_storyline
	    self.poster_image_url = poster_image
	    self.trailer_youtube_url = trailer_youtube
	
	'''
    The def __init__ give the instruction that every time that a movie will be build it as has to have the elements
    we add self to indicate that the atributes that we are passing it will be for that move only 
    '''


	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

	'''
    Here we send the instruction to open a browser with the youtube url that set on the parameters we pass on every movie
    '''