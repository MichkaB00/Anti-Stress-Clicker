from datetime import datetime

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .forms import LoginForm, ProfileForm, RegisterForm
from .models import Customer, StressLevel
from .mongo import get_user_sessions


def home(request):
    return render(request, "users/home.html")


def customer_details(request: HttpRequest):
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
        "users_data": users_data,
    }
    return render(request, "users/customer_list.html", context)


def register(request):
    if request.user.is_authenticated:
        return redirect("profile")

    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        return redirect("profile")

    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("profile")

    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("profile")

    return render(request, "users/login.html", {"form": form})


@require_POST
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def profile(request):
    user = request.user
    sessions = get_user_sessions(user.id)
    user_info = {
        "first_name": user.first_name or "—",
        "last_name": user.last_name or "—",
        "username": user.username,
        "date_joined": timezone.localtime(user.date_joined).strftime("%d.%m.%Y"),
    }
    context = {
        "user_info": user_info,
        "statistics": build_statistics(sessions),
        "activity_history": build_activity_history(sessions),
    }
    return render(request, "users/profile.html", context)


@login_required
def edit_profile(request):
    form = ProfileForm(request.POST or None, instance=request.user)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("profile")

    return render(request, "users/edit_profile.html", {"form": form})


def build_statistics(sessions):
    total_clicks = sum(int(session.get("click_count") or 0) for session in sessions)
    completed_sessions = len(sessions)
    if completed_sessions:
        average_clicks = round(total_clicks / completed_sessions)
        moments = [
            session.get("created_at")
            for session in sessions
            if session.get("created_at")
        ]
        last_moment = max(moments) if moments else None
        last_activity = format_moment(last_moment)
    else:
        average_clicks = 0
        last_activity = "—"

    return {
        "total_clicks": total_clicks,
        "completed_sessions": completed_sessions,
        "average_clicks_per_session": average_clicks,
        "last_activity": last_activity,
    }


def build_activity_history(sessions):
    history = []
    for session in sessions:
        history.append(
            {
                "date": format_moment(session.get("created_at")),
                "clicks": int(session.get("click_count") or 0),
                "duration": f"{int(session.get('duration_minutes') or 0)} хв",
            }
        )
    return history


def format_moment(value):
    if not isinstance(value, datetime):
        return "—"
    if timezone.is_naive(value):
        value = timezone.make_aware(value, timezone.utc)
    return timezone.localtime(value).strftime("%d.%m.%Y %H:%M")
