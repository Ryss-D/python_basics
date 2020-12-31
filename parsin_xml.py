import xml.etree.ElementTree as ET 
#treequotes string mean a posible multiline string
data = '''<person>
    <name>Chuck</name>
    <phone> type="initl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))  