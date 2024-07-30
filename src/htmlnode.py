class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self) -> str:
        if self.props == None:
            return ""
        return " ".join(map(lambda item: f'{item[0]}="{item[1]}"', self.props.items()))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.tag}, {self.value}, {self.children}, {self.props})"


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