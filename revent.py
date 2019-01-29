import pygame
screen=pygame.display.set_mode([1000,500])
pygame.display.set_caption('random')
screen.fill([255,255,
254])
run=True
i='a'
while(run):
 for event in pygame.event.get():
  if event.type==pygame.QUIT:
   pygame.quit()
  elif event.type==pygame.KEYUP:
   pygame.draw.line(screen,[0,0,0],[10,10],[90,10],5)
   pygame.draw.line(screen,[0,0,0],[10,50],[90,50],5)
  elif event.type==pygame.KEYDOWN:
   i=input('wanna leave')
 if i=='y' or i=='Y':
  run=False 
 pygame.display.flip()
pygame.QUIT()
