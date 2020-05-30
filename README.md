Clone or git the project and change directory to Downloaded location
eg: cd ActivityMonitor

pip3 install -r requirements.txt # for package dependencies

python manage.py migrate

python manage.py runserver 8000


python manage.py createuser
Enter Unique Id 
Enter Real Name : 
Enter Password : 
Enter time zone :

python manage.py createactivity
Enter start_time :               # %b %d %Y %I:%M%p
Enter end_time :                 #%b %d %Y %I:%M%p


python request call
import requests
x = requests.get('http://127.0.0.1:8000/home/get_data/')
print(x.status_code)
print(x.json())