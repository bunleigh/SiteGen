import unittest

from extract_markdown import *

class TestTextNode(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "this is text with a link to [bluesky](http://www.bluesky.com)"
        )
        self.assertListEqual([("bluesky", "http://www.bluesky.com")], matches)

    def test_extract_markdown_multiple_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another image](https://i.makeagif.com/media/3-20-2017/oKOK9-.gif)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("another image", "https://i.makeagif.com/media/3-20-2017/oKOK9-.gif")], matches)