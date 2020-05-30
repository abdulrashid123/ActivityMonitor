from django.contrib import admin
from .models import Activity, User

admin.site.register([Activity,User])
