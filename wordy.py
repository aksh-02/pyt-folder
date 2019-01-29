import pygame
import time

import enchant
d=enchant.Dict("en_US")

pygame.init()

# colours
white=[255,255,255]
black=[0,0,0]
red=[255,0,0]
bluish=[66,143,244]
greyish=[84,85,102]
greenish=[20,173,28]

stack=['0']

screen=pygame.display.set_mode([1000,700])
pygame.display.set_caption('The Word Game')	
screen.fill([255,255,255])
font=pygame.font.SysFont('Calibri',45,True,False)
p1=font.render('Player 1',True,[0,0,0])
p2=font.render('Player 2',True,[0,0,0])
screen.blit(p1,[50,40])
screen.blit(p2,[810,40])
s_1=font.render('Score : 0',True,greyish)
screen.blit(s_1,[45,90])
s_2=font.render('Score : 0',True,greyish)
screen.blit(s_2,[805,90])
pygame.display.flip()
start=time.time()

c=0
s1=0
s2=0
game_on=True
cause='play'
while game_on:

    pygame.draw.rect(screen,white,[400,0,260,33],0)
    c=(c+1)%2 or 2
    turn=font.render("Player {}'s turn".format(c),True,bluish)
    screen.blit(turn,[400,0])
    pygame.display.flip()

    a=input().lower()
# check if the word has been written before or can it be formed from the previous one or does it even exist in an english dictionary
    if not d.check(a):
        cause='no_word'
        break
    elif a in stack:
        cause='lost'
        break
    elif len(a)==len(stack[-1]):
        if len(list(filter(lambda x:x[0]!=x[1],zip(a,stack[-1]))))!=1:
            cause='form'
            break
    elif len(a)-len(stack[-1])==1:
        for i in range(len(stack[-1])):
            if a[i]!=stack[-1][i]:
               if a[i+1:]!=stack[-1][i:]:
                   cause='form'
               break
        if cause=='form':
            break
    else:
        cause='form'
        break

    stack.append(a)
    if c==1:
        s1+=len(a)
        pygame.draw.rect(screen,white,[0,80,400,185],0)
        s_1=font.render('Score : '+str(s1),True,greyish)
        pt1=font.render(a,True,red)
        screen.blit(s_1,[45,90])
        screen.blit(pt1,[10,150])
    else:
        s2+=len(a)
        pygame.draw.rect(screen,white,[600,80,400,185],0)
        s_2=font.render('Score : '+str(s2),True,greyish)
        pt2=font.render(a,True,red)
        screen.blit(s_2,[805,90])
        screen.blit(pt2,[790,150])
    pygame.display.flip()
# check the duration of the game play
    if time.time()-start>=60:
        cause='time'
        break


# game over screen
pygame.draw.rect(screen,white,[400,0,260,33],0)
over=font.render("Game Over",True,greenish)
screen.blit(over,[420,0])
pygame.draw.rect(screen,white,[0,150,400,185],0)
pygame.draw.rect(screen,white,[600,150,400,185],0)

if cause=='lost':
    win=font.render("Word written before, Player {} wins".format((c+1)%2 or 2),True,red)
    screen.blit(win,[200,300])
elif cause=='form':
    win=font.render("Word can't be formed, Player {} wins".format((c+1)%2 or 2),True,red)
    screen.blit(win,[200,300])
elif cause=='time':
    if s1>s2:
        win=font.render("Time is up, Player 1 wins",True,red)
    elif s1<s2:
        win=font.render("Time is up, Player 2 wins",True,red)
    else:
        win=font.render("Time is up, This is a tie",True,red)
    screen.blit(win,[260,300])    
elif cause=='no_word':
    win=font.render("Word doesn't exist, Player {} wins".format((c+1)%2 or 2),True,red)
    screen.blit(win,[230,300])
pygame.display.flip()
time.sleep(5)

# closing the window
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
pygame.quit()


