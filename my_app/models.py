from django.db import models

# Create your models here.
class ScrapedLink(models.Model):

    # fields
    source_url = models.URLField(help_text="The page you scraped")
    found_link = models.URLField(unique=True, max_length=500, help_text="The URL found on the page")
    scraped_at = models.DateTimeField(auto_now_add=True)

    #meta options
    def __str__(self):
        return self.found_link

    # methods