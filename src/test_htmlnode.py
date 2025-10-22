import unittest
from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()