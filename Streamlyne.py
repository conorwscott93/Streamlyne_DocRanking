#Conor Scott for Streamlyne
#15/05/2014
#Testing GridFS for document ranking

from pymongo import MongoClient
from gridfs import GridFS

db = MongoClient().example_fs
fs = GridFS(db)
a = fs.put("Test FS String")
b = fs.get(a).read()
print(b) #Prints "Test FS String"

#Diverged from GridFS for just MongoDB and document parsers

