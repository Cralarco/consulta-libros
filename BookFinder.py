from bs4 import BeautifulSoup as BS
import urllib2
import urllib
import time
import os

class BookFinder:
	"""Clase para obtener datos desde www.bookfinder.com"""
	urlConsulta1 = "http://www.bookfinder.com/search/?author=&title=&lang=es&isbn="
	urlConsulta2 = "&new_used=*&destination=es&currency=EUR&mode=basic&st=sr&ac=qr"
	def __init__( self, isbn ):
		self.url 	= self.urlConsulta1 + isbn + self.urlConsulta2
		self.isbn 	= isbn
	def obtenerDatos( self ):
		# Se crea objeto de la consulta a BookFinder
		html 		= urllib2.urlopen( self.url ).read()
		# Se decodifica el html en un string unicode
		unicode_str = html.decode( 'iso-8859-1' )
		# Se codifica el string en UTF-8
		enconde_str = unicode_str.encode( 'utf8' )
		# Se crea objeto con los datos de la consulta a BookFinder
		self.objetoHTML	= BS( enconde_str, "html.parser" )
		if (self.objetoHTML.find( "span" , 'page-breadcrumb' ).string == 'Search Error'):
			return 'No Okay'
		else:
			return 'Okay'

	def obtenerTitulo( self ):
		return self.objetoHTML.find( itemprop = 'name' ).string

	def obtenerAutor( self ):
		return self.objetoHTML.find( itemprop = 'author' ).string

	def obtenerImagen( self, directorio ):
		imagenSrc 	= self.objetoHTML.find( itemprop = 'image' )['src']
		urllib.urlretrieve(imagenSrc, directorio + self.isbn + '.jpg')