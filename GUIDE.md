# Step-by-Step Guide: Branded Web Portal (Week 14)

This is a **separate project** from the Week 13 guestbook. It is a 4-page Django site (Home, About,
Programs, Contact) where every page extends one shared `base.html`. The code is written and tested
(6 passing tests).

---

## Part 1 — Set up the project folder

Layout:

```
portal_project/
├── manage.py
├── requirements.txt
├── README.md
├── GUIDE.md
├── ACCESSIBILITY_REVIEW_NOTE.md
├── .gitignore
├── config/            settings.py, urls.py, wsgi.py
├── portal/            views.py, urls.py, tests.py
├── templates/         base.html, home.html, about.html, programs.html, contact.html
└── static/css/        style.css
```

1. Create a **new** folder for this activity, e.g. `Baligat_Jenna_FinalsLab2` (don't reuse the guestbook folder).
2. Extract `portal_project.zip` and copy the **contents** into it (or just keep the `portal_project` folder).
3. Open it in VS Code. In the terminal, move into the folder that contains `manage.py`:
   ```powershell
   cd portal_project
   ```
4. Create and activate a virtual environment (skip creating if you want to reuse the old one):
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```
5. Run it:
   ```powershell
   python manage.py migrate
   python manage.py runserver
   ```
6. Visit http://127.0.0.1:8000/ and click through all four pages.

> Run `dir` first. If you can see `manage.py`, you're in the right place.

> **Personalize it** (the sheet says not to copy as-is): rename the brand in `base.html`
> (header, footer, and `<title>`), edit the page text, and/or change `--primary` and `--accent`
> in `static/css/style.css`. If you rename the brand, update the two strings checked in
> `portal/tests.py` too.

---

## Part 2 — Map the task steps to the code

| Step in the sheet | Where it lives |
|---|---|
| 1. `base.html` with header, footer, nav, empty `{% block content %}` | `templates/base.html` |
| 2. `STATIC_URL` and `STATICFILES_DIRS` | `config/settings.py` (bottom) |
| 3. `{% load static %}` at the top | First line of `base.html` (child pages don't use `{% static %}`, so they don't need it) |
| 4. Child pages use `{% extends 'base.html' %}` + `{% block content %}` | `home.html`, `about.html`, `programs.html`, `contact.html` |
| 5. CSS linked with `{% static 'css/style.css' %}` | `<link>` in `base.html` |
| 6. Change one shared element and see it update everywhere | See Part 3 |

Also in `settings.py`: `TEMPLATES → DIRS = [BASE_DIR / "templates"]` tells Django where `base.html` lives.

---

## Part 3 — Do the "change one shared element" test (Step 6)

1. Open `templates/base.html` and change the brand text in the header, e.g. `Amethyst Learning Portal` → `Amethyst Learning Portal (Edited)`.
2. Save, refresh Home, About, Programs and Contact. The header changes on **all four** pages.
3. Take a screenshot of two pages showing the changed header.
4. Change it back (or keep your own brand name).

Run the tests with `python manage.py test` — they will fail if you rename the brand without updating
`tests.py`. That is expected.

---

## Part 4 — Screenshots for the PDF

**Code (8):**
1. `templates/base.html`
2. `templates/home.html`
3. `templates/about.html`
4. `templates/programs.html`
5. `templates/contact.html`
6. `static/css/style.css`
7. `config/settings.py` — the static/templates section (`DIRS`, `STATIC_URL`, `STATICFILES_DIRS`)
8. `portal/views.py` or `portal/urls.py` (optional)

**Output (4–5):** one per page, with the **address bar visible**
- Home `/`, About `/about/`, Programs `/programs/`, Contact `/contact/`
- The shared-element test (Part 3): header changed on at least two pages
- Optional: terminal showing `python manage.py test` → `OK`

Build the PDF in Word or Google Docs: title, your name/section/date, a **Code** heading with captions,
an **Output** heading with captions, and the Accessibility Review Note at the end if your instructor
wants it in the same file. Export as PDF.

---

## Part 5 — GitHub

1. https://github.com/new → name it (e.g. `Baligat_Jenna_FinalsLab2`), **Public**, leave README/.gitignore unticked.
2. In the VS Code terminal, inside the folder with `manage.py`:
   ```powershell
   git init
   git add .
   git status
   git commit -m "Add Week 14 branded web portal with shared base.html"
   git branch -M main
   git remote add origin https://github.com/jnnlyssbaligat/Baligat_Jenna_FinalsLab2.git
   git push -u origin main
   ```
3. Check that `db.sqlite3` and `venv/` are **not** in the repo. Submit the repo link.

---

## Part 6 — Accessibility Review Note

A draft is in `ACCESSIBILITY_REVIEW_NOTE.md`. Your instructor's template wasn't in the PDF, so copy
the answers into theirs. Before submitting, tab through the site yourself with the keyboard and confirm
the notes match what you see.

---

## Submission checklist

- [ ] Project zip or GitHub link (−25 pts if missing)
- [ ] PDF of screenshots: code and output (−15 pts if missing)
- [ ] Completed Accessibility Review Note
- [ ] Submitted before the end of the lab session

## Troubleshooting

| Problem | Fix |
|---|---|
| `TemplateDoesNotExist: base.html` | `TEMPLATES → DIRS` must contain `BASE_DIR / "templates"`, and the file must be in `templates/` |
| Page has no styling | Check `STATICFILES_DIRS`, that the file is `static/css/style.css`, and that `{% load static %}` is the first tag in `base.html` |
| `Invalid block tag: 'static'` | `{% load static %}` is missing in that template |
| Child page shows plain, unstyled text | `{% extends 'base.html' %}` must be the very first line |
| Content missing from a page | Block names must match exactly: `{% block content %}` in both files |
| Changes to CSS not showing | Hard refresh with Ctrl + F5 |
