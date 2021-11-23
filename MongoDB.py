import pymongo #mongoDB driver for Python to the DB

#establishing open connection to mongodb
conn = pymongo.MongoClient("mongodb://localhost:27017/")

#creating first database
dbcreated = conn.examination

#create collections

collectioncreated = dbcreated.studentExams

#INSERT METHOD FOR SINGLE VALUES
    db.studentResults.insert([
        {"RegNo":"COM/0008/19", "Student Name": "STEPHEN MUINDI", "QFC":"FIRST CLASS"},
    ])


#INSERT METHOD FOR MANY VALUES
    db.studentResults.insertMany([
        {"RegNo":"COM/0008/19", "Student Name": "STEPHEN MUINDI", "QFC":"FIRST CLASS"},
        {"RegNo":"COM/0009/19", "Student Name": "FESTUS MUTUKU", "QFC":"FIRST CLASS"},
        {"RegNo":"COM/0010/19", "Student Name": "MICHAEL JACKSON", "QFC":"SECOND UPPER"}
    ])

    #PRINTS THE RESULT IN FORM OF HEADLINES
     db.studentResults.find().forEach(function(doc){print('Result Analysis: '+doc.RegNo)})