from django.db import models


class Document(models.Model):
    title = models.TextField()
    body = models.TextField()

    def render(self):
        html = ["<div class=\"card center-text\">",
                "<h4><i>" + self.title + "</i></h4>",
                "<p>" + self.body + "</p>",
                "</div>"]

        return "\n".join(html)

    def __str__(self):
        return self.title
