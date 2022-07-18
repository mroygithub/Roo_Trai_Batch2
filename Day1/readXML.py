from xml.dom import minidom



class ReadXMLFile:

    def resdXMLAsPerNode(self , your_test_param):

        first_parse_XML = minidom.parse("/Users/mithunroy/Desktop/SelPyBatch2/readData.xml")
        data = first_parse_XML.getElementsByTagName(your_test_param)[0]
        return data.firstChild.data


        


obj =  ReadXMLFile()

print("Your XML Data is ==>"+obj.resdXMLAsPerNode("applicationURL"))
