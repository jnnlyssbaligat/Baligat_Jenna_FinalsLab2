from django.shortcuts import render

PROGRAMS = [
    {
        "title": "Python Foundations",
        "level": "Beginner",
        "weeks": 6,
        "summary": "Variables, control flow, functions and data structures with weekly lab work.",
    },
    {
        "title": "Web Development with Django",
        "level": "Intermediate",
        "weeks": 8,
        "summary": "Models, views, templates and forms, building up to a full-stack application.",
    },
    {
        "title": "Desktop Apps with Tkinter",
        "level": "Intermediate",
        "weeks": 4,
        "summary": "Build graphical dashboards and connect them to a database back end.",
    },
    {
        "title": "Secure Web Practices",
        "level": "Advanced",
        "weeks": 5,
        "summary": "Authentication, CSRF protection, validation and safe deployment habits.",
    },
]


def home(request):
    return render(request, "home.html", {"programs": PROGRAMS[:3]})


def about(request):
    return render(request, "about.html")


def programs(request):
    return render(request, "programs.html", {"programs": PROGRAMS})


def contact(request):
    return render(request, "contact.html")
