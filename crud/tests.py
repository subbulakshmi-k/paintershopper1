from django.test import TestCase
from django.urls import reverse

class PageTests(TestCase):
    def test_colors_page(self):
        response = self.client.get(reverse('colors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'colors.html')
        self.assertContains(response, 'Our Paint Colors')

    def test_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertContains(response, 'About Us')

    def test_navigation_links(self):
        pages = ['home', 'services', 'colors', 'about', 'booknow']
        for page in pages:
            url = reverse(page)
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            for nav_page in pages:
                nav_url = reverse(nav_page)
                self.assertContains(response, f'href="{nav_url}"')
