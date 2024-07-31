from textnode import TextNode, text_type_italic, text_type_link
from htmlnode import HTMLNode, LeafNode

def main():
    text_node = TextNode("I am a text node", text_type_link, "https://www.markdownguide.org")
    print(text_node)

main()