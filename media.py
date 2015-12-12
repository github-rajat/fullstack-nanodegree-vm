import webbrowser

class Movie():
  def __init__(self, movie_name, story, image_url, trailer_url):
    self.title = movie_name
    self.story_line = story
    self.poster_image_url = image_url
    self.trailer_youtube_url = trailer_url

  def show_trailer(self):
    webbrowser.open(self.youtube_url)
