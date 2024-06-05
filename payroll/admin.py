from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Deduction)
admin.site.register(Increase)
admin.site.register(Payment)