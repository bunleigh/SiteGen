import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_noteq(self):
        node = TextNode("this is a text node", TextType.BOLD)
        node2 = TextNode("is this a text node?", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_mismatch(self):
        node = TextNode("this is a text node", TextType.PLAIN, "www.butt.com")
        node2 = TextNode("this is a text node", TextType.PLAIN)
        self.assertNotEqual(node, node2)


## split_nodes_delmiiter

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("this is a test with some **bold shite** in it", TextType.PLAIN)
        converted = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(converted, [
            TextNode("this is a test with some ", TextType.PLAIN),
            TextNode("bold shite", TextType.BOLD),
            TextNode(" in it", TextType.PLAIN)
            ])
        
    def test_split_nodes_delimiter_italic(self):
        node = TextNode("this is a test with some _italic faff_ in it", TextType.PLAIN)
        converted = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(converted, [
            TextNode("this is a test with some ", TextType.PLAIN),
            TextNode("italic faff", TextType.ITALIC),
            TextNode(" in it", TextType.PLAIN)
            ])
        
    def test_split_nodes_delimiter_code(self):
        node = TextNode("this is a test with some `code` in it", TextType.PLAIN)
        converted = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(converted, [
            TextNode("this is a test with some ", TextType.PLAIN),
            TextNode("code", TextType.CODE),
            TextNode(" in it", TextType.PLAIN)
            ])

    def test_split_nodes_delimiter_multi(self):
        node = TextNode("this is a test with some **bold shite** and some _italic faff_ in it", TextType.PLAIN)
        bold = split_nodes_delimiter([node], "**", TextType.BOLD)
        nodes = split_nodes_delimiter(bold, "_", TextType.ITALIC)
        self.assertEqual(nodes, [
            TextNode("this is a test with some ", TextType.PLAIN),
            TextNode("bold shite", TextType.BOLD),
            TextNode(" and some ", TextType.PLAIN),
            TextNode("italic faff", TextType.ITALIC),
            TextNode(" in it", TextType.PLAIN)
            ])


if __name__ == "__main__":
    unittest.main()