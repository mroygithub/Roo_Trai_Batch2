

class ReadNotepad:


    def readADataFromNotepad(self):

        text = open("/Users/mithunroy/Desktop/SelPyBatch2/note.txt" , "r")
        return text.read()


obj = ReadNotepad()
print(obj.readADataFromNotepad())