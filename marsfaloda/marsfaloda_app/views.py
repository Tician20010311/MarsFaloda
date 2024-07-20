from django.shortcuts import render
from datetime import date
from .models import *


def home(request):
    today = date.today()
    try:
        daily_menu = DailyMenu.objects.get(date=today)
        soups = daily_menu.soups.all()
        main_courses = daily_menu.main_courses.all()
        desserts = daily_menu.desserts.all()
    except DailyMenu.DoesNotExist:
        daily_menu = None
        soups = main_courses = desserts = []
    
    news = News.objects.all()

    return render(request, 'home.html', {
        'daily_menu': daily_menu,
        'soups': soups,
        'main_courses': main_courses,
        'desserts': desserts,
        'news': news
    })

def about(request):
    return render(request, "about.html")

