__author__ = 'kremerdesign'

class Build_Page(object):

    @classmethod
    def html_boilerplate_start(cls): #This should be in another file
        header_content1 = "{}\n\t{}\n\t\t{}".format("<!DOCTYPE html>", "<head>",
                                                    "<meta name='author' content='Ben Kremer Design'>")
        header_content2 = "\n\t\t{}{}{}\n\t{}\n\t{}\n".format("<title>", "", "</title>", "</head>", "<body>")
        return "{}{}".format(header_content1, header_content2)
        # return "{}\n\t{}\n\t\t{}\n\t\t{}{}{}\n\t{}\n\t{}\n".format("<!DOCTYPE html>", "<head>", "<meta name='author' content='Ben Kremer Design'>", "<title>", "", "</title>", "</head>", "<body>")

    @classmethod
    def html_boilerplate_end(cls): #This could be in another file.
        return "\n\t{}\n{}".format("</body>", "</html>")

