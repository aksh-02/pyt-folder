import pyperclip
a=input('enter your text : ')
letters='abcdefghijklmnopqrstuvwxyz'
mode=input('encrypt or decrypt : ')
key=0
while (key%26)==0:
 key=int(input('enter the secret key : '))
a=a.lower()
trans=''

for sign in a:
 if sign in letters:
  num=letters.find(sign)
  if mode=='encrypt':
   num+=key
  elif mode=='decrypt':
   num-=key
  if num<0 or num>25:
   if num>25:
    num-=26
   elif num<0:
    num+=26
  trans=trans+letters[num]
 else:
  trans=trans+sign

print(trans)
pyperclip.copy(trans)
