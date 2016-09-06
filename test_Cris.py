import urllib2
import urllib
import codecs
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
resultadoFile = codecs.open('resultado', 'w', 'utf-8')

print "Procesando el archivo isbnFile.xml"
for isbn in isbnFile:
	tmp = isbn.rstrip()
	url = "http://www.bookfinder.com/search/?author=&title=&lang=es&isbn="+tmp+"&new_used=*&destination=es&currency=EUR&mode=basic&st=sr&ac=qr"
	response = urllib2.urlopen(url)
	html = response.read()
	unicode_str = html.decode("iso-8859-1")
	enconde_str = unicode_str.encode("utf8")
	soup = BS( enconde_str, "html.parser" )
	print soup.title.string.rstrip('\n')
	response.close()
	resultadoFile.write(soup.title.string.rstrip('\n')+';'+tmp)
	time.sleep( 10 )
resultadoFile.close()
isbnFile.close()