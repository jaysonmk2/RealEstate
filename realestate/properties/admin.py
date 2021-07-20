from django.contrib import admin
from .models import Homes

# Register your models here.














class HomesAdmin(admin.ModelAdmin):
    exclude = ('date_added',)
    list_display=('house_name', 'bedroom_amount', 'bathroom_amount', 'house_floor', 'garage_amount', 'square_feet')
admin.site.register(Homes, HomesAdmin)