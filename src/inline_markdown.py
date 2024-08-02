from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: TextType) -> list:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        section = node.text.split(delimiter)
        if len(section) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(node.text.split(delimiter))):
            if section[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(section[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(section[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text) -> list:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text) -> list:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)