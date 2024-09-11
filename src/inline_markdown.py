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
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        node_text = node.text
        images = extract_markdown_images(node_text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for img in images:
            sections = node_text.split(f"![{img[0]}]({img[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown: Image section not closed.")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(img[0], TextType.IMAGE, img[1]))
            node_text = sections[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes: list) -> list:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        node_text = node.text
        links = extract_markdown_links(node_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            sections = node_text.split(f"[{link[0]}]({link[1]})", 1)
            # TODO: Check the error in TEST line 145
            if len(sections) != 2:
                raise ValueError("Invalid markdown: Link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            node_text = sections[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, TextType.TEXT))
    return new_nodes