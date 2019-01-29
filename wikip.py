import wikipedia
+
print(wikipedia.summary('nikola tesla'))

print('\n')

print(wikipedia.summary('richard branson',3)) # to print exactly 3 lines

wikipedia.set_lang('fr')     # changes the language to french
print(wikipedia.summary('google',1))

print(wikipedia.search('kingfisher'))  # prints the titles of the articles

print('\n')
print(wikipedia.page('charles darwin').url) # prints the url of the page

print('\n')
print(wikipedia.page('charles darwin').title) # prints the title of the page

print('\n')
print(wikipedia.page('elon musk').content)  # prints the complete article


print(wikipedia.page('sachin tendulkar'))  # prints page object

print(wikipedia.page('queen elizabeth 2').images[0]) # generates the link of the image at index 0

# to download the image

import urllib.request
urllib.request.urlretrieve(wikipedia.page('william shakepeare').images[0],'will.jpg') # this will save the file in the same directory where the program is saved with the name as 'will.jpg'
