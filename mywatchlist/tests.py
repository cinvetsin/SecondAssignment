from django.test import TestCase, Client

# Create your tests here.
from django.urls import resolve

class MyWatchListTest(TestCase):
    def test_my_watch_list_url_exists(self):
        response = Client().get('/mywatchlist/')
        self.assertEqual(response.status_code,200)

    def test_my_watch_list_html_exists(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)

    def test_my_watch_list_xml_exists(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)

    def test_my_watch_list_json_exists(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)
    
    def test_my_watch_list_using_template(self):
        response = Client().get('/mywatchlist/')
        self.assertTemplateUsed(response, 'mywatchlist.html')    