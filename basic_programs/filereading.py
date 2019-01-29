f=open('ad.txt','r')
print(f.name) #prints the name of the file
print(f.mode) #prints the mode in which the file is open
#print(f.readline( )) #prints the first line, 
#print(f.readline()) #printing this the second time would print the second line
print(f.tell) #tells the position of the cursor
f.seek(0) #sets the cursor position to 0 
#print(f.readlines()) #prints all the lines
#print(f.read()) #prints the file
#for line in f:
 #print(line,end='') #prints all lines 
print(f.read(100)) # prints the first 100 characters
f.close()


#we can open the file through context manager which doesn't require us to explicitly close the file, to do so
#with open('ad.txt','r') as f
#now we can do all the file operations as done normally 

