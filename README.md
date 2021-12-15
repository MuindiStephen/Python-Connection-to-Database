# Python-Connection-to-Database
Is an application that i learned how Python application can work with database

**How-to-connect-to-MongoDb-from-Python**

-MongoDB is among the top used NoSQL databases around the world. Well, i know you know that already. That is not,however the reason why i love mongoDB. Perhaps i should mention to you that MongoDB is Open Source. Yeah, that is why.

Conectiong to MongoDb can be done in almost any language. I have done works using MongoDB with Nodejs, PHP, Java among others. This therefore means, you should not worry about MongoDB drivers not being available in your preferred language.

**Why MongoDB**
Well, Mongodb is NoSQL meaning it is VERY fast & scalable – huh! everyone including you will want quick apps, websites etc.Quick is the keyword here.
It is free and Opensource unless you need hosting

**Why Python + MongoDB**
Well, am sure you do not really need an answer for this but here we go:-

First, it is the title of this article
Secondly, Python is king of Artificial Intelligent(AI). AI is King of Intensive Data manipulation and MongoDB is King of Speed and scalability
That is why.

**Getting Started**
Assumptions
You have Python 3 or higher installed
You mongoDB installed and running
You have MongoDBCompass Community(optional)
Install PyMongo
PyMongo is the MongoDB Driver for Python. Use python’s package/module manager (pip) to install.

In python 3 or higher, pip is automatically installed and therefore you do not need to install it separately.

1
$ python -m pip install PyMongo
Importing PyMongo Module in your project

1
import pymongo
Opening MongoDB Connection
This is how you open the connection from python. Below your import command add the following.

1
conn = pymongo.MongoClient("mongodb://localhost:27017/")
Create your First database
To create a database named “riorityoverride“, add the following:


1
dbcreated = conn.riorityoverride
Create a collection
A collection in MongoDB is the equivalent of a Table in SQL. Let us create collection called twitter_profiles in the database riorityoverride

1
collectioncreated = dbcreated.twitter_profiles
NOTE: Up to this point, all is well and code executes perfectly. However, if you open MongoDB compass, you will realize that no database is created and no collection too. Relax. This is normal. MongoDB does not keep “empty things“

**#Inserting Data into a collection**
MongoDB uses json format for storage. To insert data into a collection utilize the python Dict data structure.

1
profiles_dict = [
2
{ "name": "Ayan", "Followers": 1100, "Following": 110},
3
{ "name": "Everest", "Followers": 357, "Following": 4},
4
{ "name": "user345", "Followers": 34000, "Following": 2300},
5
{ "name": "user346", "Followers": 456, "Following": 986},
6
{ "name": "user347", "Followers": 3200, "Following": 234},
7
{ "name": "user348", "Followers": 100456, "Following": 203872}
8
]
9
insertion_task = collectioncreated.insert_many(profiles_dict)
**#NOTE: In MongoDB it is only after inserting some data that everything else gets created. After the above code excutes, if you open MongoDB Compass, you will see our database, collection and the data in the collection.
