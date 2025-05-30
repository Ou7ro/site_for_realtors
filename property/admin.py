from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town', 'owners_phonenumber', 'owner_pure_phone']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user_name', 'flat']
    

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']


admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Flat, FlatAdmin)
admin.site.register(Owner, OwnerAdmin)