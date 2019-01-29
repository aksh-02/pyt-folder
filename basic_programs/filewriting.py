#we are using context manager

with open('test.txt','w') as f:
 f.write('i just created a new file through write option and wrote this in it')
 seek(0) #sets the cursor position to 0 
