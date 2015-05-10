from django.contrib import admin

# Register your models here.
from .models import signup
from .models import ipl_scores

admin.site.register(signup)
admin.site.register(ipl_scores)
