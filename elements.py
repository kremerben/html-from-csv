__author__ = 'kremerdesign'


class Element(object):
    def __init__(self, id, type, parent='0', text="", element_class="", style=""):
        self.id = id
        self.type = type
        self.parent = parent
        self.text = text
        self.element_class = element_class
        self.style = style
        if self.parent == "":
            self.parent = 0

    def render_open(self):
        return '<{} class="{}" id="{}" style="{}">'.format(self.type, self.element_class, "{}-{}".format(self.type, self.id), self.style)

    def render_content(self):
        if "[http://" in self.text:
            match = re.search(r'(.+) (\w+)\[(http:\/\/.+)\](.+)', self.text)
            # m = re.search(r'(.+) (\w+)\[(http:\/\/.+)\](.+)', self.text)
            return "{} <a href='{}'>{}</a>{}".format(str(match.group(1)), str(match.group(3)), str(match.group(2)), str(match.group(4)))
        else:
            return self.text

    def render_close(self):
        return "</{}>\n".format(self.type, self.id)

#
# class Link(Element):
#     def __init__(self, id, type, weblink, parent="", text="", element_class="", style=""):
#         super(Link, self).__init__(id, type, parent, text, element_class, style)
#         self.weblink = weblink
#
#     def render_link(self):
#         return '<{} href="{}" class="{}" id="{}" style="{}">'.format(self.type, self.weblink, self.element_class, self.id, self.style)

