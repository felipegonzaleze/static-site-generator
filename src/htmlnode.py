class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        html_attributes: str = ""
        for k, v in self.props:
            html_attributes += f" {k}={v} "
        return html_attributes

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children} {self.props})" 