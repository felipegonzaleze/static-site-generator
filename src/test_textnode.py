import unittest
from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter
class TestTextNode(unittest.TestCase):
    def test_bold_text_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_bold_text_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a different text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_plain_text_eq(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        node2 = TextNode("This is a text node", TextType.PLAIN_TEXT)
        self.assertEqual(node, node2)

    def test_plain_text_not_eq(self):
            node = TextNode("This is a text node", TextType.PLAIN_TEXT)
            node2 = TextNode("This is a different text node", TextType.PLAIN_TEXT)
            self.assertNotEqual(node, node2)

    def test_bold_url_text_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "https://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, "https://example.com")
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        test_node_1 = TextNode("This is text with a ", TextType.PLAIN_TEXT)
        test_node_2 = TextNode("code block", TextType.CODE_TEXT)
        test_node_3 = TextNode(" word", TextType.PLAIN_TEXT)
        print(f"Lista: {new_nodes}")
        self.assertEqual(new_nodes, [test_node_1, test_node_2, test_node_3])



if __name__ == "__main__":
    unittest.main()