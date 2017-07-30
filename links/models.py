from django.db import models


# Create your models here.
class Link(models.Model):
    title = models.TextField()
    body = models.TextField()
    order = models.IntegerField(null=True, blank=True)

    def _render_base(self, isFirst):
        html = ["<div class=\"card center-text\">",
                "<h4><i>" + self.title + "</i></h4>",
                "<p>" + self.body + "</p>",
                "</div>"]

        if isFirst:
            html.insert(1, "<h1>Bra länkar</h1>")
            html.insert(2, "<hr>")
        return "\n".join(html)

    def render_with_heading(self):
        return self._render_base(True)

    def render(self):
        return self._render_base(False)

    def __str__(self):
        return self.title
