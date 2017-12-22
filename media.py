class Video():
    '''
    Parent Class Video that has 2 children Movie class and Tv class
    Attributes: title, box_art, poster_image_url, trailer_youtube_url
    '''
    def __init__(self, title, box_art, poster_image_url, trailer_youtube_url):
        self.title = title
        self.box_art = box_art
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class Movie(Video):
    '''
    Child class Movie that is inherited from Video class
    Attributes: title, box_art, poster_image_url, trailer_youtube_url, and its own movie_hours
    '''
    def __init__(self,title,box_art,poster_image_url,trailer_youtube_url,movie_hours):
        Video.__init__(self,title,box_art,poster_image_url,trailer_youtube_url)
        self.movie_hours = movie_hours

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class Tv(Video):
    '''
    Child class Tv that is inherited from Video class
    Attributes: title, box_art, poster_image_url, trailer_youtube_url and its own broadcaster
    '''
    def __init__(self,title,box_art,poster_image_url,trailer_youtube_url,broadcaster):
        Video.__init__(self,title,box_art,poster_image_url,trailer_youtube_url)
        self.broadcaster = broadcaster

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
