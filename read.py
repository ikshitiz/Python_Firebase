import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('testiot-2018-firebase-adminsdk-1jtas-d34a4864fa.json')

firebase_admin.initialize_app(cred, {'databaseURL' : 'https://testiot-2018.firebaseio.com/'})

#Creating object 
root = db.reference().get()

print(root)
print(type(root))
