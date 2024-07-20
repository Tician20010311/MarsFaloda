from django.contrib import admin
from .models import *

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):  
    list_display = ('nev','kep_url')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):  
    list_display = ('cim','szoveg','letrehozva')



class DailyMenuAdmin(admin.ModelAdmin):
    list_display = ('date',)
    filter_horizontal = ('soups', 'main_courses', 'desserts')

class WeeklyMenuAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date')
    filter_horizontal = ('daily_menus',)

admin.site.register(Dish)
admin.site.register(DailyMenu, DailyMenuAdmin)
admin.site.register(WeeklyMenu, WeeklyMenuAdmin)

