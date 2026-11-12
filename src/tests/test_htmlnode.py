import unittest
from classes.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_eq(self):
        node = HTMLNode("Tag", "Value", [], {})
        node2 = HTMLNode("Tag", "Value", [], {})
        self.assertEqual(node, node2)

    def test_htmlnode_not_eq(self):
        node = HTMLNode("Tag", "Value")
        node2 = HTMLNode("Tag", "value")
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("Tag", "Value", [], {"href": "https://www.google.com", "target": "_blank"})
        attributes_example = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), attributes_example)

if __name__ == "__main__":
    unittest.main()