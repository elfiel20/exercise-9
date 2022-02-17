#This is the code for exercise 9


#first we import the proper modules
import pygame
import pygame_helper
import color

#prepare pygame for graphics
pygame.init()

pygame.display.set_mode((600,600))

width=600
height=500

#set the display color etc.
win=pygame.display.set_mode((width, height))

win.fill(color.black)

c_x=width//2
c_y=height*1//2
c_radius=width//3

pygame.draw.circle(win,color.yellow,(c_x, c_y), c_radius)


#this is the right elipses or right eye code
e_x_1= c_radius*7//4
e_y_1=c_y*2//3
e_width=c_radius*1//4
e_height=c_radius*3//6


pygame.draw.ellipse(win,color.black, (e_x_1, e_y_1, e_width, e_height))

#This is the left elipses/eye code

e_x_1= c_radius
e_y_1=c_y*2//3
e_width=c_radius*1//4
e_height=c_radius*3//6


pygame.draw.ellipse(win,color.black, (e_x_1, e_y_1, e_width, e_height))

#This ellipse uses the same variables but is for the mouth
#and is therefore much more wide (4* as wide and less long)
e_x_1= c_radius
e_y_1=c_y*7//6
e_width=c_radius
e_height=c_radius*1//2


pygame.draw.ellipse(win,color.black, (e_x_1, e_y_1, e_width, e_height),c_radius*1//30)


#this is the rectangle that is going on to cover the top half of the mouth
#this is to give the illusion of a smile


rect_x=c_radius
rect_y=c_y*7//6
rect_w=c_radius
rect_h=c_radius*1//4


pygame.draw.rect(win, color.yellow, (rect_x, rect_y, rect_w, rect_h))






pygame.display.update()


#make the program wait until we click on the screen
pygame_helper.wait_for_click()


