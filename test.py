import urllib.request
import json
import os

path = r'C:\Users\Ivette Escobar\Desktop\Python' # directory for search isbn.xml and save isbn json files.
retval = os.getcwd()
print ("Current working directory %s" % retval)
os.chdir( path )
retval = os.getcwd()
print ("Directory changed successfully %s" % retval)

isbn = open(r"isbn.xml", 'r')

for link in isbn: # link is a line of isbn.xml.
  response = urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:"+link)
  data = response.read()
  file = open(r'isbn'+link+'.json', 'wb') # file is a archive JSON of isbn information from API GOOGLE BOOKS.
  file.write(data)
  file.close
  filejson=open(r'isbn'+link+'.json','r')
  print("File isbn",link,".json write OK")
  
isbn.close()
filejson.close()
