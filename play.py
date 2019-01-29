import pygame
screen=pygame.display.set_mode([1200,600])
pygame.display.set_caption("Let's play")
run=True
while(run):
 for event in pygame.event.get():
  if event.type==pygame.QUIT:
   pygame.quit()
  elif event.type==pygame.KEYDOWN:
   if event.key==pygame.K_LEFT:
    screen.fill([255,255,255])  
    pygame.draw.rect(screen,[0,255,0],[10,10,400,400],5)
    pygame.display.flip()
