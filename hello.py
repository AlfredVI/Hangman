#CHAPTER IV FUNCTIONS
#Chalenge 1
#def square (x):
#	return x**2
#a=input("Entrez un nombre")
#a=int(a)
#b=square(a)
#print("Le carre de "+str(a)+ " est: "+str(b))

#Challenge 2
#def st(x):
#	print(x)
#a=input("Enter a string")
#st(a)

#Challenge 3
#def f(x,y,z,a=10,b=5):
#	return x*y-z+a*b
#d=input("d?")
#d=int(d)
#e=input("e?")
#e=int(e)
#h=input("h?")
#h=int(h)
#g=f(d,e,h)
#print(g)

#Challenge 4
#def div(x):
#	return x/2

#def mul(y):
#	return y*4

#a=input("nombre")
#a=int(a)
#b=div(a)
#c=mul(b)
#print(c)

#Challenge 5 - 6
#def conv(x):
#	"""
#	takes a string and converts it to a float pointing number
#	:param x:string
#	:return float, float of x
#	:exception handling catch the exception if the value given can't be converted to a floating point number
#	"""

#	try:
#		return float(x)

#	except ValueError:
#		print("Please enter a valid string")

#a=input("Donnez un nombre\n")
#b=conv(a)
#print(b)

#Chapter V Containers
#Challenges 1 - 2
#M=["The_Weeknd", "James_Blunt"]
#print(M)
#L=[("diourbel", "SN"),("thies", "SN"),("sophia", "FR")]
#print(L)

#Challenge 3 - 4
#ignace = {"height":"180", "weight":"74", "favorite color":"navy blue"}
#print(ignace)
#for p in ignace:
#	a=input("What's his "+p+" ?")
#	if a==ignace[p]:
#		print("You got it")
#	else:
#		print("Wrong answer")

#Challenge 5
#songz = {"The_Weeknd":"[Reminder, Six feet under, Ordinary life, The Hills, Lost in fire]", "James_Blunt":"[Ok, Into the dark, Dear Katie, These are the words]"}
#print(songz['The_Weeknd'])

#Chapter VI String manipulation
#Challenge 2
#a=input("enter response one")
#b=input("enter response two")
#c="Yesterday I wrote a {}. I sent it to {} !".format(a,b)
#print(c)

#Challenge 5
#>>> "aldous Huxley was born in 1894.".capitalize()
#'Aldous huxley was born in 1894.'
#>>> a="Where now? Who now? When now?".split("?")
#>>> print(a)
#['Where now', ' Who now', ' When now', '']
#>>> b=" ".join(["The", "fox", "jumped", "over", "the", "fence", "."])
#>>> print(b)
#The fox jumped over the fence .
#>>> b=b[:-2]+"."
#>>> print(b)
#The fox jumped over the fence.
#>>> "A screaming comes across the sky".replace("s","$")
#'A $creaming come$ acro$$ the $ky'
#>>> 

#Challenges 7 - 9
#>>> "Hemingway".index("m")
#2
#>>> "three"+" three"+" three"
#'three three three'
#>>> "three "*3
#'three three three '
 
#Challenge 10
#>>> ("It was a bright cold day in April, and the clocks were striking thirteen").split(",")
#['It was a bright cold day in April', ' and the clocks were striking thirteen']
#-----------------------------------------------------------------------------------------------------



#Chapter VII Loops
#Challenge 1
#l=["The walking dead","Entourage","The sopranos","The vampire diaries"]
#for i in l:
#	print(i)

#Challenge 2
#for i in range(25,51):
#	print(i)

#Challenge 3
#l=["The walking dead","Entourage","The sopranos","The vampire diaries"]
#k=0
#for i in l:
#	print(i+" at index "+str(k))
#	k += 1

#Challenge 4
#l=[1,64,84,15,4,42,13,54,8,47]
#while True:
	
#	a=input("guess the number or press q to quit\n")
#	if a== "q":
#		break
#	try:
#		a=int(a)
#	except ValueError:
#		print("Please type a number or press q to quit")
#	if a in l :
#		print("you guessed correctly\n")
#	else:
#		print("Try again\n")

#Challenge 5
#l1=[8,19,148,4]
#l2=[9,1,33,83]
#l3=[]
#for i in l1:
#	for j in l2:
#		k=i*j
#		l3.append(k)
#print(l3)
#---------------------------------------------------------------------------------

#chapter VIII Modules

#Challenge 1
#import statistics
#a=statistics.median([16.48,16.42,16.37])
#print(a)

#Challenge 2
#import chap8chal2
#b=input("Enter a number")
#a=chap8chal2.cube(b)
#print(a)

#--------------------------------------------------------------------------------

#Chapter IX Files
#Challenge 1
#import os
#x=os.path.join("/home","freddy","cle")
#print(x)
#with open (x,"r") as f:
#	print(f.read())

#Challenge 2
#ans=input("Hello! Tell us about something great in your life")
#with open ("answer.txt",'w') as fic:
#	fic.write(ans)

#Challenge 3
#import csv
#l=[["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
#with open("chal3.csv",'w') as f:
#	g=csv.writer(f,delimiter=",")
#	for i in range(0,len(l)):
#		g.writerow(l[i])

#Chapter X Bringing it all together
#Challenge
#import random
#def hangman():

#    m=["rainny","champion","plan","best","dominate","lifestyle","hacker"]
#    k=random.randint(0,((len(m))-1))
#    word=m[k]
#    wrong = 0
#    stages = ["",
#             "________        ",
#             "|               ",
#             "|        |      ",
#             "|        0      ",
#             "|       /|\     ",
#             "|       / \     ",
#             "|               "
#              ]
#    rletters = list(word)
#    board = ["__"] * len(word)
#    win = False
#    print("Welcome to Hangman")
#    while wrong < len(stages) - 1:
#        print("\n")
#        msg = "Guess a letter"
#        char = input(msg)
#        if char in rletters:
#            cind = rletters \
#                   .index(char)
#            board[cind] = char
#            rletters[cind] = '$'
#        else:
#            wrong += 1
#        print((" ".join(board)))
#        e = wrong + 1
#        print("\n"
#              .join(stages[0: e]))
#        if "__" not in board:
#            print("You win!")
#            print(" ".join(board))
#            win = True
#            break
#    if not win:
#        print("\n"
#              .join(stages[0: \
#              wrong]))
#        print("You lose! It was {}."
#              .format(word))


#hangman()
#m=["rainny","champion","plan","best","dominate","lifestyle","hacker"]
#k=random.randint(0,((len(m))-1))
#a=m[k]

#*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/**/*/*/*/*/*/*/*/**/*/*/*/*/*/*/*/*/*/*/*/
#Object-oriented programming
#Chapter XII

#Challenge 1
#class Apple():
#	"""docstring for Apple"""
#	def __init__(self, w,c,o,p):
#		self.weight=w
#		self.color=c
#		self.origin=o
#		self.price=p
#		print("apple created")
#ap=Apple(70,"red","france",1.2)
#print(ap)
#print(ap.price)

#Challenge 2	
#import math	
#class Circle():
#	def __init__(self,r):
#		self.ray=r
#		print("circle created")
#	def area (self):
#		return((math.pi)*self.ray*self.ray)
#cerc=Circle(2)
#print(cerc.area())

#Challenge 3
#class Triangle():
#	def __init__(self,b,h):
#		self.hauteur=h
#		self.base=b
#	def area(self):
#		return(self.base*self.hauteur/2)
#tri=Triangle(5,17)
#print(tri.area())

#Challenge 4
#class Hexagon():
	
#	def __init__(self,c1,c2,c3,c4,c5,c6):
#		self.first=c1
#		self.second=c2
#		self.third=c3
#		self.fourth=c4
#		self.fifth=c5
#		self.sixth=c6
#	def calculate_perimeter(self):
#		return self.first+self.second+self.third+self.fourth+self.fifth+self.sixth

#hx=Hexagon(5,6,8,7,2.5,24.9)
#print(hx.calculate_perimeter())
	
####################################################################################################
#Chapter XIII The four pilars of object-oriented programming	
#Challenges 1 - 2 - 3
#class Shape():
#	def what_am_i(self):
#		print("I am a shape")
#class Rectangle(Shape):
#	"""docstring for ClassName"""
#	def __init__(self, w,l):
#		self.width=w
#		self.len=l
#	def calculate_perimeter(self):
#		return 2*(self.width+self.len)
#class Square(Shape):
#	def __init__(self,c):
#		self.cote=c
#	def calculate_perimeter(self):
#		return 4*self.cote
#	def change_size(self,x):
#		self.cote=self.cote+x

#rec=Rectangle(5,3)
#print(rec.calculate_perimeter())
#sq=Square(5)
#print(sq.calculate_perimeter())
#sq.change_size(-2)
#print(sq.calculate_perimeter())
#rec.what_am_i()
#sq.what_am_i()

#Challenge 4
#class Horse():
#	def __init__(self,r,w,c):
#		self.rider=r
#		self.weight=w
#		self.color=c

#class Rider():
#	def __init__(self,n):
#		self.name=n

#john=Rider("John queen")
#jumper=Horse(john,95,"brown")
#print(john.name)
#print(jumper.rider.name)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#Chapter XIV More object-oriented programming
#Challenge 1 - 2
#class Square():
#	square_list=[]
#	def __init__(self,c):
#		self.cote=c
#		self.square_list.append((self.cote))
#	def __repr__(self):

#		return"{} by {} by {} by {}".format(self.cote,self.cote,self.cote,self.cote)

#sq=Square(5)
#sq2=Square(9)
#print(sq)
#print(sq2)

#Challenge 3
#class Person():
#	def __init__(self,n):
#		self.name=n

#x=Person("ET")
#same_x=x
#another_x=Person("ET")
#def f(a,b):
#	if a is b:
#		print("True")
#	else:
#		print("False")
#f(x,another_x)
#f(x,same_x)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#Chapter XV Bringing it all together
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#Regular expressions
#import re
#l="Beautiful is better than ugly"
#matches=re.findall("beautiful",l,re.IGNORECASE)
#print(matches)

#Chapter XVIII Packages
from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
	return "Hello World!"
app.run(port=8000)