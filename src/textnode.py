class TextNode:
    def __init__(self, text: str, text_type: str, url: str = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, textNode) -> bool:
        return self.text == textNode.text and self.text_type == textNode.text_type and self.url == textNode.url

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.text}, {self.text_type}, {self.url})"