from django.contrib import admin
# Register your models here.
from users.models import ExtendUser

admin.site.register(ExtendUser)