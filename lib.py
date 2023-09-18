from PyPDF2 import PdfReader
from plagarism import main_function
def convirtToText(path: str):
    output = ""
    reader = PdfReader(path)

    for page in reader.pages:
        output+= page.extract_text()
    
    return output

def splitTextIntoLength(string: str, length: int = 500):
    chunk =  (string[0+i:length+i] for i in range(0, len(string), length))

    return list(chunk)

def findHighestPercentage(searchList: list):
    peek = 0
    for search in searchList:
        if search[0] > peek:
            peek = search[0]
    return peek

def searchFromTextChunks(textList: list):
    total = 0
    for chunk in textList:
        results = main_function(chunk)
        total += findHighestPercentage(results)
    return total / len(textList)