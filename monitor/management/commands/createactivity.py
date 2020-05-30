# import required libraries
from django.core.management.base import BaseCommand
from monitor.models import User, Activity
from django.contrib.auth import authenticate
from datetime import datetime

# inherit BaseCommand class and override add_argument for arguments and handle to respond command method


class Command(BaseCommand):
    help = 'Command to populate data in database'

    def add_arguments(self, parser):
        parser.add_argument('--user',type=str)
        parser.add_argument('--password', type=str)
        parser.add_argument('--count', type=int)

    # create activity  for each user  with given below field and validate it

    def handle(self, *args, **options):
        username = options['user'].replace('_',' ')
        password = options['password']
        count = options['count']
        user = User.objects.get(real_name=username.strip())
        user = authenticate(real_name=user,password=password)
        if user is not None:
            if user.is_active:
                user_obj = User.objects.get(id=user.id)
                for _ in range(count):
                    start_time = input("Enter start_time : ")
                    end_time = input("Enter end_time : ")
                    try:
                        start_obj = datetime.strptime(start_time, '%b %d %Y %I:%M%p')
                        end_obj = datetime.strptime(end_time, '%b %d %Y %I:%M%p')
                        obj = Activity(user=user_obj, start_time=start_obj, end_time=end_obj)
                        obj.save()
                    except:
                        print("Error in input please check input format")
        else:
            return 'Account is not present please create'
