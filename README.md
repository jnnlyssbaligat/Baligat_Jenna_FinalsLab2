# Heavenly Learning Portal (Django) — Week 14

A multi-page Django site where every page extends one shared `base.html` and is styled by one static CSS file.

## Run it

```bash
python -m venv venv
venv\Scripts\activate          # Windows   (macOS/Linux: source venv/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/. Run tests with `python manage.py test`.

## Structure

| Path | Purpose |
|------|---------|
| `templates/base.html` | Shared header, navigation, footer, `{% block content %}` |
| `templates/home.html`, `about.html`, `programs.html`, `contact.html` | Child pages (`{% extends 'base.html' %}`) |
| `static/css/style.css` | Dark purple theme, linked with `{% static 'css/style.css' %}` |
| `config/settings.py` | `STATIC_URL`, `STATICFILES_DIRS`, template `DIRS` |
| `portal/views.py`, `portal/urls.py` | One view and URL per page |

Course: PC15 Python Programming 2 w/ Lab — National Teachers College