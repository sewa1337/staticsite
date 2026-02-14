from textnode import TextNode, TextType

def main():
    textNode = TextNode("This is some anchor text", TextType.LINK_ANCHOR, "https://www.boot.dev")
    print (textNode)



main()