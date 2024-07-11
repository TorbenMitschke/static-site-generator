from textnode import TextNode, text_type_italic

def main():
    text_node = TextNode("I am a text node", text_type_italic, "https://www.markdownguide.org")

    print(text_node)

main()