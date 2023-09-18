from plagarism import main_function
from pymongo import MongoClient
from lib import convirtToText, splitTextIntoLength, searchFromTextChunks

upload_dir = "D:\\uploads\\"
dbclient: MongoClient = MongoClient("mongodb+srv://satadeep3927:ouK9pSZoyYb71Z5k@cluster0.g6znklr.mongodb.net/edukon")
database = dbclient.mongodbVSCodePlaygroundDB

pending_projects = database.projects.find({"status": 0})

for project in pending_projects:
    file_link = project.get("file_link")
    if file_link is None :
        print("No file")
        continue
    pdf_path = upload_dir + project.get("file_link")

    fullPdfText = convirtToText(pdf_path)

    chunks = splitTextIntoLength(fullPdfText)


    average_similarity = searchFromTextChunks(chunks)

    if average_similarity > 30:
        database.projects.update_one({"_id": project.get("_id")}, {"status": 0})
    else:
        database.projects.update_one({"_id": project.get("_id")}, {"status": 1})
    

text: str = """Commits serve as the tangible building blocks of a programmer’s craft. They act as the icing on the cake of code, and when written correctly, they bring substantial value. A well-written commit message becomes indispensable because they provide context — otherwise a commit message wouldn’t be needed at the first place."""

# print(main_function(text))