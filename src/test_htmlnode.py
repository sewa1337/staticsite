import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):
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
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_empty_children(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")
    
    def test_to_html_missing_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, [LeafNode("span", "child")])
            node.to_html()
    
    def test_to_html_multiple_children(self):
        child1 = LeafNode("span", "child1")
        child2 = LeafNode("span", "child2")
        node = ParentNode("div", [child1, child2])
        self.assertEqual(node.to_html(), "<div><span>child1</span><span>child2</span></div>")


