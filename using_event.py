import pygame
screen=pygame.display.set_mode([1000,500])
run=True
screen.fill([255,255,255])
pygame.display.flip()
while(run):
 for event in pygame.event.get():
  if event.type==pygame.QUIT:
   print('wanna quit ')
   i=input()
   if i=='y':
    run=False
if i=='y':
 pygame.quit()




  

