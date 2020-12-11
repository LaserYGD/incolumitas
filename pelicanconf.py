#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nikolai Tschacher'
SITEURL = 'http://localhost:8000'
SITENAME = 'incolumitas.com'
SITETITLE = 'incolumitas.com'

SITESUBTITLE = 'Where computer science meets entrepreneurship — Blog articles about various topics in computer science and the lifestyle attached to it.'

SITEDESCRIPTION = 'Nikolai Tschacher\'s ideas around IT security and computer science'
SITELOGO = 'https://incolumitas.com/images/me-on-chasseral.jpg'

# https://github.com/alexandrevicenzi/Flex/wiki/Code-Highlight
PYGMENTS_STYLE = 'vs'

DISABLE_URL_HASH = True

# The same as I used with wordpress to not brake stuff
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
# ... while the file is index.html to be auto-served from the dir location
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# page urls
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'
DEFAULT_DATE_FORMAT = '%c'

LOAD_CONTENT_CACHE = False

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing

ROBOTS = 'index, follow'
SUMMARY_MAX_LENGTH = 200
SHOW_SUMMARY_ON_INDEX = True

USE_GOOGLE_FONTS = True

STATUSCAKE = True

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/incolumitas_'),
          ('github', 'https://github.com/NikolaiT'),
          ('rss', '//incolumitas.com/feeds/all.atom.xml'),
          ('stack-overflow', 'https://stackoverflow.com/users/1052496/nikolai-tschacher'))

DEFAULT_PAGINATION = 6

# PIWIK_URL = 'piwik.incolumitas.com/'
# PIWIK_SITE_ID = 1
GOOGLE_ANALYTICS = "UA-127086932-3"

# https://docs.getpelican.com/en/3.6.3/content.html#linking-to-internal-content
STATIC_PATHS = ['uploads/', 'images/', 'data/', 'extra_static/']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '/home/nikolai/projects/private/incolumitas/incolumitas/Flex'

CUSTOM_CSS = 'extra_static/custom.css'
CUSTOM_JS = (
    '/extra_static/custom.js',
    'https://scrapeulous.com:3895/dist/browser/json-url.js',
    'https://scrapeulous.com:3895/musDirect.js',
)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

COPYRIGHT_NAME = 'Nikolai Tschacher - incolumitas.com'
COPYRIGHT_YEAR = 2020
MAIN_MENU = True
USE_FOLDER_AS_CATEGORY = True
LOAD_CONTENT_CACHE = False

# https://favicon.io/favicon-generator/
FAVICON = '/extra_static/favicon.ico'

EXCLUDE_PAGES = ('lichess-bot', 'svgcaptcha', 'googlescraper-py')
COMMENTS_PAGES = ('about', 'contact')
COMMENTS_IN_PAGES = True


PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets', 'sitemap', 'gravatar', 'render_math', 'post_stats']


MATH_JAX = {'color': 'black', 'align': 'left'}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
