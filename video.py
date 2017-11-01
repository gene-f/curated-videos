from urllib.parse import urlsplit

class Video:

    youtube_domains = (
        'www.youtu.be',
        'www.youtube.com'
    )

    youtube_embed_url = 'https://www.youtube.com/embed/{}'

    def __init__(self, title, img, video_url):
        self.title = title
        self.img = img
        self.video_url = self.embed_url(video_url)

    def embed_url(self, video_url):
        split_url = urlsplit(video_url)
        if split_url.netloc in self.youtube_domains:
            if split_url.query:
                id = split_url.query[2:]
            else:
                id = split_url.path[1:]
            return self.youtube_embed_url.format(id)
        else:
            return ''
