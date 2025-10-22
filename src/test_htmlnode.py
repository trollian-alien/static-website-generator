import unittest
from htmlnode import HTMLNode, LeafNode

class TestTextNode(unittest.TestCase):
   class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "meow",
            "meowzer",
            None,
            {"class": "domain", "href": "http://www.com"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="domain" href="http://www.com"',
        )

    def test_values(self):
        node = HTMLNode(
            "waluigi",
            "number one",
        )
        self.assertEqual(
            node.tag,
            "waluigi",
        )
        self.assertEqual(
            node.value,
            "number one",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "E",
            "EEEEEEEE",
            None,
            {"class": "EE"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(E, EEEEEEEE, children: None, {'class': 'EE'})",
        )

    def test_leaf_to_html_p(self):
            node = LeafNode("p", "Hello, world!")
            self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()