from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm,CustomUserChangeForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form= CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    list_display=['email','username','batch','gender']
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)


admin.site.register(CustomUser,CustomUserAdmin)