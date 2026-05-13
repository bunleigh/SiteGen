import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

# LeafNode

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

# ParentNode

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_multiple_children(self):
        child_node = LeafNode("b", "bold")
        child_node2 = LeafNode("i", "italics")
        parent_node = ParentNode("p", [child_node, child_node2])
        self.assertEqual(parent_node.to_html(), "<p><b>bold</b><i>italics</i></p>")

    def test_to_html_no_children(self):
        parent_node = ParentNode("p", [])
        self.assertRaises(ValueError)

if __name__ == "__main__":
    unittest.main()
