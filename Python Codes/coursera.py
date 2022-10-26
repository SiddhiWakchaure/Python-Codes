'''l = []
while True:
    num = input("Enter a number: ")

    if num == "done":
        break
    try:
        num=int(num)
        l.append(num)
    except:
        print("Invalid input")


print("Maximum is",max(l))
print("Minimum is",min(l))


fname = input("Enter file name: ")
fh = open(fname,'r')
a=[]

for line in fh:
    line=line.rstrip()
    print(line)
    for i in line.split(" "):
        if i not in a:
            a.append(i)
a.sort()
print(a)
name = input("Enter file:")
handle = open(name)
x=[]
dict={}
for line in handle:
    line.rstrip()
    a=line.split(" ")
    if a[0]=="From":
        s=str(a[6])
        b=s.split(":")
        x.append(b[0])
for nos in x:
    dict[nos]=dict.get(nos,0)+1
y=sorted(dict.items())
for k,v in y:
    print(k,v)'''



#Acessing web data using python (import re)
'''import re
l=[]
sum=0
handle=open("actual data.txt",'r')
for line in handle:
    line.strip()
    x=re.findall('[0-9]+',line)
    if x!=[]:
        for i in x:
            l.append(i)
print(len(l))
for i in l:
    i=int(i)
    sum=sum+i
print(sum)'''

#Acessing web data using python(import socket)
'''import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()'''

#Acessing web data using Python(import urllib,etc for specific tags code1)
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

'''from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
l=[]

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    l.append(int(tag.contents[0]))
print("Count",len(l))
print("Sum",sum(l))'''




#Acessing web data using python(ipmort diff url lib code 2)
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

'''import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL- ')
a=int(input("Enter Count:"))
b=int(input("Enter Position:"))
print(url)
c=0
for i in range(a):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    #retrieves all anchor tag elements resembles like an anchor tag file
    tags = soup('a')
    for tag in tags:
        c=c+1
        if c%b==0:
            url=tag.get("href", None)
            print(url)
            break'''



#Acessing web data using python(import XML libs)
'''import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
l=[]
while True:
    url = input('Enter location: ')
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)
    results = tree.findall('comments/comment')
    print("Count:",len(results))
    for item in results:
        l.append(int(item.find('count').text))
    print("Sum:",sum(l))
    break
    #how to retrieve <c>abc</c> abc value if we found access to c tag????'''




#Acessing web data using python(import Json libs)
'''import urllib.request, urllib.parse, urllib.error
import json
import ssl
l=[]


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter URL:")
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

print('Retrieved', len(data), 'characters')
info = json.loads(data)

x = info["comments"]
for item in x:
    l.append(item["count"])
print("Count", len(l))
print("Sum", sum(l))'''




#Acessing web data using Python(import json, geojson API)
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print("Place id",js["results"][0]["place_id"])








































