fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

from reportlab.platypus import SimpleDocTemplate
report = SimpleDocTemplate("C:\\Users\\LENOVO\\Downloads\\test.pdf")

from reportlab.platypus import Paragraph, Spacer, Table, Image

#You can make a style all of your own, but we’ll use the default provided by the module for these examples. The styles object now contains a default "sample" style. It’s like a dictionary of different style settings. If you've ever written HTML, the style settings will look familiar. For example h1 represents the style for the first level of headers. Alright, we're finally ready to give this report a title!

from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
report.build([report_title])

#Let's spice this up by adding a Table. To make a Table object, we need our data to be in a list-of-lists, sometimes called a two-dimensional array. We have our inventory of fruit in a dictionary. How can we convert a dictionary into a list-of-lists?

table_data = []
for k,v in fruit.items():
    table_data.append([k,v])
print(table_data)

report_table = Table(data = table_data)
report.build([report_title, report_table])

from reportlab.lib import colors
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data = table_data, style = table_style, hAlign = "LEFT")
report.build([report_title, report_table])

inch = 1

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
report_pie = Pie(width=3*inch, height=3*inch)

report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)
print(report_pie.data)
print(report_pie.labels)

report_chart = Drawing()
report_chart.add(report_pie)
report.build([report_title, report_table, report_chart])