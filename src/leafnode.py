from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, props: dict = None):
        super().__init__(tag=tag, value=value, children=None, props=props) # "value" needs to be mandatory

    def to_html(self) -> str:
        if self.value == None:
            raise ValueError("Value property of LeafNode class is not set.")

        if self.tag == None:
            return self.value

        if self.props_to_html() == "":
            props_as_str = ""
        else:
            props_as_str = " " + self.props_to_html()

        return f"<{self.tag}{props_as_str}>{self.value}</{self.tag}>"