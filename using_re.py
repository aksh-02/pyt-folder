import re

Nage='''
Ram is 22 and a rich man Aman is smart and 34
Gabiel is 45 and Joey 54'''

ages=re.findall(r'\d{1,3}',Nage) # searches no.s of 1,2 or 3 digits
names=re.findall(r'[A-Z][a-z]*',Nage) # searches words with first alphabet capital

agedict={}
x=0
for eachname in names:
 agedict[eachname]=ages[x]
 x+=1

print(agedict)

for i in ages:
 print(i)

for j in names:
 print(j)

# searching for a word in a string
if re.search('inf','we need to inform with the latest information'):
 print('yes')

# searching for all the same words in a string
allinf=re.findall('inf','we need to inform with the latest information')
for i in allinf:
 print(i)

# printing the index of a word
st='we need to talk to him before he talks to us'
for i in re.finditer('talk',st):
 loctup=i.span()
 print(loctup)


str="Sat,hat,mat,pat"
allstr=re.findall("[shmp]at",str) 
#prints all words starting with s,h,m or p and ending with at
#[shmp] could be replaced with [s-p]
#using a caret symbol '^' before [s-p] like [^s-p] will exclude s and p
for i in allstr:
 print(i)
 
#replacing a particular piece of string
food="hat,rat,mat,pat"
regex=re.compile('[r]at')
food=regex.sub('elephant',food)
print(food)

randstr='here is a \\dog'
print(randstr) # will print a single backslash
print(re.search(r"\\dog",randstr)) # will print both the backslashes

rastr='''
Keep the blue flag
flying high
Chelsea
'''
print(rastr)
 
reg=re.compile("\n") #replaces '\n' with ''
rastr=reg.sub("",rastr)
print(rastr) 
 
'''other whitespaces include 
\b:backspace
\f:formfeed
\r:carriage return
\t:tab
\v:vertical tab
'''

rastring='12345'
print('Matches:',re.findall('\d',rastring))
#\d will search for digits
#\D will search for anything but numbers

num="24 4539 435453 3542215 675555754"
print(re.findall('\d{5,7}',num)) #finds all no.s with 5 to 7 digits
print(len(re.findall('\d{5,7}',num))) #finds number of no.s with 5 to 7 digits

#verifying phone numbers
# \w= [a-zA-Z0-9_]
# \W= [^a-zA-Z0-9_]

phn="421-454-4534" 
if re.search("\w{3}-\w{3}-\w{4}",phn):
 print("it is a phone number")

#\s=[\f\n\r\t\v]
#\S=[^\f\n\r\t\v]

#to check for a valid full name
name="Akshay Gandhi"
if re.search("\w{2,20}\s\w{2,20}",name):
 print('It is a valid full name')
# to check if the first alphabets are uppercase or not in a name
if re.search("[A-Z][a-z]*\s[A-Z][a-z]*",name):
 print('It indeed is a valid full name')

#to check no. of valid email ids
email="sk@aol.com md@.com @seo.com dc@.com"
print(len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",email)))

#web scraping
# to get phone numbers from a website 
# where numbers are in the form (234) 574-6576

import urllib.request
from re import findall

url="http://www.summet.com/dmsi/html/codesamples/addresses.html"
response=urllib.request.urlopen(url)
html=response.read()
htmlstr=html.decode()
pdata=findall("\(\d{3}\) \d{3}-\d{4}",htmlstr)

for item in pdata:
 print(item)


