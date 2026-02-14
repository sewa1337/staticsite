import unittest
from functions import split_nodes_delimiter
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    
    def test_eq_diff_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is different", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_diff_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)


    def test_eq_diff_url(self):
        node = TextNode("This is a text node", TextType.LINK, "http://example.com")
        node2 = TextNode("This is a text node", TextType.LINK, "http://example.org")
        self.assertNotEqual(node, node2)


    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")

    def test_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")

    def test_code(self):
        node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code text")

    def test_link(self):
        node = TextNode("Link text", TextType.LINK, "http://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Link text")
        self.assertEqual(html_node.props["href"], "http://example.com")

    def test_image(self):
        node = TextNode("Alt text", TextType.IMAGE, "http://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "http://example.com")
        self.assertEqual(html_node.props["alt"], "Alt text")

 
    def test_split_nodes_delimiter_valid(self):
        # Test valid split with even delimiter count
        old_nodes = [TextNode("This is **bold** text", TextType.TEXT)]
        delimiter = "**"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[1].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, " text")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_split_nodes_delimiter_invalid(self):
        # Test invalid split with odd delimiter count
        old_nodes = [TextNode("This is **bold", TextType.TEXT)]
        delimiter = "**"
        text_type = TextType.BOLD
        with self.assertRaises(Exception):
            split_nodes_delimiter(old_nodes, delimiter, text_type)

    def test_split_nodes_delimiter_non_text_node(self):
        # Test non-TEXT node is added as-is
        old_nodes = [TextNode("This is text", TextType.BOLD)]
        delimiter = "**"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(new_nodes, old_nodes)

if __name__ == "__main__":
    unittest.main()



