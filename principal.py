from bs4 import BeautifulSoup as BS
# Clase para la lectura de datos desde www.BookFinder.com
import BookFinder as BF
import urllib2
import urllib
import time
import os


# path = r'C:\Users\Ivette Escobar\Desktop\Python' # directory for search isbn.xml and save isbn json files.
# retval = os.getcwd()
# print ("Current working directory %s" % retval)
# os.chdir( path )
# retval = os.getcwd()
# print ("Directory changed successfully %s" % retval)

#	Lectura del archivo
listaISBN = open( u'isbnFile.xml', 'r' )
#resultadoFile = codecs.open('resultado', 'w', 'utf-8')

for isbn in listaISBN:
	tmp = isbn.rstrip()
	# Ejemplo de su uso
	objeto = BF.BookFinder( tmp )
	if ('No Okay' == objeto.obtenerDatos()):
		print tmp + ' - Error en la obtencion de datos'
	else:		
		print objeto.obtenerTitulo()
		print objeto.obtenerAutor()
		#objeto.obtenerImagen('/Users/Cris/consulta-libros/')
	

#resultadoFile.close()
listaISBN.close()