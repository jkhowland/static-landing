#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'your name'
SITENAME = 'your site name'
SITEURL = 'your url'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 1
PAGINATED_DIRECT_TEMPLATES = (('index', 'archives',))

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/path/to/static-landing"

PLUGIN_PATH = "/home/detailyang/pelican-plugins"
PLUGINS = ['neighbors',]

GOOGLE_ANALYTICS = 'UA-30756331-1'#GA code

#META ABOUT SEO
META_TITLE="you title"
META_DESCRIPTION="you title"
META_AUTHOR="you name"

#Socail URL
TWITTER_URL = "YOUR TWITTER URL"
FACEBOOK_URL = "YOUR FACEBOOK URL"
INSTAGRAM_URL = "YOUR TWITTER URL"
DRIBBBLE_URL = "YOUR TWITTER URL"

#landing page
ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
BLOG_SAVE_AS = 'blog/index.html'
DIRECT_TEMPLATES = ('index','blog')

#process the images and favicon.ico
STATIC_PATHS = ['images',
		'extra/favicon.ico',
		]
EXTRA_PATH_METADATA = {
		    'extra/favicon.ico': {'path': 'favicon.ico'},
		        }

JINJA_EXTENSIONS  = ['jinja2.ext.loopcontrols']
