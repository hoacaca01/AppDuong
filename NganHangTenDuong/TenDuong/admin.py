from django.contrib import admin
from .models import User, Street, Source, StreetType, StreetGroup, Address, Permission

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email', 'usertype', 'active_status')
    list_filter = ('usertype', 'active_status')
    search_fields = ('username', 'full_name', 'email')
@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('source_name', 'source_docID')
    search_fields = ('source_name', 'source_docID')

@admin.register(StreetType)
class StreetTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)
    search_fields = ('type_name',)

@admin.register(StreetGroup)
class StreetGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'number_member')
    search_fields = ('group_name',)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id_address', 'ward_name', 'district_name')
    search_fields = ('id_address', 'ward_name', 'district_name')
@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ('street_name', 'type_streetID', 'group_streetID', 'length', 'width')
    list_filter = ('type_streetID', 'group_streetID')
    search_fields = ('street_name', 'type_streetID', 'group_streetID')
@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'active_status', 'created_at')
    list_filter = ('role', 'active_status')
    search_fields = ('user__username', 'role')