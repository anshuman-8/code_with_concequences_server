from django.contrib import admin

from .models import Payment, User, Organisation, Social

class OrgAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'funds_required', 'funds_raised')

admin.site.register(User)
admin.site.register(Organisation, OrgAdmin)
admin.site.register(Payment)
admin.site.register(Social)