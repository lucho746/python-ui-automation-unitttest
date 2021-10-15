from xml.dom import minidom


class XMLReader:
    def __init__(self):
        self.document = minidom.parse('./config/configuration.xml')

    def get_data(self, data):
        item = self.document.getElementsByTagName(data)[0].firstChild.nodeValue
        return item
