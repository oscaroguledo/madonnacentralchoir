from django.contrib import admin
from .models import Profile_Akpugo, Campus, Executive_Akpugo, Position_Akpugo, Position_Elele, Position_Okija, \
    Profile_Elele, Profile_Okija, Executive_Elele, Executive_Okija, Position_National, Profile_National, \
    Executive_National, CustomUser, Group


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_filter = ['part']
    list_per_page = 20


admin.site.register(Profile_Akpugo, ProfileAdmin)
admin.site.register(Profile_Elele, ProfileAdmin)
admin.site.register(Profile_Okija, ProfileAdmin)
admin.site.register(Profile_National, ProfileAdmin)


class CampusAdmin(admin.ModelAdmin):
    list_per_page = 20


admin.site.register(Campus, CampusAdmin)


class ExecutiveAdmin(admin.ModelAdmin):
    list_per_page = 20


admin.site.register(Executive_Akpugo, ExecutiveAdmin)
admin.site.register(Executive_Elele, ExecutiveAdmin)
admin.site.register(Executive_Okija, ExecutiveAdmin)
admin.site.register(Executive_National, ExecutiveAdmin)


class PositionAdmin(admin.ModelAdmin):
    list_per_page = 20


admin.site.register(Position_Akpugo, PositionAdmin)
admin.site.register(Position_Elele, PositionAdmin)
admin.site.register(Position_Okija, PositionAdmin)
admin.site.register(Position_National, PositionAdmin)


from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_filter = ['campus']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'campus','email',)}),
        ('Permissions/Status', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','campus', 'password', 'password_2')}
        ),
    )
    search_fields = ['first_name', 'last_name','username','campus','email']
    ordering = ['first_name']
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)
# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)