from wagtail.tests.utils import WagtailPageTests
from .models import BlogPage, BlogIndexPage
from home.models import HomePage


class BlogIndexPageTests(WagtailPageTests):

    def test_can_create_a_page(self):
        self.assertCanCreateAt(BlogIndexPage, BlogIndexPage)

    def test_can_create_under_home_page(self):
        self.assertCanCreateAt(HomePage, BlogIndexPage)


class BlogPageTests(WagtailPageTests):

    def test_can_create_a_page(self):
        self.assertCanCreateAt(BlogPage, BlogPage)

    def test_can_create_under_blog_index_page(self):
        self.assertCanCreateAt(BlogIndexPage, BlogPage)