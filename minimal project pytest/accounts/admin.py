from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Profile_Pic)
admin.site.register(Post)
admin.site.register(Social)
admin.site.register(About)
admin.site.register(Comments)

admin.site.register(Reply,MPTTModelAdmin)
admin.site.register(Blog)
admin.site.register(Video)
