from django.core.management.base import BaseCommand
from monitor.models import User
from django.contrib.auth import authenticate


class Command(BaseCommand):
    help = 'Command to populate data in database'

    def add_arguments(self, parser):
        pass

    def validate_create(self, key, username, password,tz):
        try:
            user = User.objects.get(real_name=username)
            print(user.pk)
            print('User name present try another')
        except User.DoesNotExist:
            User.objects.create_user(id=key,username=username, password=password,timezone=tz)
            user = authenticate(real_name=username, password=password)
            print(user)

    def handle(self, *args, **options):
        key = input("Enter Unique Id : ")
        username = input("Enter Real Name : ")
        password = input("Enter Password : ")
        timezone = input("Enter time zone : ")
        self.validate_create(key,username, password,timezone)

