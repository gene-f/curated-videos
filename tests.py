import unittest
import video
import create_page


class testVideo(unittest.TestCase):
    def test_create_Video(self):
        with self.assertRaises(TypeError):
            v = video.Video()
        with self.assertRaises(TypeError):
            v = video.Video(img="img", video_url="url")
        with self.assertRaises(TypeError):
            v = video.Video(title="movie", video_url="url")
        with self.assertRaises(TypeError):
            v = video.Video(title="movie", img="img")
        v = video.Video(title="movie", img="img", video_url="url")

    def test_Video_attributes(self):
        v = video.Video(title="movie", img="img", video_url="url")
        self.assertEqual(v.title, "movie")
        self.assertEqual(v.img, "img")
        self.assertEqual(v.video_url, "url")

    def test_Video_embed_url(self):
        v = video.Video(title="movie", img="img", video_url="url")
        embedded = v.embed_url()
        self.assertEqual(embedded, "")
        v = video.Video(
            title="movie",
            img="img",
            video_url="https://www.youtu.be/LQRawYZl-ls"
        )

        embedded = v.embed_url()
        self.assertEqual(
            embedded,
            "https://www.youtube.com/embed/LQRawYZl-ls"
        )

        v = video.Video(
            title="movie",
            img="img",
            video_url="https://www.youtube.com/watch?v=LQRawYZl-ls"
        )

        embedded = v.embed_url()
        self.assertEqual(
            embedded,
            "https://www.youtube.com/embed/LQRawYZl-ls"
        )

    def test_video_subclass(self):
        class Movie(video.Video):
            def __init__(self, title, poster, url, year, review):
                video.Video.__init__(self, title, poster, url)
                self.year = year
                self.review = review

        m = Movie(
            title="movie",
            poster="img",
            url="https://www.youtube.com/watch?v=LQRawYZl-ls",
            year=1985,
            review='*** out of ****'
        )

        embedded = m.embed_url()
        self.assertEqual(
            embedded,
            "https://www.youtube.com/embed/LQRawYZl-ls"
        )

class testCreatePage(unittest.TestCase):
    def test_group_videos_by_class(self):
        class MusicVideo(video.Video):
            def __init__(self, title, img, url, artist, album):
                video.Video.__init__(self, title, img, url)
                self.arist = artist
                self.album = album

        class TVShow(video.Video):
            def __init__(self, title, img, url, season):
                video.Video.__init__(self, title, img, url)
                self.season  = season

        music = MusicVideo('song1', 'albumcover1', 'url', 'artist', 'album')
        music2 = MusicVideo('song2', 'albumcvr', 'url', 'artist', 'album')
        show1 = TVShow('episode1', 'img', 'url', 'season1')
        show2 = TVShow('ep3', 'img', 'url', 'se3')
        result = create_page.group_by_type(music, show1, music2, show2)
        self.assertEqual(
            result,
            {MusicVideo:[music, music2], TVShow:[show1, show2]}
        )


if __name__ == '__main__':
    unittest.main()
