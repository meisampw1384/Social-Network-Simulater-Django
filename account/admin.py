from django.contrib import admin


from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('user','avatar')
    list_display = ['user','avatar','phone_number']
    



