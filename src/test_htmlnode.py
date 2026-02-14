import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello", children=None, props={"class": "container"})
        self.assertEqual(
            node.__repr__(),
            "tag: div value=Hello children=None props={'class': 'container'}"
        )

    def test_props_to_html(self):
        node = HTMLNode(props={"class": "container", "id": "main"})
        self.assertEqual(
            node.props_to_html(),
            " class= container  id= main "
        )

    def test_initialization(self):
        node = HTMLNode(
            tag="p",
            value="Test",
            children=["child"],
            props={"style": "font-weight:bold;"}
        )
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Test")
        self.assertEqual(node.children, ["child"])
        self.assertEqual(node.props, {"style": "font-weight:bold;"})

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Heading")
        self.assertEqual(node.to_html(), "<h1>Heading</h1>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Link", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), "<a href= https://example.com >Link</a>")

        


