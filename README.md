**Download repository**

Clone or git the project and change directory to Downloaded location

use : https://github.com/abdulrashid123/ActivityMonitor.git

eg: cd ActivityMonitor

pip3 install -r requirements.txt # for package dependencies

**Migrations**

python manage.py migrate

**Run server**

python manage.py runserver 8000

Note: if not to test on local use python manage.py runserver 0.0.0.0:8000 and change settings allowed host 

**Create Users Management command**

python manage.py createuser

Enter Unique Id : # enter id

Enter Real Name : ## name 

Enter Password : # password

Enter time zone :# tz


**Addactivity to  Users using  Management command**

python manage.py createactivity --user real_name --password  password --count number

Enter start_time :               # %b %d %Y %I:%M%p

Enter end_time :                 #%b %d %Y %I:%M%p

Note: format is compulsory else error will be returned count denotes number of activity required to add to each user

**Client side python code to get all data in json format**

import requests

x = requests.get('http://127.0.0.1:8000/home/get_data/')

print(x.status_code)

print(x.json())

Note:if not hosted on local server change url to  http://<ip_address>:8000/home/get_data/'

**Note :create user and add data **
