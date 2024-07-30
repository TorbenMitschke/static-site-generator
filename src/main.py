from textnode import TextNode, text_type_italic, text_type_link
from htmlnode import LeafNode

def main():
    text_node = TextNode("I am a text node", text_type_link, "https://www.markdownguide.org")

    print(text_node)

    leafnode = LeafNode("a", "click here", {"href": "https://github.com/TorbenMitschke", "target": "_blank"})
    leafnode1 = LeafNode("a", "click here")
    leafnode2 = LeafNode(None, "click here")
    print(leafnode.to_html())
    print(leafnode1.to_html())
    print(leafnode2.to_html())
    print(leafnode.__repr__())

main()