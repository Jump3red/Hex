#coding: utf-8
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile
import time
'''
global e

def choix_chemin():
	global cheminrelatif
	cheminrelatif=askopenfile(mode="r", filetypes=[("Binary files", "*.bin")])

def callback():
    print(e.get())
    xpt=e.get()
    print(xpt)
'''
def main():
	x=0
	chemin="ressources/bin.bin"
	fichier=open(chemin,"r")
	contenu=fichier.read()
	'''e = Entry(root)
	e.pack()
	button2.pack()'''
	while x != len(contenu):
	    if int(contenu[x]) ==1 :
	        print("█", end="")
	        time.sleep(0.02)
	    elif int(contenu[x]) ==0 :
	        print(" ", end="")
	    else:
	    	print("", end="")
	    x=x+1
	    if x%6 ==0:
	        print("")
	#button3.pack()
	input("\n")

main()
'''
def yey():
	root.destroy()

root = tkinter.Tk() 
button1=tkinter.Button(root, text="Sélectionner un fichier", command=choix_chemin)
button1.pack()
button2=tkinter.Button(root, text="Lancer !", command=main)
button3=tkinter.Button(root, text="Quitter", command=yey)
b = Button(root, text="get", width=10, command=callback)
b.pack()
root.mainloop()
'''