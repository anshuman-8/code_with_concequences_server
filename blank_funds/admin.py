from django.contrib import admin

from .models import Payment, User, Organisation, Social

admin.site.register(User)
admin.site.register(Organisation)
admin.site.register(Payment)
admin.site.register(Social)