from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Posts)
admin.site.register(Tag)
admin.site.register(Comments)
