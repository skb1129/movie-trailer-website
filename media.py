import webbrowser


class Movie():
    """ This class stores the title, storyline, poster image url and trailer
    url of an instance movie and show_trailer() plays the trailer on a
    webbrowser.
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# This function plays the trailer on webbrowser.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
