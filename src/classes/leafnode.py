from classes.htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(
            tag = tag,
            value = value,
            children = None,
            props = props
        )

    def to_html(self) -> str:
        if not self.value:
            raise ValueError
        elif not self.tag:
            return self.value
        elif self.props:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.props == other.props