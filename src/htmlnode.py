class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag, self.value, self.children, self.props = tag, value, children, props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented (try a subclass)")
    
    def props_to_html(self):
        return  "".join([f' {key}:"{self.props[key]}"' for key in self.props]) if self.props is not None else ""
    
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value}, children: {self.children},props: {self.props})"
    