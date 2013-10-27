#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'your name'
SITENAME = 'your site name'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 8
PAGINATED_DIRECT_TEMPLATES = ('blog',)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/home/detailyang/work/joshua/static-landing/static-landing"

PLUGIN_PATH = "/home/detailyang/work/joshua/static-landing/plugins"
PLUGINS = ['typepaginator',]

#recentposts
RECENT_POSTS_MAX = 5


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

#SIGNUP FORM TEXT
SIGNUP_FORM_TEXT_TITLE = "The Freelancer's Guide"
SIGNUP_FORM_TEXT_CONTENT = """
<p>Receive <strong>free tips</strong> on running a successful freelancing business! You’ll also be first in line to try out <strong>Static Buildup</strong> when it’s ready!</p>
"""

#FOLLOW_TEXT
FOLLOW_TEXT = "Follow us on Twitter"
