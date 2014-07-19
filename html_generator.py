import csv
import re
from elements import Element
from build_pages import Build_Page

__author__ = 'kremerdesign'


def main(source_file, output_file):
    web_page = []
    with open(source_file, 'rb') as file:
        output = open(output_file, 'w')
        for row in csv.reader(file):
            for i in range(0,6):
                try:
                    row[i]
                except:
                    row.append(" ")
            web_page.append(Element(row[0], row[1], row[2], row[3], row[4], row[5]))
    output.write(Build_Page.html_boilerplate_start())
    web_page.pop(0)

    unwrapping_line_of_code = []
    prev_element_parent = 0
    current_level = 0
    for element in web_page:
        if element.parent > prev_element_parent:
            current_level = int(current_level) + 1
            output.write("\n{}{}".format("\t" * (int(current_level)+2), element.render_open()))

        elif element.parent < prev_element_parent:
            current_level = int(current_level) + 1
            # current_level = int(current_level) - 1
            for i in range(0, 2): #moving down one level - closing two tags
                if len(unwrapping_line_of_code) > 0:
                    output.write("{}".format(unwrapping_line_of_code.pop())) #close previous element
            output.write("{}{}".format("\t" * (int(current_level)), element.render_open()))

        else:
            if len(unwrapping_line_of_code) > 0:
                output.write(unwrapping_line_of_code.pop()) #close previous element(s)
            output.write("{}{}".format("\t" * (int(current_level)+2), element.render_open()))

        output.write(element.render_content())
        wrap_element = "\t{}".format(element.render_close())
        unwrapping_line_of_code.append(wrap_element)

        current_level = element.parent
        prev_element_parent = element.parent

    while len(unwrapping_line_of_code) > 0:
        output.write("{}".format(unwrapping_line_of_code.pop())) #close any remaining previous elements
    output.write(Build_Page.html_boilerplate_end())


main("html.csv", "index.html")
main("html2.csv", "index2.html")