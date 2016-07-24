from datetime import timedelta, date
from pytz import timezone

# Django models
from django.db import models

# Our own models
from about.models import Member, Committee
from upload.models import Upload

"""
news.models module.

In this module we define the models for our Object-Relational Mapping (ORM) that
allows us to map python objects to a database which allows seamless database
interaction.
"""
class Post(models.Model):
    """
    Post model.

    This is the actual news post model, and contains a title, the post content,
    a published date, a post author and an option to not publish the post
    immediately.

    To interact with this object, make sure that it is imported, one can simply
    let the ORM do all the heavy lifing.
    Examples:

    >>> from news.models import Post
    # Imports the object

    >>> allPosts = Post.objects.all()
    # Gets all posts
    >>> allPublished = Post.objects.filter(published=True)
    # Gets all published posts
    >>> post14 = Post.objects.get(id=14)
    # Gets the fourteenth post
    """

    # Title of post
    title = models.CharField(max_length=100)
    # Content of post, could be html or anything
    content = models.TextField()
    # Date of when the post was published
    pub_date = models.DateTimeField('date published')
    # Link to the author that published the post
    author = models.ForeignKey(Member)
    # Whether the post is published or not
    published = models.BooleanField(default=False)
    # An image linked to the post
    image = models.ForeignKey(Upload, blank=True, default=None)

    @staticmethod
    def published_posts():
        """
        Retrieves all published posts from the current year.
        """
        year = date.today().year
        return Post.published_posts_by_year(year)

    @staticmethod
    def published_posts_by_year(year):
        """
        Retrieves all published posts from a specified year.
        """
        return Post.all_published_posts().filter(pub_date__year=int(year))

    @staticmethod
    def all_published_posts():
        """
        Retrieves all published posts

        All it does is filters out the unpublished posts.
        """
        return Post.objects.filter(published=True)

    @staticmethod
    def by_month(year, month):
        """
        Retrieve all posts published during a month.

        To get the last day in the month a little hack is used,
        we get the date of the first day in next month and then we
        subtract one day from the date. This gives us the date for
        the last day in the month so that we retrieve every post
        in a month without knowing the number of days in that month.

        Raises a ValueError if month is out of bounds.
        """
        first_day = date(int(year), int(month), 1)

        # last day = first day in next month - 1 day
        last_day = date(int(year), int(month)+1, 1) - timedelta(days=1)
        return Post.published_posts().filter(pub_date__date__range=(first_day, last_day))

    @staticmethod
    def by_day(year, month, day):
        """
        Retrieves the posts published during a day in a month.

        Raises a ValueError if month or day are out of bounds.
        """
        sthlm = timezone("Europe/Stockholm")

        date = date(int(year), int(month), int(day))
        return Post.published_posts().filter(pub_date__date=date)

    def publish(self):
        """
        Publishes a post.

        This function will publish a post and then save it,
        if the post already is published nothing happens.

        >>> p = Post(title="T", content="Some text", author=0)
        # Creates a new post
        >>> p.publish()
        # Sets its status to published and saves the post
        """
        if not self.published:
            self.published = True
            self.save()
        # If self is published, nothing will happen


    def unpublish(self):
        """
        Unpublishes a post.

        This function will unpublish a post and then save it,
        if the post is not published when this function is called nothing will
        happen.

        >>> p = Post.objects.latest('pub_date')
        # p = latest post (considering published date)
        >>> p.unpublish()
        # Sets its status to unpublished and saves the post
        """

        if self.published:
            self.published = False
            self.save()
        # If self is not published, nothing will happen

    def __str__(self):
        """
        To string function.
        This function is called when Python is trying to display a Post in text.

        With this function every time a post is displayed in a textual
        representation it is now called <Post: $title> or something like that.
        """
        return self.title
