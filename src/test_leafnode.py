import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
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
        leafnode = LeafNode("click here", {"href": "https://github.com/TorbenMitschke", "target": "_blank"})

if __name__ == "__main__":
    unittest.main()