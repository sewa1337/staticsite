class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        result = ""
        if self.props == None:
            return result
        for item in self.props.keys():
            result += f" {item}= {self.props[item]} " 
        return result

    def __repr__(self):
        return f"tag: {self.tag} value={self.value} children={self.children} props={self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__( tag, value, None, props)

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None or self.tag == "":
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"tag: {self.tag} value={self.value} props={self.props}"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Must have a tag")
        if self.children == None:
            raise ValueError("Must have children")
        string = ""
        for child in self.children:
            string +=  child.to_html()
        if self.props == None:
            return f"<{self.tag}>{string}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props}>{string}</{self.tag}>"