import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node,node2)

    def test_eq2(self):
        node = TextNode("I am a text node", TextType.ITALIC, None)
        node2 = TextNode("I am a text node", TextType.ITALIC)
        self.assertEqual(node,node2)

    def test_not_eq(self):
        node = TextNode("I am a text node as well", TextType.IMAGE)
        node2 = TextNode("I am a text node as well", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("I am a text node as well", TextType.CODE, "https://github.com/TorbenMitschke")
        node2 = TextNode("I am a text node as well", TextType.CODE, "https://github.com/TorbenMitschke")
        self.assertEqual(node, node2)

    def test_repr_eq(self):
        node = TextNode("I am a text node as well", TextType.ITALIC, "https://github.com/TorbenMitschke")
        self.assertEqual("TextNode(I am a text node as well, ITALIC, https://github.com/TorbenMitschke)", repr(node))

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        text = TextNode("bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text)
        self.assertEqual(html_node.value, "bold text")
        self.assertEqual(html_node.tag, "b")

    def test_image(self):
        image = TextNode("placeholder image", TextType.IMAGE, "https://picsum.photos/400")
        html_node = text_node_to_html_node(image)
        self.assertEqual(repr(html_node), "LeafNode(img, , {'src': 'https://picsum.photos/400', 'alt': 'placeholder image'})")
        self.assertEqual(html_node.value, "")

if __name__ == "__main__":
    unittest.main()