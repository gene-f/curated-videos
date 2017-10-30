import unittest
import video
import create_page


class testVideo(unittest.TestCase):
    def test_create_Video(self):
        with self.assertRaises(AttributeError):
            v = video.Video()

        v = video.Video(title="movie", img="img", video_url="url")

    def test_Video_attributes(self):
        v = video.Video(title="movie", img="img", video_url="url")
        self.assertEqual(v.title, "movie")
        self.assertEqual(v.img, "img")
        self.assertEqual(v.video_url, "")

    def test_video_subclass(self):
        pass


class testCreatePage(unittest.TestCase):
    def test_add_videos(self):
        pass
    def test_group_videos_by_category(self):
        pass
    def test_create_entry(self):
        pass
    def test_create_section(self):
        pass
    def test_create_page(self):
        pass

if __name__ == '__main__':
    unittest.main()
