#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'your name'
SITENAME = 'your site name'
SITEURL = 'your url'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 1
PAGINATED_DIRECT_TEMPLATES = (('index', 'archives',))

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/home/detailyang/work/pelican/static-landing"

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
