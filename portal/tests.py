from django.test import TestCase
from django.urls import reverse

PAGES = ["home", "about", "programs", "contact"]


class TemplateInheritanceTests(TestCase):
    def test_every_page_loads(self):
        for name in PAGES:
            with self.subTest(page=name):
                self.assertEqual(self.client.get(reverse(name)).status_code, 200)

    def test_every_page_extends_base_html(self):
        for name in PAGES:
            with self.subTest(page=name):
                response = self.client.get(reverse(name))
                self.assertTemplateUsed(response, "base.html")
                self.assertTemplateUsed(response, f"{name}.html")

    def test_shared_header_and_footer_on_every_page(self):
        for name in PAGES:
            with self.subTest(page=name):
                response = self.client.get(reverse(name))
                self.assertContains(response, "Heavenly Learning Portal</span>")
                self.assertContains(response, "&copy; 2026 Heavenly Learning Portal")

    def test_static_css_is_linked_correctly(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, 'href="/static/css/style.css"')

    def test_current_page_is_marked_in_navigation(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, 'href="/about/" aria-current="page"')

    def test_css_file_is_found_via_staticfiles_dirs(self):
        from django.contrib.staticfiles import finders

        self.assertIsNotNone(finders.find("css/style.css"))
