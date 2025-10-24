from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #input: lost of textnodes, a delimiter, and the texttype of each delimiter
    new_nodes = []
    for node in old_nodes:
        node_text_type = node.text_type
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise SyntaxError("Invalid Markdown Syntax; either an extra delimiter was added or one is missing")
        use_node_text_type = True
        for text in split_text:
            current_text_type = node_text_type if use_node_text_type else text_type
            use_node_text_type = not use_node_text_type
            if text != "":
                new_nodes.append(TextNode(text, current_text_type))
    return new_nodes