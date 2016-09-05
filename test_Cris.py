import urllib2
import urllib
import time
import json
import os
from bs4 import BeautifulSoup as BS

#
#	URL para consultas: http://www.bookfinder.com/search/?keywords=9789876129978&new_used=&lang=&st=sh&ac=qr&submit=
#
#	ISBN de prueba
#	isbn = "9781937965044"		# Scrum: a Breathtakingly Brief and Agile Introduction
#	isbn = "9789876129091"		# Blackbird
#	isbn = "9789876129978"		# Deadfall. Atrapada

#	Lectura del archivo
isbnFile = open( u'isbnFile.xml', 'r' )

for isbn in isbnFile:
	tmp = isbn.rstrip()
	url = "http://www.bookfinder.com/search/?author=&title=&lang=es&isbn="+tmp+"&new_used=*&destination=es&currency=EUR&mode=basic&st=sr&ac=qr"
	response = urllib2.urlopen(url)
	html = response.read( )
	response.close()
	soup = BS( html, "html.parser" )
	print soup.title.string
	time.sleep( 1 )

isbnFile.close()

# isbn = "9789876129091"			# Deadfall. Atrapada
# url = "http://www.bookfinder.com/search/?keywords="+isbn+"&new_used=&lang=&st=sh&ac=qr&submit="
# url2 = "http://www.bookfinder.com/search/?author=&title=&lang=es&isbn="+isbn+"&new_used=*&destination=es&currency=EUR&mode=basic&st=sr&ac=qr"
# response = urllib2.urlopen(url2)
# html = response.read()
# response.close()
# soup = BS(html, "html.parser")
# print soup.title.string
#print html

#http://www.bookfinder.com/search/?author=&title=&lang=es&isbn=9789876129978&new_used=*&destination=es&currency=EUR&mode=basic&st=sr&ac=qr


#<form action="http://www.bookfinder.com/search/" method="GET" accept-charset="iso-8859-1" name="search_form" id="search_form" " class="search-form">