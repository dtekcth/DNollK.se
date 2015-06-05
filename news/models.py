from datetime import datetime, timedelta
from pytz import timezone
# Django models
from django.db import models


"""
news.models module.

In this module we define the models for our Object-Relational Mapping (ORM) that
allows us to map python objects to a database which allows seamless database 
interaction.
"""
class Author(models.Model):
    """
    Author model.
    
    This is an object for post authors.
    As of now I have not found a use case for this model, so it might be removed
    in a future update...

    It is basically a user object.
    """

    # Name of author
    name = models.CharField(max_length=100)
    # Nick of author, could be only for viewing or maybe something else
    nick = models.CharField(max_length=20)
    # E-mail of author for contact and maybe logging in
    email = models.CharField(max_length=30)
    # Password of author for logging in
    password = models.CharField(max_length=50)
    # Access level of author, could be an Admin, editor or member.
    # Maybe should change the fieldtype
    access_level = models.CharField(max_length=10)

    def __str__(self):
        """
        A to string function for authors.
        When Python tries to create a textual representation of an author it will
        be displayed as the name of the author.
        """
        return self.name


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
    author = models.ForeignKey(Author)
     # Whether the post is published or not
    published = models.BooleanField(default=False)

    def publishedPosts():
        """
        Retrieves all published posts

        All it does is filters out the unpublished posts.
        """
        return Post.objects.filter(published=True)

    def byMonth(month):
        """
        Retrieve all posts published during a month.

        To get the last day in the month a little hack is used, 
        we get the date of the first day in next month (right before midnight)
        and then we subtract one second from the date. 
        This gives us the date and time for the last second in the month so
        that we retrieve every post even from the last day.

        Raises a ValueError if month is out of bounds.
        """
        # Create our timezone
        sthlm = timezone("Europe/Stockholm")
        year = datetime.now().year            
        first_day = sthlm.localize(datetime(year, month, 1, 00, 00, 00))
        
        if month == 12:
            # If we are in december we know the last day
            last_day= sthlm.localize(datetime(year, 12, 31, 23, 59, 59))
        else:
            # Otherwise, last day = first day in next month - 1 second
            tmp_day = sthlm.localize(datetime(year, month+1, 1, 00, 00, 00))
            last_day = tmp_day - timedelta(seconds=1)
            return Post.publishedPosts().filter(
                pub_date__range=(first_day, last_day))
        
    def byDay(month, day):
        """
        Retrieves the posts published during a day in a month.
        
        Not really sure what use we could have of this functions, but convinience functions are always nice.
        
        Raises a ValueError if month or day are out of bounds.
        """
        posts_in_month = Post.byMonth(month)
        sthlm = timezone("Europe/Stockholm")
        year = datetime.now().year            
        
        start_time = sthlm.localize(datetime(year, month, day, 00, 00, 00))
        end_time = sthlm.localize(datetime(year, month, day, 23, 59, 59))
        return posts_in_month.filter(pub_date__range=(start_time, end_time))
        
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

