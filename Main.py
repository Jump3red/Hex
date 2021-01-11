#coding:utf8
import os
try:
	os.system("cls")
	sh=open("ressources/SHARK.txt", "r")
	shark=sh.read()
	print(shark)
	def abc():
		rep=input("Votre réponse : ")
		if rep == "C":
			os.system("cls")
			from ressources.modules import SH4RK_CYPHER
		elif rep == "D":
			os.system("cls")
			from ressources.modules import SH4RK_DECYPHER
		else:
			print("Réponse non valide...\n")
			abc()
	abc()
	os.system("cls")
except KeyboardInterrupt:
    os.system("cls")
    exit()
