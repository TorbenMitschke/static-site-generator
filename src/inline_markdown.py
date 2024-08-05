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

def split_nodes_image(old_nodes: list) -> list:
    #TODO: split the TextNode objects to generate a list of TextNode objects of type text and image
    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(map(lambda text_and_url: TextNode(text_and_url[0], TextType.IMAGE, text_and_url[1]), extract_markdown_images(node.text)))
    return new_nodes

def split_nodes_link(old_nodes: list) -> list:
    #TODO: split the TextNode objects to generate a list of TextNode objects of type text and link
    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(map(lambda text_and_url: TextNode(text_and_url[0], TextType.LINK, text_and_url[1]), extract_markdown_links(node.text)))
    return new_nodes