from django.test import TestCase
from .helpers import error_handler, camelize, underlize


class Helpers(TestCase):
    def test_error_handling(self):
        @error_handler
        def division_by_zero():
            4 // 0

        with self.assertRaises(ZeroDivisionError):
            division_by_zero()

    def test_camelize_underlize(self):
        self.assertEquals(camelize("book_type", False), "bookType")
        self.assertEquals(underlize(camelize("book_type", False)), "book_type")
