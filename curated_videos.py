from video import Video
from create_page import create_page


class Movie(Video):
    def __init__(self, title, poster_url, trailer_url, director):
        super(Movie, self).__init__(title, poster_url, trailer_url)
        self.director = director


class TVShow(Video):
    def __init__(self, title, img, clip_url, season, episode):
        super(TVShow, self).__init__(title, img, clip_url)
        self.season = season
        self.episode = episode


after_hours = Movie(
    'After Hours', 
    'https://d32qys9a6wm9no.cloudfront.net/images/movies/poster/f2/f26bdcba3e7ea29ba3b9f8bc2555fefa_500x735.jpg',
    'https://www.youtube.com/watch?v=LQRawYZl-ls',
    'Martin Scorsese'
)

planes = Movie(
    'Planes, Trains & Automobiles',
    'http://www.joblo.com/posters/images/full/1987-planes-trains-and-automobiles-poster1.jpg',
    'https://www.youtube.com/watch?v=VWGqGHMO294',
    'John Hughes'
)

dr_phil = TVShow(
    'Dr. Phil',
    'https://pmcdeadline2.files.wordpress.com/2017/03/dr-phil-2.jpg',
    'https://www.youtube.com/watch?v=xldZvPdRUew',
    '9',
    '153'
)

page = create_page(after_hours, planes, dr_phil)
with open('index.html', 'w') as f:
    f.write(page)
