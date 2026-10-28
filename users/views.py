from django.http import HttpRequest
from django.shortcuts import render

from .models import Customer, StressLevel
from datetime import datetime


def home(request):
    return render(request, "users/home.html")


def admin(request: HttpRequest):
    users_data: list[Customer] = [
        Customer(
            full_name="Bertha King",
            stress_level=StressLevel.LOW,
            total_clicks=12,
            average_clicking_speed=3.2,
            last_activity=datetime.now(),
        ),
        Customer(
            full_name="Anthony Ward",
            stress_level=StressLevel.MEDIUM,
            total_clicks=94,
            average_clicking_speed=6.5,
            last_activity=datetime.now(),
        ),
        Customer(
            full_name="Frederick Owens",
            stress_level=StressLevel.HIGH,
            total_clicks=98,
            average_clicking_speed=2.2,
            last_activity=datetime.now(),
        ),
        Customer(
            full_name="Lora Saunders",
            stress_level=StressLevel.LOW,
            total_clicks=44,
            average_clicking_speed=8.3,
            last_activity=datetime.now(),
        ),
        Customer(
            full_name="Tillie Graves",
            stress_level=StressLevel.MEDIUM,
            total_clicks=59,
            average_clicking_speed=7.0,
            last_activity=datetime.now(),
        ),
        Customer(
            full_name="Alejandro Williams",
            stress_level=StressLevel.HIGH,
            total_clicks=91,
            average_clicking_speed=5.3,
            last_activity=datetime.now(),
        ),
        Customer(
            full_name="Beulah Owens",
            stress_level=StressLevel.LOW,
            total_clicks=33,
            average_clicking_speed=3.5,
            last_activity=datetime.now(),
        ),
    ]
    context: dict = {
        "users": users_data,
    }
    return render(request, "users/admin.html", context)


def profile(request):
    user_info = {
        "full_name": "Олена Коваленко",
        "username": "olena.kovalenko",
        "date_joined": "12.09.2025",
    }

    statistics = {
        "total_clicks": 1840,
        "completed_sessions": 24,
        "average_clicks_per_session": 77,
        "last_activity": "18.03.2026",
    }

    activity_history = [
        {"date": "18.03.2026", "clicks": 92, "duration": "12 хв"},
        {"date": "15.03.2026", "clicks": 65, "duration": "8 хв"},
        {"date": "12.03.2026", "clicks": 110, "duration": "15 хв"},
        {"date": "09.03.2026", "clicks": 48, "duration": "6 хв"},
        {"date": "05.03.2026", "clicks": 81, "duration": "10 хв"},
    ]

    context = {
        "user_info": user_info,
        "statistics": statistics,
        "activity_history": activity_history,
    }
    return render(request, "users/profile.html", context)
