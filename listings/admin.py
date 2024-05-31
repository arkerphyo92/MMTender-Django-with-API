from django.contrib import admin
from .models import Ministry, Fields, StateOrRegion, City, Department, ListingTender

class ListingTenderAdmin(admin.ModelAdmin):
    list_display = ('title', 'source_company', 'type', 'opendate', 'closedate', 'created_at', 'updated_at')
    list_filter = ('type', 'opendate', 'closedate')
    search_fields = ('title', 'description')

admin.site.register(Ministry)
admin.site.register(Fields)
admin.site.register(StateOrRegion)
admin.site.register(City)
admin.site.register(Department)
admin.site.register(ListingTender, ListingTenderAdmin)
