BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
import pygame
pygame.init()
screen=pygame.display.set_mode([1000,500])
pygame.display.set_caption("Gamer's Earth") #sets the title of the new window
screen.fill(WHITE) #fills the screen with white
a=0
for a in range(0,100,10):
 pygame.draw.line(screen,RED,[0,0+a],[100,100+a],5)
pygame.draw.rect(screen,BLACK,[100,190,250,100],1) #rectangle starts at i.e top most point is (100,190) with l=100 pxl and b=250 pxl
pygame.draw.ellipse(screen,BLACK,[350,190,250,100,],10) #draws an ellipse within a rectangle which starts at(350,190) and l=100pxl and b=250pxl
pygame.draw.arc(screen,BLUE,[350,290,250,250],0,1.57,5) #draws an arc from 0 to pi/2
pygame.draw.polygon(screen,BLACK,[(100,200),(200,250),(45,78)],5) #draws a polygon with as many given co-ordinates
font=pygame.font.SysFont('Calibri',40,True,False) #sets the font
text=font.render("this is awesome",True,BLACK) #this is text and color
screen.blit(text,[100,100]) # stamps the text on the screen
pygame.display.flip() #kind of refreshes for the new screen
x=input("wanna leave ")
if x=='Y' or x=='y':
 pygame.quit()
