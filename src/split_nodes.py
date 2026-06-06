from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    splits = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            splits.append(node)
            continue
        
        node_split = node.text.split(delimiter)
        if len(node_split) % 2 == 0:
            raise Exception("Invalid markdown syntax")
        
        inside_delim = False

        for segment in node_split:
            if segment == "":
                continue

            if not inside_delim:
                splits.append(TextNode(segment, TextType.PLAIN))
                
            else:
                splits.append(TextNode(segment, text_type))

            inside_delim = not inside_delim
    
    return splits

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    pass

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    pass