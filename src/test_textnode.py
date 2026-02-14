import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT_BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT_BOLD)
        self.assertEqual(node, node2)
    
    
    def test_eq_diff_text(self):
        node = TextNode("This is a text node", TextType.TEXT_BOLD)
        node2 = TextNode("This is different", TextType.TEXT_BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_diff_type(self):
        node = TextNode("This is a text node", TextType.TEXT_BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT_ITALIC)
        self.assertNotEqual(node, node2)


    def test_eq_diff_url(self):
        node = TextNode("This is a text node", TextType.LINK_ANCHOR, "http://example.com")
        node2 = TextNode("This is a text node", TextType.LINK_ANCHOR, "http://example.org")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
