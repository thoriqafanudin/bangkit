import csv

def csv_to_html(csv_file, html_file):
    with open(csv_file, "r") as f:
        csv_reader = csv.reader(f)
        data = list(csv_reader)
    
    with open(html_file, "w") as f:
        f.write("<html><body><table>\n")
        for row in data:
            f.write("<tr>")
            for cell in row:
                f.write("<td>{}</td>".format(cell))
            f.write("</tr>\n")
        f.write("</table></body></html>\n")

csv_to_html("my_dict.csv", "jadi_html.html")