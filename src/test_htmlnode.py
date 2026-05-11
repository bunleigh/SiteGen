import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_paragraph(self):
        node = HTMLNode("p", "the quick brown fox jumped over the lazy dog")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    
    def test_props_link(self):
        node = HTMLNode("a", "Google", children=None, props={"href": "http://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="http://www.google.com"')


    def test_parent(self):
        node = HTMLNode("ul",value=None , children=[HTMLNode("li", "li1"), HTMLNode("li", "li2"), HTMLNode("li", "li3")])
        self.assertEqual(node.value, None)

    def test_all_defaults(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

if __name__ == "__main__":
    unittest.main()
