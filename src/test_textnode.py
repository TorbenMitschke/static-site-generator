import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node,node2)

    def test_eq2(self):
        node = TextNode("I am a text node", text_type_italic, None)
        node2 = TextNode("I am a text node", "italic")
        self.assertEqual(node,node2)

    def test_not_eq(self):
        node = TextNode("I am a text node as well", text_type_image)
        node2 = TextNode("I am a text node as well", text_type_link)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("I am a text node as well", text_type_code, "https://github.com/TorbenMitschke")
        node2 = TextNode("I am a text node as well", text_type_code, "https://github.com/TorbenMitschke")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("I am a text node as well", "italic", "https://github.com/TorbenMitschke")
        self.assertNotEqual("I am a text node as well, italic, https://github.com/TorbenMitschke", repr(node))

if __name__ == "__main__":
    unittest.main()