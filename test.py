import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import datetime
import time
import random

cred = credentials.Certificate('testiot-2018-firebase-adminsdk-1jtas-d34a4864fa.json')

firebase_admin.initialize_app(cred, {'databaseURL' : 'https://testiot-2018.firebaseio.com/'})

#Creating object 
root = db.reference()

# Add a new Data for specific date under Specific Time.

while (True):
    time.sleep(3.0)
    now = datetime.datetime.now()
    datetoday = str(now.hour) + ":" + str(now.minute) +":" + str(now.second)
    randTemp = random.randint(20,32)
    randHum = random.randint(40,80)
    root.push({
        'Temperature' : randTemp, 
        'Humidity' : randHum
    })
