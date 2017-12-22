class Video():
    '''
    Parent Class Object that stores Video related information.
    '''
    def __init__(self, title, box_art, poster_image_url, trailer_youtube_url):
        '''
        Initialize instance of class Video

        :param title: string
        :param box_art: string
        :param poster_image_url: string
        :param trailer_youtube_url: string
        '''
        self.title = title
        self.box_art = box_art
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        """
        Initializing instance for opening the youtube video

        :return: webbrowser to play trailer
        """
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class Movie(Video):
    '''
    Child Class Object that is inherited from Parent Class Object
    '''
    def __init__(self,title,box_art,poster_image_url,trailer_youtube_url,movie_hours):
        '''
        Initialize instance of class Movie

        :param title: string (from parent class)
        :param box_art: string (from parent class)
        :param poster_image_url: string (from parent class)
        :param trailer_youtube_url: string (from parent class)
        :param movie_hours: int
        '''
        Video.__init__(self,title,box_art,poster_image_url,trailer_youtube_url)
        self.movie_hours = movie_hours

    def show_trailer(self):
        '''
        Initializing instance for opening the youtube video

        :return: webbrowser to play trailer
        '''
        webbrowser.open(self.trailer_youtube_url)

class Tv(Video):
    '''
    Child Class Object that is inherited from Parent Class Object
    '''
    def __init__(self,title,box_art,poster_image_url,trailer_youtube_url,broadcaster):
        '''
        Initialize instance of class Tv

        :param title: string (from parent class)
        :param box_art: string (from parent class)
        :param poster_image_url: string (from parent class)
        :param trailer_youtube_url: string (from parent class)
        :param movie_hours: int
        '''
        Video.__init__(self,title,box_art,poster_image_url,trailer_youtube_url)
        self.broadcaster = broadcaster

    def show_trailer(self):
        '''
        Initializing instance for opening the youtube video

        :return: webbrowser to play trailer
        '''
        webbrowser.open(self.trailer_youtube_url)
