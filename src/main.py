from textnode import TextNode, text_type_italic, text_type_link
from htmlnode import HTMLNode, LeafNode

def main():
    text_node = TextNode("I am a text node", text_type_link, "https://www.markdownguide.org")
    print(text_node)

    html_a = HTMLNode("a", "click here", None, {"href": "https://github.com/TorbenMitschke", "target": "_blank"})
    html_h1 = HTMLNode("h1", "This is a heading 1.", None, None)
    htmlnode = HTMLNode("p", "This is a paragraph.", [html_a, html_h1], {"id": "paragraph1", "class": "text-muted", "lang": "en"})
    print(htmlnode)

    leafnode = LeafNode("a", "click here", {"href": "https://github.com/TorbenMitschke", "target": "_blank"})
    leafnode1 = LeafNode("a", "click here")
    leafnode2 = LeafNode(None, "click here")
    print(leafnode.to_html())
    print(leafnode1.to_html())
    print(leafnode2.to_html())
    print(leafnode.__repr__())

main()