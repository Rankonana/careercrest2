from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Post

class PostSitemap(Sitemap):
		changefreq = "daily"
		priority = 0.9
		
		def items(self):
				return Post.objects.all()
		
		def lastmod(self, obj):
				return obj.updated
		
		def location(self,obj):
			return '/blog/%s' % (str(obj.id) +"/" + obj.title.replace(" ", "-").lower().replace("/", "-").replace("\\", "-"))
