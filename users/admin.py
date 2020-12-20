"""  Users admin classes"""

#Django 
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
#Models 
from users.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""
    list_display = ('pk', 'user' , 'phone_number', 'biography', 'picture')
    list_display_links = ('pk' , 'user')
    list_editable = ('phone_number', 'picture', 'biography')
    search_fields = ('user__username','user__email', 'phone_number')
    
    list_filter = ('created', 'modified', 'user__is_active')

    fieldsets = (
        ('Profile', {
            'fields' :(('user', 'biography'),('website',)), 
        }),
        ('Extra fields', {
            'fields' : ('phone_number', 'picture'),
        }),
        ('Date',{
            'fields' : (('created' , 'modified'),)
        })
    )

    readonly_fields = ('created' , 'modified')

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete=False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine,)
    list_display = ('username',
                    'is_active',
                    'last_name',
                    'first_name',
                    'email')

admin.site.unregister(User)
admin.site.register(User,UserAdmin)

