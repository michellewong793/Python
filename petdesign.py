#Tamagotchi 
#By Michelle Wong
#A pet that needs you to feed it and play games with it. 

from graphics import *
from random import randint 

class Pet:
    '''Creates pet'''
    def __init__(self):

        #creates the pet body
        center = Point(0,-30)
        self.radius = w/2
        self.rectp1 = Point(center.getX() - self.radius, center.getY())
        self.rectp2 = Point(center.getX() + self.radius, center.getY()- self.radius)
        
        self.pet = SemiCircle(self.radius, center, self.rectp1, self.rectp2)
        self.pet.color('khaki1', 'PaleGreen1')

        
        #creates the hat
        self.p1 = Point(0,60)
        self.p2 = Point(-25,15)
        self.p3 = Point(25,15)
        self.hat = Polygon(self.p1, self.p2, self.p3)

        #creates the eyes 
        self.center1 = Point(-25, -15)
        self.center2 = Point(25, -15)
        self.r = 7
        self.eye1 = Circle(self.center1,self.r)
        self.eye2 = Circle(self.center2, self.r+2)
        self.pupil = Circle(self.center1, 4)
        self.pupil2 = Circle(self.center2, 5)

        #creates mouth
        self.mouth = SemiCircle(self.r, Point(0,-15), Point(-self.r, -self.r), Point(self.r,-(self.r*2)))

        #creates the hunger bar
        self.hungerbar = Hunger(0)
 
    def getValue(self):
        '''Returns value of hunger meter'''
        self.h = self.hungerbar.getValue()
        return self.h

    def hungerPet(self):
        '''Lowers the value of  the pet'''
        self.hungerbar.lowerValue()

    def drawHunger(self,win):
        '''Draws hunger bar'''
        self.hungerbar.drawBox(win)
        
    def hungerDrawText(self,win):
        '''Draws text'''
        self.hungerbar.drawText(win)
        
    def undraw(self, win):
        '''Undraws pet'''
        self.pet.undraw()
        self.hat.undraw()
        self.eye1.undraw()
        self.eye2.undraw()
        self.pupil.undraw()
        self.pupil2.undraw()
        self.mouth.undraw()

    def undrawUnhappy(self,win):
        '''Undraws unhappy pet'''
        self.tail.undraw()
        self.mouth.undraw()

    def setLeft(self,pet,win):
        '''Sets pet to look to the left'''
        pet.undraw(win)
        self.pupil = Circle(Point(-30,-15),4)
        self.pupil2 = Circle(Point(20,-15),5)

    def setRight(self,pet,win):
        '''Sets pet to look to the right'''
        pet.undraw(win)
        self.pupil = Circle(Point(-20,-15),4)
        self.pupil2 = Circle(Point(30,-15),5)

    def resetPupils(self,pet,win):
        '''Resets pupils'''
        self.pupil = Circle(self.center1, 4)
        self.pupil2 = Circle(self.center2, 5)
         
    def draw(self, win):
        '''Draws pet'''
        self.pet.draw(win)
        self.hat.draw(win)
        self.eye1.draw(win)
        self.eye2.draw(win)
        self.pupil.draw(win)
        self.pupil2.draw(win)
        self.mouth.draw(win) 
        
        self.eye1.setFill('white')
        self.eye2.setFill('white')
        self.eye1.setOutline('white')
        self.eye2.setOutline('white')

        self.mouth.color('pink', 'khaki1')

        self.pupil.setFill('black')
        self.pupil2.setFill('black')
        
        self.hat.setFill('light blue')
        self.hat.setOutline('light blue')

    def setEmotion(self, value):
        '''Sets emotion of pet'''
        self.happiness = value
        #happy 
        if self.happiness == 1:
            self.p1 = Point(0, 70)
            self.p2 = Point(-25, 25)
            self.p3 = Point(25, 25)
            self.center1 = Point(-25, -15)
            self.center2 = Point(25, -15)
            self.r = 7
            self.eye1 = Circle(self.center1,self.r)
            self.eye2 = Circle(self.center2, self.r+2)
            self.pupil = Circle(self.center1, 4)
            self.pupil2 = Circle(self.center2, 5)
            self.hat = Polygon(self.p1, self.p2, self.p3)
            self.mouth = SemiCircle(self.r, Point(0,-15), Point(-self.r, -self.r), Point(self.r,-(self.r*2)))
        #sad 
        elif self.happiness == -1:
            self.p1 = Point(0,60)
            self.p2 = Point(-25,15)
            self.p3 = Point(25,15)
            self.hat = Polygon(self.p1, self.p2, self.p3)

            self.mouth = SemiCircle(self.r, Point(0,-(15+self.r)), Point(-self.r, -(15+self.r)), Point(self.r,-(self.r*2+15)))
            #second triangle 
            self.p4 = Point(35, 30)
            self.tail = Polygon(self.p1, self.p2, self.p4)
            self.tail.draw(win)
            self.tail.setFill('light blue')
            self.tail.setOutline('light blue')
        else:
        #neutral 
            self.p1 = Point(0,60)
            self.p2 = Point(-25,15)
            self.p3 = Point(25,15)
            self.hat = Polygon(self.p1, self.p2, self.p3)
            
    def getEmotion(self):
        '''Returns emotion level'''
        return self.happiness
    
class Hunger:
    '''Creates hunger meter'''
    def __init__(self,h):
        #sets the initial value to the value passed
        self.h = h
        self.box = Rectangle(Point(70,40), Point(80,-10))
        self.fill = Rectangle(Point(0,0), Point(0,0))

       
    def feed(self):
        '''Adds one to height'''
        self.h += 1
        topY = (self.h*10)-10
        if 6 > self.h >= 0 :
            self.fill = Rectangle(Point(70,topY), Point(80,-10))
        elif self.h == 6: 
            print('Taco full. You can play with taco!')
            

    def lowerValue(self):
        '''Lowers the value of the hunger meter'''
        topY = (self.h*10)-10
        if self.h > 0:
            self.h = self.h - 1
            self.fill = Rectangle(Point(70,topY),Point(80,-10))
        elif self.h == 0:
            self.fill = Rectangle(Point(0,0),Point(0,0))
            print('Taco very hungry. Feed Taco.')

    def feedBut(self):
        '''Creates feed button'''
        self.feedbut = Button(Point(-70,20),40,20,'Feed Taco')
        self.feedbut.activate() 
        
    def getValue(self):
        '''Returns value of hunger meter'''
        self.h = self.h
        return self.h
 
    def drawBox(self,win):
        '''Draws box outline'''
        self.box.setOutline('white')
        self.box.draw(win)
    
    def drawFill(self,win):
        '''Fills hunger meter'''
        self.fill.setOutline('cornflower blue')
        self.fill.setFill('cornflower blue')
        self.fill.draw(win)
        
    def undrawFill(self,win):
        '''Unfills hunger meter'''
        self.fill.undraw()

    def drawText(self,win):
        self.text = Text(Point(75,-15),'Hunger Meter')
        self.text.setSize(15)
        self.text.setFace('helvetica')
        self.text.setStyle('bold')
        self.text.setTextColor('cornflower blue')
        self.text.draw(win)
        
                 

class SemiCircle:
    '''Creates a semicircle'''
    def __init__(self, radius, center, rectp1, rectp2):
        self.radius = radius
        self.center = center
        self.rectp1 = rectp1
        self.rectp2 = rectp2 

        self.circ = Circle(center, radius)
        
        self.rect = Rectangle(self.rectp1, self.rectp2)

    def draw(self,win):
        '''Draws the circle and rectangle'''
        self.circ.draw(win)
        self.rect.draw(win) 

    def color(self,color, color2):
        '''Sets fill and outline to colors'''
        self.circ.setFill(color)
        self.rect.setFill(color2)
        self.circ.setOutline(color) 
        self.rect.setOutline(color2)
        
    def undraw(self):
        '''Undraws the semi-circle'''
        self.circ.undraw()
        self.rect.undraw()

class resultText():

    def __init__(self,pet, value,result):
        if value== result:
            self.text = Text(Point(0,-90),'Yippee! You won! Taco happy!')
        else:
            self.text = Text(Point(0,-90),'You lost. Taco sad.')
        self.text.setSize(20)
        self.text.setFace('helvetica')
        self.text.setStyle('bold')
        self.text.setTextColor('purple4')

    def draw(self,win):
        self.text.draw(win)

    def undraw(self,win):
        '''Undraws text'''
        self.text.undraw()
        
class Button:

    def __init__( self, pcent, width, height, strlabel ):

        w,h = width/2, height/2
        x,y = pcent.getX( ), pcent.getY( )
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point( self.xmin, self.ymin )
        p2 = Point( self.xmax, self.ymax )
        self.rect = Rectangle( p1, p2 )
        self.rect.setFill( 'pink' )
        self.rect.draw( win )
        self.textlabel = Text( pcent, strlabel )
        self.textlabel.setSize( 18 )
        self.strlabel = strlabel
        self.textlabel.draw( win )
        self.deactivate( )

    def clicked( self, p ):
        x,y = p.getX( ), p.getY( )
        bool_clicked = (self.active
                and
                self.xmin <= x <= self.xmax
                and
                self.ymin <= y <= self.ymax
                )
        return bool_clicked

    def activate( self ):
        self.textlabel.setFill( 'white' )
        self.rect.setWidth( 3 )
        self.rect.setOutline( 'cornflower blue' )
        self.active = True

    def deactivate( self ):
        self.textlabel.setFill( 'darkgray' )
        self.rect.setWidth( 1 )
        self.rect.setOutline( 'Black' )
        self.active = False

def Won(value, result):
    '''Determines if you have won game'''
    if value == result:
        return True
    return False

def feedPet(win,pet,feedbut, value):
    '''Feeds the pet'''
    pet.hungerbar.undrawFill(win)
    pet.hungerbar.feed()
    value = pet.hungerbar.getValue()
                   
def starvePet(win,pet,playbut,value):
    '''Makes the pet hungry'''
    pet.hungerbar.undrawFill(win)
    pet.hungerbar.lowerValue()
    value = pet.hungerbar.getValue()

def playGame(win, pet):
    '''Makes the buttons, starts the game and exits if quit is clicked'''
    
    #create the play and quit buttons 
    playbut = Button(Point(-70,70), 20, 30, 'Play' )
    quitbut = Button(Point(70,70), 20,30, 'Quit')
    #creates feed button
    feedbut = Button(Point(-70,20),40,20,'Feed Taco')
    Lbuts = [playbut, quitbut, feedbut]
    
    for but in Lbuts:
        but.activate()
        
    while True:
        p=win.getMouse()
        if quitbut.clicked(p):
            break

        left = Button(Point(-70,-60), 20,30,'Left')
        right = Button(Point(70,-60),20,30, 'Right')

        value= pet.getValue()
        if value == 0:
            print('Taco hungry. Please feed Taco.')
            pet.hungerbar.undrawFill(win)

 
         #feeds the pet and redraws hungerbar
        if feedbut.clicked(p):
            feedPet(win,pet,feedbut, value)
            if value <= 5: 
                pet.hungerbar.drawFill(win)

        #initiates game
        if playbut.clicked(p) and value != 0:

            #decreases hunger bar and redraws it
            if value != 0:
                starvePet(win,pet,playbut,value)
                pet.hungerbar.drawFill(win)
            
            playbut.deactivate()
         
            #undraws the previous emotion 
            if pet.getEmotion() == -1:
                pet.undraw(win)
                pet.undrawUnhappy(win)
                pet.setEmotion(1)
                pet.draw(win)
            
            left.activate()
            right.activate()

            print('Start game! Guess which side Taco will face!')
           
            #generates a random left or right when right or left is clicked
            x = win.getMouse()
            if right.clicked(x) or left.clicked(x):
                n = randint(0,1)
                
                if right.clicked(x):
                    print('You clicked right')
                    value = 0
                elif left.clicked(x):
                    print('You clicked left')
                    value = 1

                if n == 1:
                    pet.setLeft(pet,win)
                    print('Taco went left')
                    result = 1
                    
                elif n==0:
                    pet.setRight(pet, win)
                    print('Taco went right')
                    result = 0
                    
                
                #prints victory and resets pet 
                if Won(value, result):
                    pet.undraw(win)
                    print('You won. Click play to play again, or feed Taco.')
                    pet.setEmotion(1)
                    
                else:
                    pet.undraw(win)
                    pet.setEmotion(-1)
                    print('You lost. Click play to try again, or feed Taco.')

            #draws pet with new emotion after win or loss
 
            pet.draw(win)

            text = resultText(pet, value,result)
            text.draw(win)
            
            playbut.activate()

            win.getMouse()
            text.undraw(win)
            
    win.close()
               
def main():
    global win
    global w
    
    w = 100
    win = GraphWin('window',500,500)
    win.setCoords( -w, -w, w, w )
    win.setBackground('PaleGreen1')
    
    #creates pet
    pet = Pet()
    pet.setEmotion(0)
    pet.draw(win)

    #draws hunger meter and text 
    pet.drawHunger(win)
    pet.hungerDrawText(win)
    
    #play game
    playGame(win, pet)
   
    
main() 

    
