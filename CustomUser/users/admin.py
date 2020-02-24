from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, ExtendedDoctorsDetail, ExtendedPatientsDetail

'''
#shows other model into user model
class ExtendedDoctorsDetailInline(admin.StackedInline):
    model = ExtendedDoctorsDetail
    can_delete = False


class ExtendedPatientsDetailInline(admin.StackedInline):
    model = ExtendedPatientsDetail
    can_delete = False
'''


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'is_doctor', 'is_patient', 'address')}),
        ('Other details', {'fields': (
            'last_login',
            'is_active',
            'is_superuser',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2', 'name', 'is_doctor', 'is_patient', 'address')
            }
        ),
    )

    list_display = ('email', 'name', 'address')
    list_filter = ('is_superuser', 'is_active', 'is_doctor', 'is_patient')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, UserAdmin,)
admin.site.register(ExtendedDoctorsDetail)
admin.site.register(ExtendedPatientsDetail)
