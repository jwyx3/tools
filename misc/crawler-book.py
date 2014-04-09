#!/usr/bin/env python
"""
Grab a book

python crawler-book.py http://www.siluke.com/0/5/5788/ |tee /tmp/queyuewutong.txt

"""

import urllib2, sys
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
  print __doc__
else:
  base_url = sys.argv[1]
  book_doc = urllib2.urlopen(base_url).read()
  book_soup = BeautifulSoup(book_doc)
  for a in book_soup.select('div#list dd > a[href]'):
    title = a.contents[0]
    chapter_doc = urllib2.urlopen(base_url + a['href'])
    chapter_soup = BeautifulSoup(chapter_doc)
    for content in chapter_soup.select('div#content'):
      print content.get_text('\n').encode('utf-8')
