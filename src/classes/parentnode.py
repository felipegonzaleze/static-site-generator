from classes.htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(
            tag = tag,
            children = children,
            props = props
        )

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is missing")
        elif not self.children:
            raise ValueError("Children is missing")
        else:
            final_text = ""
            for children in self.children:
                    final_text += children.to_html()
            return f"<{self.tag}{super().props_to_html()}>{final_text}</{self.tag}>"

    def __eq__(self, other):
        return self.tag == other.tag and self.children == self.children and self.props == self.props

    def __repr__(self):
         return f"ParentNode({self.tag}, {self.children}, {self.props})"
            