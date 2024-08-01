from enum import Enum
from htmlnode import LeafNode


# text_type_text = "text"
# text_type_bold = "bold"
# text_type_italic = "italic"
# text_type_code = "code"
# text_type_link = "link"
# text_type_image = "image"

class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = 5
    IMAGE = 6

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None) -> None:
        if not isinstance(text_type, TextType):
            raise TypeError(f"text_type must be a member of TextType enum, got {type(text_type).__name__}.")

        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, textNode) -> bool:
        return (
            self.text == textNode.text
            and self.text_type == textNode.text_type
            and self.url == textNode.url
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.text}, {self.text_type.name}, {self.url})"

def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise TypeError(f"Invalid TextType: Must be of TEXT, BOLD, ITALIC, CODE, LINK or IMAGE. Got: {type(text_node.text_type).__name__}")