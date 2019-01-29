from bs4 import BeautifulSoup
import requests
import csv   



'''
###this was from an html file on your pc
with open('simple.html') as ht:
   s=BeautifulSoup(ht,'lxml')

#print(s)  # prints all of the html      
print(s.prettify())   # prints with all the indents 

a=s.title  # grabs the title
print(a)

b=s.title.text  # removes the <title> tag and grabs the text inside
print(b)

print(s.div)  # grabs the first <div> tag

m=s.find('div')     # finds the <div> tag
print(m)

j=s.find('div',class_='footer')   # finds the div tag with the specified attribute
print(j)

article=s.find('div',class_='article')
print(article)
headline=article.h2.a.text
print(headline)
summary=article.p.text
print(summary)

for inp in s.find_all('div',class_='article'):
   healin=inp.h2.a.text
   print(healin)

   summ=inp.p.text
   print(summ)

'''

# now we scrape from an actual website

source=requests.get('http://coreyms.com').text

soup=BeautifulSoup(source,'lxml')

csv_file=open('cms.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['headline','summaary','vid_link'])

#print(soup.prettify())
print('\n')
for article in soup.find_all('article'):
   print(article.prettify())
   try:
      heli=article.h2.a.text
      print(heli)
      suma=article.find('div',class_='entry-content').p.text
      print(suma)

      vid=article.find('iframe',class_='youtube-player')
      print(vid)

      vid=article.find('iframe',class_='youtube-player')['src'] # prints src attribute
      print(vid)

      vid_id=vid.split('/')[4]
      vid_id=vid_id.split('?')[0]
      print(vid_id)

      # creating a link
      ylink='https://youtube.com/watch?v={}'.format(vid_id)
      print(ylink)
   except Exception as e:
      print('nope')


   csv_writer.writerow([heli,suma,ylink])
csv_file.close()



