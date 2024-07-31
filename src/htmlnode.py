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
        return "".join(map(lambda item: f' {item[0]}="{item[1]}"', self.props.items()))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag, value, None, props) # "children" should not be allowed

    def to_html(self) -> str:
        if self.value == None:
            raise ValueError("Invalid HTML: No value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None) -> None:
        super().__init__(tag, None, children, props) # "value" should not be allowed

    def to_html(self):
        if self.tag == None:
            raise ValueError("Invalid HTML: No tag")
        if self.children == None:
            raise ValueError("Invalid HTML: Parent node must have children") #TODO: Refine error message
        return f"<{self.tag}{self.props_to_html()}>{"".join(map(lambda child: child.to_html(), self.children))}</{self.tag}>"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.tag}, children: {self.children}, {self.props})"