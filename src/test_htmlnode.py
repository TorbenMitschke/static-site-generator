import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        html_node = HTMLNode("a", "click here", None, {"href": "https://github.com/TorbenMitschke", "target": "_blank"})
        self.assertEqual(html_node.props_to_html(), ' href="https://github.com/TorbenMitschke" target="_blank"')

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
        self.assertEqual(html_node.__repr__(),
                         "HTMLNode(p, This is a paragraph., children: [HTMLNode(a, click here, children: None, {'href': 'https://github.com/TorbenMitschke', 'target': '_blank'}), HTMLNode(h1, This is a heading 1., children: None, None)], {'id': 'paragraph1', 'class': 'text-muted', 'lang': 'en'})")

    def test_repr_not_eq(self):
        html_node = HTMLNode( tag="a", props={"href": "https://github.com/TorbenMitschke", "target": "_blank"})
        html_node2 = HTMLNode("h1", "This is a heading", None, None)
        self.assertNotEqual(repr(html_node), repr(html_node2))

    def test_values(self):
        html_node = HTMLNode("a", "click here", None, {"href": "https://github.com/TorbenMitschke", "target": "_blank"})
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "click here")
        self.assertEqual(html_node.children, None)

# LeafNode class
    def test_to_html_valid(self):
        leafnode = LeafNode("a", "click here", {"href": "https://github.com/TorbenMitschke", "target": "_blank"})

        try:
            leafnode.to_html()
        except ValueError:
            self.fail("to_html() raised ValueError unexpectedly")

    def test_to_html_no_value(self):
        leafnode = LeafNode("a", None, {"href": "https://github.com/TorbenMitschke", "target": "_blank"})

        with self.assertRaises(ValueError) as context:
            leafnode.to_html()
            self.assertEqual(str(context.exception), "Value property of LeafNode class is not set.")

    def test_to_html_equal(self):
        leafnode = LeafNode("a", "click here", {"href": "https://github.com/TorbenMitschke", "target": "_blank"})
        self.assertEqual(leafnode.to_html(), '<a href="https://github.com/TorbenMitschke" target="_blank">click here</a>')

    def test_to_html_not_equal(self):
        leafnode = LeafNode("a", "click here")
        self.assertNotEqual(leafnode.to_html(), '<a >click here</a>')

    def test_to_html_no_tag(self):
        leafnode = LeafNode(None, "click here", {"href": "https://github.com/TorbenMitschke", "target": "_blank"})
        self.assertEqual(leafnode.to_html(), "click here")

    def test_to_html_no_children(self):
        leafnode = LeafNode("p", "Hello World!")
        self.assertEqual(leafnode.to_html(), "<p>Hello World!</p>")

if __name__ == "__main__":
    unittest.main()