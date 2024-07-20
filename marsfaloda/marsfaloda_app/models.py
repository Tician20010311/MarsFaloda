from django.db import models
from django.shortcuts import render, get_object_or_404

class Image(models.Model):
    nev = models.CharField(max_length=350)
    kep_url = models.ImageField(upload_to='images/')

class News(models.Model):
    letrehozva = models.DateTimeField(auto_now_add=True)  
    cim = models.CharField( default='',max_length=350)
    szoveg = models.CharField(default='', max_length=350)


from django.db import models

class Dish(models.Model):
    DISH_TYPE_CHOICES = [
        ('soup', 'Leves'),
        ('main_course', 'Főétel'),
        ('dessert', 'Desszert'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    dish_type = models.CharField(max_length=20, choices=DISH_TYPE_CHOICES)
    
    def __str__(self):
        return self.name

class DailyMenu(models.Model):
    date = models.DateField(unique=True)
    soups = models.ManyToManyField(Dish, related_name='daily_menus_as_soup', limit_choices_to={'dish_type': 'soup'})
    main_courses = models.ManyToManyField(Dish, related_name='daily_menus_as_main_course', limit_choices_to={'dish_type': 'main_course'})
    desserts = models.ManyToManyField(Dish, related_name='daily_menus_as_dessert', limit_choices_to={'dish_type': 'dessert'})
    
    def __str__(self):
        return f"Napi menü - {self.date}"

def daily_menu_detail(request, date):
    daily_menu = get_object_or_404(DailyMenu, date=date)
    soups = daily_menu.soups.all()
    main_courses = daily_menu.main_courses.all()
    desserts = daily_menu.desserts.all()
    return render(request, 'marsfaloda_app/daily_menu_detail.html', {
        'daily_menu': daily_menu,
        'soups': soups,
        'main_courses': main_courses,
        'desserts': desserts,
    })

class WeeklyMenu(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    daily_menus = models.ManyToManyField(DailyMenu)
    
    def __str__(self):
        return f"Heti menü - {self.start_date} - {self.end_date}"
