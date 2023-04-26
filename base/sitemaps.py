from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Job, Post

class StaticSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "daily"
    priority = 0.9

    def items(self):
        # Return list of url names for views to include in sitemap
        return ['home', 'about', 'contact','joblist', 'our-services','privacy-policy','terms-and-conditions']

    def location(self, item):
        return reverse(item)

class JobSitemap(Sitemap):
		changefreq = "daily"
		priority = 0.9
		
		def items(self):
				return Job.objects.all()
		
		def lastmod(self, obj):
				return obj.updated
		
		def location(self,obj):
			return '/job/%s' % (str(obj.id) +"/" + obj.title.replace(" ", "-").lower().replace("/", "-").replace("\\", "-"))

class PostSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Post.objects.all()
    def lastmod(self, obj):
        return obj.updated