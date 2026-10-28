from django.shortcuts import render


def home(request):
    return render(request, 'users/home.html')


def profile(request):
    user_info = {
        'full_name': 'Олена Коваленко',
        'username': 'olena.kovalenko',
        'date_joined': '12.09.2025',
    }

    statistics = {
        'total_clicks': 1840,
        'completed_sessions': 24,
        'average_clicks_per_session': 77,
        'last_activity': '18.03.2026',
    }

    activity_history = [
        {'date': '18.03.2026', 'clicks': 92, 'duration': '12 хв'},
        {'date': '15.03.2026', 'clicks': 65, 'duration': '8 хв'},
        {'date': '12.03.2026', 'clicks': 110, 'duration': '15 хв'},
        {'date': '09.03.2026', 'clicks': 48, 'duration': '6 хв'},
        {'date': '05.03.2026', 'clicks': 81, 'duration': '10 хв'},
    ]

    context = {
        'user_info': user_info,
        'statistics': statistics,
        'activity_history': activity_history,
    }
    return render(request, 'users/profile.html', context)
