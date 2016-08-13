from django.test import TestCase
from news.models import Post
from about.models import Member, Committee

from datetime import datetime, timezone, timedelta

# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self):
        # Add a committee
        Committee.objects.create(name="Test committee",
                                 image="/static/test/image.png",
                                 text="A very interesting test committee")

        c = Committee.objects.get(name="Test committee")

        # Add an author (member)
        Member.objects.create(first_name="Test",
                              last_name="Test",
                              nick="TT",
                              committee=c,
                              image="/static/test/image.png")

        t = Member.objects.get(first_name="Test")

        sthlm = timezone(timedelta(hours=1))

        # Add post on start of year
        Post.objects.create(title="test post",
                            content="very interesting post",
                            pub_date=datetime(2016, 12, 31, 23, 59, 59, 999, sthlm),
                            published=True,
                            author=t)

        # Add post on end of year
        Post.objects.create(title="test post 2",
                            content="more interesting stuff",
                            pub_date=datetime(2016, 1, 1, 0, 0, 0, 0, sthlm),
                            published=True,
                            author=t)

        # Add unpublished post
        Post.objects.create(title="test post 3",
                            content="unpublished, but yet very interesting stuff",
                            pub_date=datetime(2016, 8, 16, 8, 30, 00, 0, sthlm),
                            published=False,
                            author=t)

    def test_filter_on_date_range_works_as_expected(self):
        posts = Post.published_posts_by_year(2016)

        self.assertEqual(len(posts), 2)

    def test_published_posts_exclude_unpublished_posts(self):
        # Count the number of posts in db
        postsCount = len(Post.objects.all())

        self.assertEqual(len(Post.published_posts()), postsCount - 1)

        # unpublish a post, should result in 1 published and 2 unpublished
        p2 = Post.objects.get(title="test post 2")
        p2.unpublish()

        self.assertEqual(len(Post.published_posts()), postsCount - 2)

        # publish a post, should go back to 2 published and 1 unpublished
        p3 = Post.objects.get(title="test post 3")
        p3.publish()

        self.assertEqual(len(Post.published_posts()), postsCount - 1)
