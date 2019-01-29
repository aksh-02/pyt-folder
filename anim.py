import pygame
screen=pygame.display.set_mode([1000,500])
screen.fill([255,255,255])
for a in range(1,990):
 pygame.draw.rect(screen,[255,0,0],[a,200,50,100],10)
 pygame.display.flip()
 screen.fill([255,255,255])
 

run=True
while(run):
 for event in pygame.event.get():
  if event.type==pygame.QUIT:
   pygame.quit()
i=input('wanna leave ')
if i=='Y' or i=='y':
 pygame.quit()
