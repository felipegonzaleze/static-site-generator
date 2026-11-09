from enum import Enum

class TextNode:
    class TextType(Enum):
        PLAIN_TEXT = "plain"
        BOLD_TEXT = "bold"
        CODE_TEXT = "code"
        LINK_TEXT = "link"
        IMAGE_TEXT = "image"
        
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = self.TextType[text_type]
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"