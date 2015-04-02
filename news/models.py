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

    def __str__(self):
        """
        To string function. 
        This function is called when Python is trying to display a Post in text.
        
        With this function every time a post is displayed in a textual 
        representation it is now called <Post: $title> or something like that.
        """
        return self.title

