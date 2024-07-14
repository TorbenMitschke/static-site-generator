import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        html_node = HTMLNode("a", "click here", None, {"href": "https://github.com/TorbenMitschke", "target": "_blank"})
        self.assertEqual(html_node.props_to_html(), 'href="https://github.com/TorbenMitschke" target="_blank"')

    def test_props_none(self):
        html_node = HTMLNode()
        self.assertEqual(html_node.props_to_html(), "")

    def test_props_not_eq(self):
        html_node = HTMLNode("p", "This is a paragraph.", None, {"id": "paragraph1", "class": "text-muted", "lang": "en"})
        html_node2 = HTMLNode("p", "This is a paragraph.", None, {"id": "paragraph2", "class": "text-muted", "lang": "en"})
        self.assertNotEqual(html_node.props_to_html(), html_node2.props_to_html())

    def test_repr_eq(self):
        html_a = HTMLNode("a", "click here", None, {"href": "https://github.com/TorbenMitschke", "target": "_blank"})
        html_h1 = HTMLNode("h1", "This is a heading 1.", None, None)
        html_node = HTMLNode("p", "This is a paragraph.", [html_a, html_h1], {"id": "paragraph1", "class": "text-muted", "lang": "en"})
        self.assertEqual(repr(html_node),
                         "HTMLNode(p, This is a paragraph., [HTMLNode(a, click here, None, {'href': 'https://github.com/TorbenMitschke', 'target': '_blank'}), HTMLNode(h1, This is a heading 1., None, None)], {'id': 'paragraph1', 'class': 'text-muted', 'lang': 'en'})")

    def test_repr_not_eq(self):
        html_node = HTMLNode( tag="a", props={"href": "https://github.com/TorbenMitschke", "target": "_blank"})
        html_node2 = HTMLNode("h1", "This is a heading", None, None)
        self.assertNotEqual(repr(html_node), repr(html_node2))