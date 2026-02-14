from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type   != TextType.TEXT:
            new_nodes.append(old_node)
        elif old_node.text.count(delimiter) % 2 != 0:
            raise Exception("Not a valid markdown, missing delimiter")
        else:
            sub_strings = old_node.text.split(delimiter)
            for sub_string in sub_strings:
                new_nodes.append(TextNode(sub_string,old_node.text_type))

    return new_nodes
