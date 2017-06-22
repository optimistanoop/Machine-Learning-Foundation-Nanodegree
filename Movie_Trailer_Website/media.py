# Import python library webbrowser to open browser tab
import webbrowser


class Movie():
    """This Class holds movie data with a
    functionality to open trailer in default browser tab"""
    def __init__(self, title, poster_url, youtube_link):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_link

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
